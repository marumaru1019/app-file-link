import streamlit as st
from azure.storage.fileshare import ShareServiceClient
import os
from dotenv import load_dotenv


load_dotenv()
st.title("Azure Files Explorer")

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
share_name = os.getenv("AZURE_STORAGE_SHARE_NAME")

def list_files():
    share_service_client = ShareServiceClient.from_connection_string(connect_str)
    share_client = share_service_client.get_share_client(share_name)
    files = share_client.list_directories_and_files()
    return [file_or_dir.name for file_or_dir in files]

files_list = list_files()
st.write("Files in Azure Files:")
for file in files_list:
    st.write(file)
