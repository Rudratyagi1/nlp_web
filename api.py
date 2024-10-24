from textblob import TextBlob

# Function to perform NER
def ner(text):
    blob = TextBlob(text)
    entities = [{"text": np, "label": "NOUN PHRASE"} for np in blob.noun_phrases]
    return entities

# Function for sentiment analysis
def sentiment_analysis(text):
    blob = TextBlob(text)
    return {"polarity": blob.sentiment.polarity, "subjectivity": blob.sentiment.subjectivity}

# Function for abuse detection (simple keyword-based approach)
def abuse_detection(text):
    abuse_keywords = ["abuse", "hate", "violence", "bully", "attack"]
    for keyword in abuse_keywords:
        if keyword in text.lower():
            return True
    return False
