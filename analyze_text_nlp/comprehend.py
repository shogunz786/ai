import boto3

try:
    # AWS credentials setup
    aws_id = ''
    aws_secret = ''
    aws_session = boto3.Session(
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret
    )

    # Initialize Comprehend client
    comprehend_client = aws_session.client('comprehend', region_name='us-east-1')

    # Text to analyze
    sample_text = "Ada Lovelace is considered the first computer programmer."

    # Detect entities in the text
    result = comprehend_client.detect_entities(Text=sample_text, LanguageCode='en')

    # Output detected entities
    for item in result['Entities']:
        print('Text:"{0}" Type:{1} Score:{2}'.format(item['Text'], item['Type'], item['Score']))

except Exception as error:
    print(f"Error: {error}")