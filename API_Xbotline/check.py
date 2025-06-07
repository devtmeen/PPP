import requests
import os
import time

def notifyNetwork(message):
    token = "B8jjc50224xy5yWGZRVDkOkPkcmRzVnWcRnuCNJZWFW"
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    msg = {"message": message}
    resp = requests.post(uri, headers=header, data=msg)


hostname = list([['141.11.33.184', True], ['141.11.33.189', True], ['141.11.33.234', True]])


def checkNetwork(hostname):
    response = os.popen("ping "+hostname).read()
    if (("unreachable") or ("Request time out")) in response:
        status = False
    else:
        status = True
    return status


while True:
    for index, roitai in enumerate(hostname):
        currentStatus = checkNetwork(roitai[0])
        previusStatus = roitai[1]
        if currentStatus == previusStatus:
            print('-----no notify--------')
        else:
            hostname[index][1] = currentStatus
            if currentStatus:
                statusNetwork = 'UP'
            else:
                statusNetwork = 'DOWN'
            message = f"{hostname[index][0]} {statusNetwork}"
            notifyNetwork(message)
            print('--- Notify ----')
        time.sleep(60)
    print(hostname)