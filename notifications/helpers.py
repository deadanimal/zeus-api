import requests
import json

HEADER =  { 'Content-Type': 'application/json; charset=utf-8' }
PAYLOAD = { 'app_id' : config('ONE_SIGNAL_APP_ID'}



def send_message_to_all(message):
    payload = PAYLOAD
    payload['included_segments'] = ['All']
    payload['contents'] = {'en': message }}
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=HEADER, data=json.dumps(payload))
    print(req.status_code, req.reason)


def send_message_to_specific(client_list, message):
    payload = PAYLOAD
    payload['include_player_ids'] = client_list
    payload['contents'] = {'en': message }}
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=HEADER, data=json.dumps(payload))
    print(req.status_code, req.reason)
