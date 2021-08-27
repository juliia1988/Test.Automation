import pyodbc
from azure.storage.blob import BlobServiceClient
import os

server = 'fracvaultstagingdbserver.database.windows.net'
database = 'DR_Testing'
username = 'fracvaultsql'
password = 'Halliburton1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

stg_connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountpepepb62e;AccountKey=ryg/iMmlzyjJR6SAtuhzshJ04MAt4MD0dU3ZwL8m4ZQPZWW0SCMFqgHfESe/OY9g/Ob3sYkHWM3Hy2AH8RpVYw==;EndpointSuffix=core.windows.net"
service = BlobServiceClient.from_connection_string(conn_str=stg_connect_str)
blob_service_client = BlobServiceClient.from_connection_string(stg_connect_str)

local_path = "data"
local_file_name = str("Change_Operator_name") + ".csv"
upload_file_path = os.path.join(local_path, local_file_name)

