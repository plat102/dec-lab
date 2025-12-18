
# Miniproject 1


## Yêu cầu 2

Processed jobs are loaded into PostgreSQL db: 
![Jobs loaded into PostgreSQL db](images/db_jobs.png)

Scheduled job runs the ETL pipeline every 1 min via [run_pipeline.sh](scripts/run_pipeline.sh):
![img.png](images/cron_job.png)