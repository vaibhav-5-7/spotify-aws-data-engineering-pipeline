CREATE EXTERNAL TABLE IF NOT EXISTS spotify_tracks (
    track_id string,
    track_name string,
    artist_id string,
    popularity int,
    duration_ms int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar"     = "\""
)
LOCATION 's3://<your-bucket-name>/processed/tracks/'
TBLPROPERTIES ('has_encrypted_data'='false');