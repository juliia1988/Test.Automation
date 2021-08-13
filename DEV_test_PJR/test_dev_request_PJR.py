import os
import uuid
import json
from DEV_test_ETL.settings_for_etl import blob_service_client, cursor

new_file_name = str("autotest_") + str(uuid.uuid4()) + ".json"
local_path = "./json_data"
local_file_name = str("autotest") + ".json"
upload_file_path = os.path.join(local_path, local_file_name)

cursor.execute("SELECT NumAPI,Operator,TreatmentNumber FROM [dbo].[WellSummary] JOIN TreatmentSummary ON WellSummary.WellSummaryId = TreatmentSummary.WellSummaryId order by NEWID()")
row = cursor.fetchone()
new_numAPI = row[0]
new_operator = row[1]
new_treatmentNumber = row[2]

def test_update_json():
    try:
       # Update file in the local data directory

        f = open(upload_file_path, 'r')
        json_data = json.load(f)
        json_data['numAPI'] = [new_numAPI]
        json_data['operator'] = [new_operator]
        json_data['Intervals'] = [new_treatmentNumber]

        f = open(upload_file_path, 'w')
        f.write(json.dumps(json_data))

    except Exception as ex:
        print('Exception:')
        print(ex)

    print("Success update file with:_")
    print("\nNew file name:_\n\t" + new_file_name)
    print("\nNew numAPI:_\n\t" + new_numAPI)
    print("\nNew operator:_\n\t" + new_operator)
    print("\nNew treatmentNumber:_\n\t")
    print(new_treatmentNumber)

test_update_json()

def test_upload_json_to_blob():
    try:

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container="pjrequest", blob=new_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + new_file_name)

        # Upload the created file
        data = open(upload_file_path, "rb")
        blob_client.upload_blob(data, overwrite=True)

    except Exception as ex:
        print('Exception:')
        print(ex)

test_upload_json_to_blob()