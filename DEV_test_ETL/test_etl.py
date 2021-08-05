import uuid
import time
from DEV_test_ETL.settings_for_etl import blob_service_client, local_file_name, upload_file_path
from DEV_test_ETL.settings_for_etl import cursor
import allure
operator = str(uuid.uuid4())
salesOrderNumber = str(uuid.uuid4())
fluidDescription = str(uuid.uuid4())

#Check for WellSummary table:

@allure.feature('Check ETL function')
@allure.story('Update CSV file')
@allure.step
def test_update_csv_with_new_operator():
    try:
        # Открываем файл только для чтения
        f = open(upload_file_path, 'r')
        lines = f.readlines()
        lines[7] = 'Customer,' + operator + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n'
        lines[12] = 'Sales Order #,' + salesOrderNumber + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n'
        lines[170] = '6/9/2021 7:07,2,' + fluidDescription + ',,0,0,0,0,0,0,60,0,3.581302643,-9.75969357,21.84483676,3714.887153,0,-35.17467584,755.2437609,0,0,10.00811688,8.421172748,8.421172748,0,0,0,0.045299999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,60,0,0' + '\n'
        print("Operator:" + operator)
        print("SalesOrder" + salesOrderNumber)
        print("FluidDesctription" + fluidDescription)
        # Закрываем файл
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

test_update_csv_with_new_operator()

@allure.feature('Check ETL function')
@allure.story('Upload local file to Azure dev storage Landing container')
@allure.step
def test_upload_updated_csv_to_blob():
    time.sleep(10)
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

@allure.feature('Check ETL function')
@allure.story('Check Operator')
@allure.step
def test_data_base_check_operator():
    time.sleep(10)
    cursor.execute("select Operator from WellSummary where numAPI = '42-003-48292-00'")
    row_operator = cursor.fetchone()
    print("Start paring:")
    print(row_operator)

    assert row_operator[0] == operator, 'значения не равны'
    print("Paired success")

test_data_base_check_operator()

#Check for TreatmentSummary table:

@allure.feature('Check ETL function')
@allure.story('Check Sales Order')
@allure.step
def test_check_new_salesOrderNumber():
     time.sleep(10)
     cursor.execute("select SalesOrdernumber from TreatmentSummary where WellSummaryId = '5C03FAE2-53D8-4134-886B-BFCDAC061047' and TreatmentNumber = '2'")
     row_salesOrder = cursor.fetchone()
     print(row_salesOrder[0])
     print("Start paring:")
     print(salesOrderNumber)

     assert row_salesOrder[0] == salesOrderNumber, 'значения Sales Order не равны'
     print("Paired success")

test_check_new_salesOrderNumber()

#Check for TimeHistory table:

@allure.feature('Check ETL function')
@allure.story('Check FluidDescription')
@allure.step
def test_check_new_fluidDescription():
    time.sleep(10)
    cursor.execute(
        "select FluidDescription from TreatmentSummaryTimeHistory where TreatmentSummaryId = '91157A9B-E828-4094-96BA-84CCC917755A'")
    row_fluidDescription = cursor.fetchone()
    print(row_fluidDescription[0])
    print("Start paring:")
    print(fluidDescription)

    assert row_fluidDescription[0] == fluidDescription, 'значения Fluid Description не равны'
    print("Paired success")

test_check_new_fluidDescription()