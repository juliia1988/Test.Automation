import requests
import allure
import json
from STAGE_test_PJR.stage_settings_db_vs_azure import cursor

cursor.execute("select numAPI, TreatmentNumber, Operator from [dbo].WellSummary "
               "INNER JOIN TreatmentSummary on TreatmentSummary.WellSummaryId = WellSummary.WellSummaryId "
               "INNER JOIN stimJobInterval on stimJobInterval.TreatmentSummaryId = TreatmentSummary.TreatmentSummaryId "
               "where PercentProppantPumped IS NOT NULL "
               "order by NEWID()")
row = cursor.fetchone()
new_numAPI = row[0]
new_interval = row[1]
new_operator = row[2]
print(new_numAPI, new_interval, new_operator)

url = 'https://fvpostjobreportdev.azurewebsites.net/api/generatepjr'
email = 'yuliia.sokolova3@halliburton.com'
headers = {'content-type': 'application/json', 'x-functions-key': "9w4dlObARP3S3NIs7lB/aTpZzxzopHR49kqyLAJEzzlc5Y47v6OlAw=="}
data = {"numAPI": [new_numAPI], "Intervals": [str(new_interval)],
        "email": email, "operator": [new_operator]}


@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with valid parameters')
@allure.step
def test_generatepgr_api():

    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 200
    print(response.content)

test_generatepgr_api()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request without auth token')
@allure.step
def test_generatepgr_auth():
    headers = {'content-type': 'application/json',
               'x-functions-key': ""}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 401
    print(response.content)

test_generatepgr_auth()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with empty numAPI object parameter')
@allure.step

def test_generatepgr_empty_numAPI():

    data = {"Intervals": [str(new_interval)],
            "email": email, "operator": [new_operator]}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'invalid request parametes'

test_generatepgr_empty_numAPI()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with invalid numAPI object parameter')
@allure.step

def test_generatepgr_invalid_numAPI():

    data = {"numAPI": ["05-123-4815"], "Intervals": [str(new_interval)],
            "email": email, "operator": [new_operator]}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)

test_generatepgr_invalid_numAPI()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with empty Intervals object parameter')
@allure.step

def test_generatepgr_empty_intervals():

    data = {"numAPI": [new_numAPI], "email": email, "operator": [new_operator]}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'invalid request parametes'

test_generatepgr_empty_intervals()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with invalid operator')
@allure.step

def test_generatepgr_invalid_operator():
    data = {"numAPI": [new_numAPI], "Intervals": [str(new_interval)],
            "email": email, "operator": "Anadarko Pe"}

    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'Error in generating PJR request...Invalid Operator, please check operator name in the request file'

test_generatepgr_invalid_operator()

@allure.feature('Send request to the PJR Genarate API')
@allure.story('Send request with multiple Intervals')
@allure.step

def test_generatepgr_multipleIntervals():
    data = {"numAPI": [new_numAPI], "Intervals": ["1-"+str(new_interval)],
            "email": email, "operator": [new_operator]}

    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    assert response.status_code == 200
    print(response.content)
    print(data)

test_generatepgr_multipleIntervals()