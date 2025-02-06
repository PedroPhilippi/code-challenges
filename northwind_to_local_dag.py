from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='daily_data_extraction',
    schedule_interval='@daily',  
    default_args=default_args,
    catchup=False,
) as dag:

    tables = ['orders']

    with TaskGroup("data_extraction") as extraction_group:
        for table in tables:
            task = DockerOperator(
                task_id=f"extract_{table}",
                image="meltano_northwind",
                command=(
                    f"meltano run tap-postgres-orders-{table} target-jsonl-{table}"
                    f"--select public.{table} "
                    f"--output /data/postgres/{table}/{{{{ ds }}}}/.json"

                ),
                docker_url="unix://var/run/docker.sock",
                network_mode="bridge",
                auto_remove=True,
                mount_tmp_dir=False,
               #volumes=["/opt/airflow/data:/data"],
            )

            # extraction_group >>