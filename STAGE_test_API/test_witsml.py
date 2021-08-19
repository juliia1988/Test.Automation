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

url = 'https://netwitsmlgenerationapitest.azurewebsites.net/api/GenerateWitsml'
email = 'yuliia.sokolova3@halliburton.com'
code = 'N8HkjnysYknhYiqlN51239'
headers = {'content-type': 'application/json'}
data = {"numAPI": [new_numAPI], "Intervals": [str(new_interval)],
        "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
params = {'code': code}

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with valid parameters')
@allure.step
def test_witsml_api():

    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 200
    print(response.content)

test_witsml_api()

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with ExcludeElements parameters')
@allure.step
def test_witsml_api_excludeElements():
    data = {"numAPI": [new_numAPI], "Intervals": [str(new_interval)],
            "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"],
            "ExcludeElements": [["/pds:stimJobs/pds:stimJob/pds:jobInterval/pds:totalProppantUsage","/pds:stimJobs/pds:stimJob/pds:jobInterval/pds:flowPath/pds:tubular"]]}
    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 200
    print(response.content)

test_witsml_api_excludeElements()

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with empty numAPI object parameter')
@allure.step

def test_witsml_api_empty_numAPI():

    data = {"Intervals": [str(new_interval)],
            "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'Request should contain exactly 1 NumAPI'

test_witsml_api_empty_numAPI()

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with invalid numAPI object parameter')
@allure.step

def test_witsml_api_invalid_numAPI():

    data = {"numAPI": ["05-123-4815"], "Intervals": [str(new_interval)],
            "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'Invalid NumApi = 05-123-4815. Allowed formats: SS-CCC-NNNNN or SS-CCC-NNNNN-BB or SS-CCC-NNNNN-BB-BB\nwhere SS - state code, CCC - county code, NNNNN - well number, BB - bore number'

test_witsml_api_invalid_numAPI()

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with empty Intervals object parameter')
@allure.step

def test_witsml_api_empty_intervals():

    data = {"numAPI": [new_numAPI], "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 400
    print(response.content)
    assert response.content == b'Request should contain exactly 1 interval'

test_witsml_api_empty_intervals()

@allure.feature('Send request to the WITSML API')
@allure.story('Send request with invalid code params')
@allure.step

def test_witsml_api_invalid_code():

    params = {'code': 'N8HkjnysYknhYiqlN512'}

    response = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))

    assert response.status_code == 401
    print(response.content)

test_witsml_api_invalid_code()