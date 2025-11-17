CREATE EXTERNAL TABLE IF NOT EXISTS spotify_artists (
    artist_id string,
    artist_name string,
    followers int,
    genres string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar"     = "\""
)
LOCATION 's3://<your-bucket-name>/processed/artists/'
TBLPROPERTIES ('has_encrypted_data'='false');