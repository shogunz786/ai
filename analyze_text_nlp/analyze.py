import boto3

try:
    # AWS credentials setup
    key_id = 'XXXX'
    key_secret = 'YYY'
    aws_sess = boto3.Session(
        aws_access_key_id=key_id,
        aws_secret_access_key=key_secret
    )

    # Textract client initialization
    textract_client = aws_sess.client('textract', region_name='us-east-1')

    # S3 client initialization
    s3_client = aws_sess.client('s3', region_name='us-east-1')

    # S3 bucket and file details
    s3_bucket = 'abcd'
    s3_key = 'one.png'

    s3_file = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    doc_ref = {'S3Object': {'Bucket': s3_bucket, 'Name': s3_key}}

    # Textract analyze_document call
    textract_output = textract_client.analyze_document(
        Document=doc_ref,
        FeatureTypes=['TABLES', 'FORMS', 'SIGNATURES', 'QUERIES'],
        QueriesConfig={'Queries': [
            {'Text': '{}'.format('How much is the work experience of the candidate?')}
        ]}
    )

    # Print the response
    print_response(textract_output)

except Exception as err:
    print(f"Error: {err}")