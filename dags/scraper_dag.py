from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    'scrape_and_upload_to_adls2',
    default_args=default_args,
    description='A simple DAG to run Selenium scraper',
    schedule_interval=None,
)

def install_requirements():
    url = "http://selenium-chrome:4444/install-requirements"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error installing requirements: {e}")

install_requirements_task = PythonOperator(
    task_id='install_requirements',
    python_callable=install_requirements,
    dag=dag,
)

def run_scraper():
    url = "http://selenium-chrome:4444/run-scraper"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error running scraper: {e}")

run_scraper_task = PythonOperator(
    task_id='run_scraper',
    python_callable=run_scraper,
    dag=dag,
)

def upload_file_to_adls2():
    url = "http://selenium-chrome:4444/upload-file"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")

upload_file_task = PythonOperator(
    task_id='upload_file_to_adls2',
    python_callable=upload_file_to_adls2,
    dag=dag,
)

install_requirements_task >> run_scraper_task >> upload_file_task
