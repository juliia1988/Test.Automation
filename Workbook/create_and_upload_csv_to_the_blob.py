import os, uuid
from azure.storage.blob import BlobServiceClient
from settings_for_etl import blob_service_client

def create_csv_and_upload_to_blob(local_path = "./data"):
    try:
        # Create a local directory to hold blob data
        #local_path = "./data"

        # Create a file in the local data directory to upload and download
        local_file_name = str("autotest_") + str(uuid.uuid4()) + ".csv"
        upload_file_path = os.path.join(local_path, local_file_name)

        # Write text to the file
        file = open(upload_file_path, 'w')
        file.write("Yuliia Sokolova Test")
        file.close()

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container="autotest", blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

    except Exception as ex:
        print('Exception:')
        print(ex)

    print("Success")

create_csv_and_upload_to_blob()

