import boto3

try:
    # Set up AWS credentials
    aws_id = 'XXXXXXXXXX'
    aws_secret = 'YYYYYYYY'
    aws_session = boto3.Session(
        aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret
    )

    # Initialize Textract client
    textract_client = aws_session.client('textract', region_name='us-east-1')

    # Read the input image file
    img_file = 'in.png'
    with open(img_file, 'rb') as img_handle:
        img_bytes = img_handle.read()

    # Call Textract to detect text
    textract_result = textract_client.detect_document_text(Document={'Bytes': img_bytes})

    # Output detected lines
    for block in textract_result['Blocks']:
        if block['BlockType'] == 'LINE':
            print(block['Text'])

except Exception as error:
    print(f"Error: {error}")