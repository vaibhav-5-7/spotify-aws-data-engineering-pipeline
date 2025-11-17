🎵 Spotify Data Engineering Pipeline (AWS Serverless Architecture)

1. Project Overview

This project implements an end-to-end serverless data engineering pipeline on AWS for processing Spotify dataset files.
Raw CSV files are ingested into an Amazon S3 data lake, transformed using AWS Lambda, organized into a processed layer, cataloged using AWS Glue, and queried through Amazon Athena.

The solution follows a modern, cloud-ready architecture aligned with real-world data engineering practices.

⸻

2. Architecture

                  ┌──────────────────────┐
                  │     S3 (raw layer)   │
                  │   Raw Spotify CSVs   │
                  └──────────┬───────────┘
                             │  S3 Event Trigger
                             ▼
                  ┌──────────────────────┐
                  │     AWS Lambda       │
                  │   ETL Processing     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ S3 (processed layer) │
                  │  Cleaned CSV Output  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ AWS Glue Data Catalog│
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │     Amazon Athena    │
                  │   SQL-Based Querying │
                  └──────────────────────┘

3. AWS Services Used

Service	Purpose
Amazon S3	Raw and processed data lake storage
AWS Lambda	Serverless ETL written in Python
S3 Event Notifications	Trigger Lambda on file upload
AWS Glue Data Catalog	Schema definitions for Athena
Amazon Athena	SQL querying directly on S3
IAM	Secure access and role management

4. Data Flow

Step 1 — Data Ingestion (S3 Raw Layer)

Raw Spotify CSV files (artists.csv, tracks.csv) are uploaded to the raw/ folder in S3.

Step 2 — ETL Processing (AWS Lambda)

Triggered automatically by S3 events.
Lambda performs:
	•	Data cleaning
	•	Type conversions
	•	Field normalization
	•	Validation
	•	Saves transformed output into the processed/ layer

Step 3 — Catalog Creation (AWS Glue)

Glue databases and tables are configured to map the processed S3 paths.

Step 4 — Querying (Amazon Athena)

Athena enables SQL queries on the cleaned dataset for analysis and reporting.

5. S3 Data Lake Structure

s3://<bucket-name>/
│
├── raw/
│   ├── artists.csv
│   └── tracks.csv
│
└── processed/
    ├── artists/
    │   └── artists_cleaned.csv
    └── tracks/
        └── tracks_cleaned.csv

6. Sample Athena Queries

Top Artists by Followers

SELECT artist_name, followers
FROM spotify_artists
ORDER BY followers DESC
LIMIT 10;

Popular Tracks (Popularity > 80)

SELECT track_name, popularity
FROM spotify_tracks
WHERE popularity > 80;

7. IAM & Security
	•	Lambda execution role with S3 and Glue permissions
	•	CloudWatch logging enabled
	•	Least privilege IAM policies used for security

8. Key Features
	•	Event-driven, fully serverless architecture
	•	Raw → Processed data lake modeling
	•	Automated ETL pipeline using Lambda
	•	Schema management using Glue Catalog
	•	Cost-efficient and free-tier friendly
	•	Queryable datasets using Athena SQL

9. Future Enhancements
	•	PySpark-based ETL using AWS Glue Jobs
	•	Apache Airflow or Step Functions orchestration
	•	Redshift integration for warehousing
	•	CI/CD using CodePipeline or GitHub Actions
	•	API ingestion pipeline

10. Author

Vaibhav Panade
Data Engineering | AWS | Python | SQL