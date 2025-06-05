docker network create pg-network


docker-compose up -d 


URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
docker run -it  \
    --network=pg-network \
    taxi_ingest:v1 \
    --user=root \
    --password=root \
    --host=postgres \
    --port=5432 \
    --db=ny_taxi \
    --table-name=yellow_taxi_trips \
    --url=${URL}