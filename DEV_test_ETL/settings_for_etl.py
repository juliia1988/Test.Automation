import pyodbc
from azure.storage.blob import BlobServiceClient
import os


server = 'peprotosqlcarrizo.database.windows.net'
database = 'DR_Testing'
username = 'peprotosql'
password = 'Halliburton1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountpepepba38;AccountKey=rMNwWiGzF2qlQOOY/4KTNXlkRFBe3BUD2Jnxf7sme+nlLsQy84QVttaol55SV+oP/J/KeFjxYPaD2nv26MS/dg==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

local_path = "data"
local_file_name = str("Change_Operator_name") + ".csv"
upload_file_path = os.path.join(local_path, local_file_name)

