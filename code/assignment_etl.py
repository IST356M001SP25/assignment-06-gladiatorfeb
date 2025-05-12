import pandas as pd
import json
from pandas import json_normalize
from apicalls import get_place_reviews, analyze_sentiment, extract_entities

CACHE_REVIEWS_FILE = "cache/reviews.csv"
CACHE_SENTIMENT_FILE = "cache/review_sentiment_by_sentence.csv"
CACHE_ENTITIES_FILE = "cache/review_sentiment_entities_by_sentence.csv"

def reviews_step(input_file="data/place_ids.csv"):
    if isinstance(input_file, str):
        df = pd.read_csv(input_file)
    else:
        df = input_file

    results = []
    for _, row in df.iterrows():
        place_id = row['place_id']
        place = get_place_reviews(place_id)
        if place and 'result' in place:
            result = place['result']
            result['place_id'] = place_id
            result['name'] = row.get('name', '')
            results.append(result)

    reviews_df = json_normalize(results, 'reviews', ['place_id', 'name'])
    reviews_df = reviews_df[['place_id', 'name', 'author_name', 'rating', 'text']]
    reviews_df.to_csv(CACHE_REVIEWS_FILE, index=False)
    return reviews_df


def sentiment_step(input_file=CACHE_REVIEWS_FILE):
    if isinstance(input_file, str):
        df = pd.read_csv(input_file)
    else:
        df = input_file

    results = []
    for _, row in df.iterrows():
        response = analyze_sentiment(row['text'])
        if response and 'documents' in response['results']:
            doc = response['results']['documents'][0]
            doc['place_id'] = row['place_id']
            doc['name'] = row['name']
            doc['author_name'] = row['author_name']
            doc['rating'] = row['rating']
            results.append(doc)

    sent_df = json_normalize(results, 'sentences', ['place_id', 'name', 'author_name', 'rating'])
    sent_df.rename(columns={'text': 'sentence_text', 'sentiment': 'sentence_sentiment'}, inplace=True)
    sent_df.to_csv(CACHE_SENTIMENT_FILE, index=False)
    return sent_df


def entity_extraction_step(input_file=CACHE_SENTIMENT_FILE):
    if isinstance(input_file, str):
        df = pd.read_csv(input_file)
    else:
        df = input_file

    results = []
    for _, row in df.iterrows():
        response = extract_entities(row['sentence_text'])
        if response and 'documents' in response['results']:
            for entity in response['results']['documents'][0].get('entities', []):
                entity['place_id'] = row['place_id']
                entity['name'] = row['name']
                entity['author_name'] = row['author_name']
                entity['rating'] = row['rating']
                entity['sentence_text'] = row['sentence_text']
                entity['sentence_sentiment'] = row['sentence_sentiment']
                entity['confidenceScores.positive'] = row['confidenceScores.positive']
                entity['confidenceScores.neutral'] = row['confidenceScores.neutral']
                entity['confidenceScores.negative'] = row['confidenceScores.negative']
                results.append(entity)

    entity_df = pd.DataFrame(results)
    entity_df.rename(columns={
        'text': 'entity_text',
        'category': 'entity_category',
        'subcategory': 'entity_subcategory',
        'confidenceScore': 'confidenceScores.entity'
    }, inplace=True)
    entity_df.to_csv(CACHE_ENTITIES_FILE, index=False)
    return entity_df


if __name__ == "__main__":
    reviews_step()
    sentiment_step()
    entity_extraction_step()
