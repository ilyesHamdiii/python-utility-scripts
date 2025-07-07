# i used text belt API for sms sending
import requests
import schedule
import time 
def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '19702584068', #provide the number
    'message': 'wakey wakey time to school',
    'key': 'textbelt',
    })
    print(resp.json())
    
schedule.every().day.at("06:00").do(send_message) 


############ greet for every s seconds
def greet():
    print("hello")
schedule.every(5).seconds.do(greet)
while True:
    schedule.run_pending()
    time.sleep(1)
