import requests
import allure
import json
from stage_settings_db import cursor

cursor.execute("select numAPI, TreatmentNumber, Operator from [dbo].WellSummary INNER JOIN TreatmentSummary on TreatmentSummary.WellSummaryId = WellSummary.WellSummaryId order by NEWID()")
row = cursor.fetchone()
new_numAPI = row[0]
new_interval = row[1]
new_operator = row[2]
print(new_numAPI,new_interval,new_operator)

url = 'https://netwitsmlgenerationapitest.azurewebsites.net/api/GenerateWitsmlAndSendEmail'
email = "yuliia.sokolova3@halliburton.com"
code = 'N8HkjnyNYkn%$hYiHn%23@N51239'
headers = {'content-type': 'application/json'}
data = {"numAPI": [new_numAPI], "Intervals": [str(new_interval)], "email": email, "operator": [new_operator], "WITSMLObjects": ["ALL"], "ExcludeElements": [[""]]}
params = {'code': code}


@allure.feature('Send request to the WITSML send Email API')
@allure.story('Send request with valid parameters')
@allure.step
def test_witsml_send_email_with_valid_parameters(headers=headers,url=url,params=params,data=data):

    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)
    print(data)

    assert response.status_code == 200
    print(response.content)


test_witsml_send_email_with_valid_parameters()



