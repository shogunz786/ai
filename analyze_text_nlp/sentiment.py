import boto3

try:
    # AWS credentials configuration
    aws_key = ''
    aws_secret = ''
    aws_session = boto3.Session(
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret
    )

    # Create Comprehend client
    comprehend_client = aws_session.client('comprehend', region_name='us-east-1')

    # Text for sentiment analysis
    review_text = "The weather today is absolutely wonderful and uplifting."

    # Detect sentiment in the text
    sentiment_result = comprehend_client.detect_sentiment(Text=review_text, LanguageCode='en')

    # Output the sentiment
    print(sentiment_result['Sentiment'])

except Exception as err:
    print(f"Error: {err}")