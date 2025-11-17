import boto3
import csv
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = '/tmp/tracks.csv'
    upload_path = '/tmp/tracks_cleaned.csv'
    processed_key = 'processed/tracks/tracks_cleaned.csv'

    s3.download_file(bucket, key, download_path)

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

    s3.upload_file(upload_path, bucket, processed_key)

    return {"status": "success", "processed_file": processed_key}