import uuid
import time
from STAGE_test_ETL.settings_for_etl import blob_service_client, local_file_name, upload_file_path, cursor
import allure
operator = str(uuid.uuid4())
salesOrderNumber = str(uuid.uuid4())
fluidDescription = str(uuid.uuid4())

@allure.feature('Check ETL function')
@allure.story('Update CSV file')
@allure.step
def test_update_csv():
    try:
        # Открываем файл только для чтения
        f = open(upload_file_path, 'r')
        lines = f.readlines()
        lines[7] = 'Customer,' + operator + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n'
        lines[12] = 'Sales Order #,' + salesOrderNumber + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n'
        lines[170] = '6/9/2021 7:07,2,' + fluidDescription + ',,0,0,0,0,0,0,60,0,3.581302643,-9.75969357,21.84483676,3714.887153,0,-35.17467584,755.2437609,0,0,10.00811688,8.421172748,8.421172748,0,0,0,0.045299999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,60,0,0' + '\n'

        f.close()

        # Открываем файл для записи
        save_changes = open(upload_file_path, 'w')
        # Сохраняем список строк
        save_changes.writelines(lines)

        # Закрываем файл
        save_changes.close()

    except Exception as ex:
        print('Exception:')
        print(ex)

    print("Success: changed file with new Operator,SalesOrder,FluidDescription")

test_update_csv()

@allure.feature('Check ETL function')
@allure.story('Upload local file to Azure dev storage Landing container')
@allure.step
def test_upload_updated_csv_to_blob():
    try:
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container="landing",
                                                          blob=operator + '_' + local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        print("\nOperator:_\n\t" +operator)
        print("\nSales Order:_\n\t" +salesOrderNumber)
        print("\nFluid Description:_\n\t" +fluidDescription)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

    except Exception as ex:
        print('Exception:')
        print(ex)

test_upload_updated_csv_to_blob()

def test_data_base_check_data():
    time.sleep(10)
    cursor.execute("Select Operator, SalesOrdernumber, FluidDescription from [dbo].WellSummary "
                   "INNER JOIN TreatmentSummary on TreatmentSummary.WellSummaryId = WellSummary.WellSummaryId "
                   "INNER JOIN TreatmentSummaryTimeHistory on TreatmentSummaryTimeHistory.TreatmentSummaryId = TreatmentSummary.TreatmentSummaryId "
                   f"where Operator = '{operator}' AND SalesOrdernumber = '{salesOrderNumber}'")

    row = cursor.fetchone()
    new_operator = row[0]
    new_salesOrder = row[1]
    new_fluidDescription = row[2]
    print(new_operator, new_salesOrder, new_fluidDescription)
    print("Start paring:")

    assert new_operator == operator, 'значения operator не равны'
    print("Paired success")

    assert new_salesOrder == salesOrderNumber, 'значения Sales Order не равны'
    print("Paired success")

    assert new_fluidDescription == fluidDescription, 'значения fluidDescription не равны'
    print("Paired success")


test_data_base_check_data()

