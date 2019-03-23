import requests
import secret

api_key = secret.companieshouse

companies = requests.get('https://api.companieshouse.gov.uk/search/companies', headers = {
'Content-Type':'application/json',
'Authorization': api_key
})

print(companies)
