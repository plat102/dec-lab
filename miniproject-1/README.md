
# Miniproject 1

## Yêu cầu 1
- Quick solution in notebook: [01_etl_quick.ipynb](notebooks/01_etl_quick.ipynb)
- ETL source: [src/](src/main.py)

## Yêu cầu 2

Processed jobs are loaded into PostgreSQL db: 
![Jobs loaded into PostgreSQL db](images/db_jobs.png)

Scheduled job runs the ETL pipeline every 1 min via [run_pipeline.sh](scripts/run_pipeline.sh):
![img.png](images/cron_job.png)

Unit testing for transform functions with `pytest`
![img.png](images/unit_test.png)

## Yêu cầu 3
Data analysis notebook with charts included:
[03_analysis.ipynb](notebooks/03_analysis.ipynb):
