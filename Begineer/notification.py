from plyer import notification

# a simple notification
title = 'Hello Amazing people!'
message = 'Thankyou for reading! Take care!'
notification.notify(title=title,
                    message=message,
                    app_icon="Paomedia-Small-N-Flat-Bell.ico",
                    timeout=5,  # notification shows only 5 sec
                    toast=False)


# covid data notification
import datetime  # for reading present date
import time
import requests  # for retreiving coronavirus data from web
from plyer import notification  # for getting notification on your PC

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
    # print(covidData.content)

except:
    # if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

# if we fetched data
if covidData != None:
    # converting data into JSON format
    data = covidData.json()['Success']
    print(data)

    # repeating the loop for multiple times
    while True:
        notification.notify(
            # title of the notification,
            title="COVID19 Stats on {}".format(datetime.date.today()),
            # the body of the notification
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal "
                    "active :{active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data['todayDeaths'],
                active=data["active"]),
            # creating icon for the notification
            # we need to download a icon of ico file format
            app_icon="Paomedia-Small-N-Flat-Bell.ico",
            # the notification stays for 50sec
            timeout=5
        )
        # sleep for 4 hrs => 60*60*4 sec
        # notification repeats after every 4hrs
        time.sleep(60 * 60 * 4)  # if u remove it will show for every second


""" 
# a another notification
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10
        )
        time.sleep(3600)
"""

