import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pyodbc

server = 'fracvaultstagingdbserver.database.windows.net'
database = 'DR_Testing'
username = 'fracvaultsql'
password = 'Halliburton1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

stg_connect_str = os.getenv('STAGE_AZURE_STORAGE_CONNECTION_STRING')
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

