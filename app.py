from flask import Flask, jsonify
from azure.storage.fileshare import ShareServiceClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def list_files():
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    share_name = os.getenv("AZURE_STORAGE_SHARE_NAME")
    
    share_service_client = ShareServiceClient.from_connection_string(connect_str)
    share_client = share_service_client.get_share_client(share_name)
    files = share_client.list_directories_and_files()
    
    files_list = [file_or_dir.name for file_or_dir in files]
    
    return jsonify(files_list)

if __name__ == '__main__':
    app.run(debug=True)
