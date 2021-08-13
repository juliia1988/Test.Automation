import requests
import allure
headers = {'content-type': 'application/json'}
url = 'https://fracvaultnodeapis.azurewebsites.net/api/JobSummaryAPI'
params = {'code': 'VRAT1FU8XcS3s7psAIW2ucXW4w6T2LD8aKIlsOy/P646ia0pkQek8Q==', 'numAPI': ["05-123-49763-00"]}


@allure.feature('Send request to the JobSummary')
@allure.story('Send request with valid parameters')
@allure.step
def test_JobSummaryAPI_with_valid_parameters(headers=headers,url=url,params=params):

    response = requests.post(url, params=params, headers=headers)

    assert response.status_code == 200
    print(response.content)
test_JobSummaryAPI_with_valid_parameters()

@allure.feature('Send request to the JobSummary')
@allure.story('Send request with invalid numAPI parameter')
@allure.step
def test_JobSummaryAPI_with_invalid_numAPI_parameters(headers=headers,url=url):

     params = {'code': 'VRAT1FU8XcS3s7psAIW2ucXW4w6T2LD8aKIlsOy/P646ia0pkQek8Q=='}
     response = requests.post(url, params=params, headers=headers)

     assert response.status_code == 400
     print(response.content)

     assert response.content == b'invalid request parameters'
test_JobSummaryAPI_with_invalid_numAPI_parameters()

@allure.feature('Send request to the JobSummary')
@allure.story('Send request with invalid code parameter')
@allure.step
def test_JobSummaryAPI_with_invalid_code_parameters(headers=headers,url=url):

    params = {'code': 'VRAT1FU8XcS3s7psAIW2ucXW4w6T2LD8aKIlsOy/P646ia0pkQek8', 'numAPI': ["05-123-49763-00"]}
    response = requests.post(url, params=params, headers=headers)

    assert response.status_code == 401
    print(response.content)
test_JobSummaryAPI_with_invalid_numAPI_parameters()