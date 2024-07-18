from flask import Flask
import subprocess

app = Flask(__name__)

# Update pip and install requirements.txt
@app.route('/install-requirements', methods=['GET'])
def update_pip_and_install_requirements():
    try:
        # Update pip
        subprocess.run(['pip', 'install', '--upgrade', 'pip'], check=True)
        # Install requirements.txt
        subprocess.run(['pip', 'install', '-r', '/shared/requirements.txt'], check=True)
        return "Requirements Installed Successfully"
    except subprocess.CalledProcessError as e:
        return f"Unxpected Error: {str(e)}"
        
@app.route('/run-scraper', methods=['GET'])
def run_scraper():
    try:
        result = subprocess.run(['python', '/shared/scraper.py'], check=True, capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error running subprocess command: {str(e)}'
    except Exception as e:
        return f'Unexpected error: {str(e)}'

@app.route('/upload-file', methods=['GET'])
def upload_file():
    try:
        # Run the script to upload files
        result = subprocess.run(['python', '/shared/upload_file.py'], check=True, capture_output=True, text=True)
        print("File Uploaded Successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error running subprocess command: {str(e)}'
    except Exception as e:
        return f'Unexpected error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
