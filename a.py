import requests

url1 = "https://auth.dhanuat.co/partner/generate-consent" #uat


header = {
    "partner_id": "4c506ecb",
    "partner_secret": "f91a17bc-4520-46f9-b223-43da8b55202a"
}


response=requests.get(url1, headers=header,data={})
 
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())


consentID=response.json()
consentID=consentID['consentId']
print("cid",consentID)



url2=f"https://auth.dhanuat.co/consent-login?consentId={consentID}"

print("Redirect user to this url",url2)

