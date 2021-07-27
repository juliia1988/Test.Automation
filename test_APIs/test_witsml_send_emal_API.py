import requests
import json
import allure
headers = {'content-type': 'application/json'}
url = 'https://witsmlapitrigger.azurewebsites.net/api/GenerateWitsmlAndSendEmail'
data = {"numAPI": ["05-001-09880-00"], "Intervals": ["9"], "email": "yuliia.sokolova3@halliburton.com", "operator": ["Great Western"], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
params = {'code': 'c4QwXXPhK/AzgTjpyal8DUZ/P9qtIEbLzXQtTKOXrNmxl/POmiuwkA=='}


@allure.feature('Send request to the WITSML send Email API')
@allure.story('Send request with valid parameters')
@allure.step
def test_witsml_send_email_with_valid_parameters(headers=headers,url=url,data=data,params=params):

    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    print(response.content)

test_witsml_send_email_with_valid_parameters()

@allure.feature('Send request to the WITSML send Email API')
@allure.story('Send request with Exclude elements parameters')
@allure.step
def test_witsml_send_email_with_ExcludeElements_parameters(headers=headers,url=url):

    data = {"numAPI": ["05-001-09880-00"], "Intervals": ["1"], "email": "yuliia.sokolova3@halliburton.com",
                "operator": ["Great Western"], "WITSMLObjects": ["ALL"],
                "ExcludeElements": [["/pds:stimJobs/pds:stimJob/pds:jobInterval/pds:totalProppantUsage","/pds:stimJobs/pds:stimJob/pds:jobInterval/pds:flowPath/pds:tubular"]]}
    params = {'code': 'c4QwXXPhK/AzgTjpyal8DUZ/P9qtIEbLzXQtTKOXrNmxl/POmiuwkA=='}

    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    print(response.content)
test_witsml_send_email_with_ExcludeElements_parameters()

@allure.feature('Send request to the WITSML send Email API')
@allure.story('Send request with empty WITSML object parameter')
@allure.step
def test_witsml_send_email_with_emptyWITSMLObjects_parameter(headers=headers,url=url):

    data = {"numAPI": ["05-001-09880-00"], "Intervals": ["9"], "email": "yuliia.sokolova3@halliburton.com", "operator": ["Great Western"], "ExcludeElements": [[""]]}
    params = {'code': 'c4QwXXPhK/AzgTjpyal8DUZ/P9qtIEbLzXQtTKOXrNmxl/POmiuwkA=='}

    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)

    assert response.status_code == 400
    print(response.content)

    assert response.content == b'WITSMLObjects must not be empty. '
test_witsml_send_email_with_emptyWITSMLObjects_parameter()

@allure.feature('Send request to the WITSML send Email API')
@allure.story('Send request without numAPI parameters')
@allure.step
def test_witsml_send_email_without_numAPI_parameter(headers=headers,url=url):

    data = {"Intervals": ["9"], "email": "yuliia.sokolova3@halliburton.com", "operator": ["Great Western"], "ExcludeElements": [[""]]}
    params = {'code': 'c4QwXXPhK/AzgTjpyal8DUZ/P9qtIEbLzXQtTKOXrNmxl/POmiuwkA=='}

    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)

    assert response.status_code == 400
    print(response.content)

    assert response.content == b'Request should contain exactly 1 NumAPIWITSMLObjects must not be empty. '

test_witsml_send_email_without_numAPI_parameter()