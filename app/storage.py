import boto3
from app import app

s3_client = boto3.client(
    's3',
    aws_access_key_id=app.config['AWS_ACCESS_KEY'],
    aws_secret_access_key=app.config['AWS_SECRET_KEY']
)

def upload_file_to_s3(file, filename):
    s3_client.upload_fileobj(file, app.config['AWS_S3_BUCKET'], filename)

def get_file_from_s3(filename):
    response = s3_client.get_object(Bucket=app.config['AWS_S3_BUCKET'], Key=filename)
    return response['Body'].read()
