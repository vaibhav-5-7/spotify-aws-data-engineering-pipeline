import boto3
import csv
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Extract bucket and object info
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download file
    download_path = '/tmp/artists.csv'
    s3.download_file(bucket, key, download_path)

    processed_key = 'processed/artists/artists_cleaned.csv'
    upload_path = '/tmp/artists_cleaned.csv'

    # Process CSV
    with open(download_path, 'r') as infile, open(upload_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        header = [h.strip().lower().replace(" ", "_") for h in header]
        writer.writerow(header)

        for row in reader:
            cleaned = [col.strip() for col in row]
            writer.writerow(cleaned)

    # Upload processed file
    s3.upload_file(upload_path, bucket, processed_key)

    return {"status": "success", "processed_file": processed_key}