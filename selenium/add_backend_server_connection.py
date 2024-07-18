import subprocess

def create_connection():
    try:
        command = [
            "airflow", "connections", "add", "backend_server",
            "--conn-type", "http",
            "--conn-host", "selenium-chrome",
            "--conn-port", "4444"
        ]
        subprocess.check_call(command)
        print("Connection `backend_server` added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add connection `backend_server`: {e}")

if __name__ == "__main__":
    create_connection()
