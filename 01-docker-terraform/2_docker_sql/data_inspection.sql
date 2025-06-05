SELECT
	*
FROM
	zones
LIMIT 50;



SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
    CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc"
FROM
    yellow_taxi_trips t
JOIN
    zones zpu ON t."PULocationID" = zpu."LocationID"
JOIN
    zones zdo ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;




select
	*
from
	yellow_taxi_trips
where
	"DOLocationID" not in (
	select
		"LocationID"
	from
		zones);

select
	*
from
	yellow_taxi_trips
where
	"PULocationID" not in (
	select
		"LocationID"
	from
		zones);



select tpep_dropoff_datetime::date as "date", count(*)
from yellow_taxi_trips
group by tpep_dropoff_datetime::date;