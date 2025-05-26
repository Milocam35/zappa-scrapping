import json
import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'parcial3-bigdata'

def app(event, context):
    now = datetime.utcnow().strftime('%Y-%m-%d')
    urls = {
        'eltiempo': 'https://www.eltiempo.com',
        'elespectador': 'https://www.elespectador.com'
    }

    for name, url in urls.items():
        response = requests.get(url)
        content = response.text

        key = f"headlines/raw/{name}-contenido-{now}.html"
        s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=content, ContentType='text/html')

    return {
        'statusCode': 200,
        'body': json.dumps('Páginas descargadas y subidas a S3 correctamente.')
    }
