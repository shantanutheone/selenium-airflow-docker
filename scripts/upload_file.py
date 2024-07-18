
import os
from azure.storage.blob import BlobServiceClient, BlobClient
import shutil

# Azure Storage Blob details
ADLS_ACCOUNT_NAME = ""
ADLS_CONTAINER_NAME = ""
AZURE_STORAGE_ACCOUNT_KEY = ""  # Replace with your storage account key primary key
DIRECTORY_TO_UPLOAD = "scrape_results"

def upload_to_adls(directory_path, account_name, container_name, account_key):
    # Construct the BlobServiceClient using the account key
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
    
    # List files in the directory
    files = os.listdir(directory_path)
    
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        
        # Upload file to ADLS Gen2
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print(f"Uploaded {file_name} to Azure Blob Storage")

def delete_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Deleted directory {directory_path} successfully")
    except Exception as e:
        print(f"Failed to delete directory {directory_path}: {str(e)}")

if __name__ == "__main__":
    # Check if the directory exists
    if os.path.exists(DIRECTORY_TO_UPLOAD):
        # Upload files to ADLS Gen2
        upload_to_adls(DIRECTORY_TO_UPLOAD, ADLS_ACCOUNT_NAME, ADLS_CONTAINER_NAME, AZURE_STORAGE_ACCOUNT_KEY)
        
        # Delete the directory after successful upload
        delete_directory(DIRECTORY_TO_UPLOAD)
    else:
        print(f"Directory {DIRECTORY_TO_UPLOAD} does not exist")
