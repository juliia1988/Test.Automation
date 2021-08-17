import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pyodbc

server = 'fracvaultstagingdbserver.database.windows.net'
database = 'DR_Testing'
username = 'fracvaultsql'
password = 'Halliburton1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#stg_connect_str = os.getenv('STAGE_AZURE_STORAGE_CONNECTION_STRING')
stg_connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountpepep9765;AccountKey=gr2XHdMUhXPTtq2V5NW19dZGs3LsP2ZHl7dYah/yV2XgvbID/SXg8ji8UfbFsdKErTWLnZY+1iFF+B2zKrGT9A==;EndpointSuffix=core.windows.net"
service = BlobServiceClient.from_connection_string(conn_str=stg_connect_str)
blob_service_client = BlobServiceClient.from_connection_string(stg_connect_str)

local_path = "stage_data"
local_file_name = str("autotest_pjr") + ".json"
upload_file_path = os.path.join(local_path, local_file_name)

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)

