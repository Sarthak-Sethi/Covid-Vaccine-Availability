import requests
from datetime import date
import json
import urllib
from twilio.rest import Client
from win10toast import ToastNotifier
today = date.today()
todays_date = today.strftime("%d-%m-%Y")
args = {"date": todays_date}
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=143001&date={}".format(urllib.parse.urlencode(args))
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url,headers = headers)
data_in_json = response.json()
for i in range(len(data_in_json["sessions"])) :
    second_dose_count = data_in_json["sessions"][i]["available_capacity_dose2"]
    vaccine = data_in_json["sessions"][i]["vaccine"]
    min_age_limit = data_in_json["sessions"][i]["min_age_limit"]
    n.show_toast("COVID VACCINATIION", "Script Running", duration = 10)
    if(vaccine=="COVISHIELD" and second_dose_count!=0 and min_age_limit == 45) :
        name = data_in_json["sessions"][i]["name"]
        address = data_in_json["sessions"][i]["address"]
        fees = data_in_json["sessions"][i]["fee_type"]
        message_data = "Name of covid vaccination center "+name+" Address of covid vaccination center "+address+" FEES"+fees
        n = ToastNotifier()
        n.show_toast("COVID VACCINATIION", message_data, duration = 10)
        