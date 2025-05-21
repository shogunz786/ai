import boto3

try:
    # AWS credentials setup
    my_access_key = ''
    my_secret_key = ''
    my_session = boto3.Session(
        aws_access_key_id=my_access_key,
        aws_secret_access_key=my_secret_key
    )

    # Initialize Comprehend client
    nlp_client = my_session.client('comprehend', region_name='us-east-1')

    # Text to analyze
    sample_sentence = "Artificial intelligence is transforming many industries rapidly."

    # Detect syntax tokens in the text
    syntax_result = nlp_client.detect_syntax(Text=sample_sentence, LanguageCode='en')

    # Output syntax tokens
    for word in syntax_result['SyntaxTokens']:
        print('Token:"{0}" POS:{1} Confidence:{2}'.format(
            word['Text'], word['PartOfSpeech']['Tag'], word['PartOfSpeech']['Score'])
        )

except Exception as error:
    print(f"Error: {error}")