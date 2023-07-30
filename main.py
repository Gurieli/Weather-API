import requests
import smtplib

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_API = api
MY_API2 = api2
SALOME_MAIL = 'pkhakadze.salome7@gmail.com'

parametres = {
    "lat": 48.856613,
    "lon": 2.352222,
    "appid": MY_API
}

response = requests.get(ENDPOINT, params=parametres)
response.raise_for_status()
data = response.json()
hour_data = data["list"]


weather = []
start_end = []

# loop through the hour_data list
for i in range(12):
    temp_id = (hour_data[i]['weather'][0]['id'])
    if 200 <= temp_id <= 232:
        start_end.append(i)
        weather.append("thunderstorm")
    elif 300 <= temp_id <= 321:
        start_end.append(i)
        weather.append("drizzle")
    elif 500 <= temp_id <= 531:
        start_end.append(i)
        weather.append("rain")
    else:
        pass

if 'thunderstorm' in weather:
    if start_end[0] == 0:
        main_text = f"Gogo cheqaquxils iwyebs axa da gacherdeba {start_end[len(start_end)-1]} saatshi" \
                    f"xoda argaxvide garet <3"
    else:
        main_text = f"Gogo cheqaquxils daiwyebs {start_end[0]} saatshi da gadaigebs {start_end[len(start_end)-1]}" \
                    f" saatshi " \
                    f"xoda argaxvide garet <3"
elif 'rain' in weather:
    if start_end[0] == 0:
        main_text = f"Gogo iwvimebs axa da gacherdeba {start_end[len(start_end)-1]} saatshi da waige qolga <3"
    else:
        main_text = f"Gogo wvimas daiwyebs {start_end[0]} saatshi da gadaigebs {start_end[len(start_end)-1]} saatshi " \
                    f"xoda waige qolga <3"
elif "drizzle" in weather:
    if start_end[0] == 0:
        main_text = f"Gogo winwklavs axa da gacherdeba {start_end[len(start_end)-1]} saatshi da waige qolga <3"
    else:
        main_text = f"Gogo wamowinwklavs :D {start_end[0]} saatshi da gadaigebs {start_end[len(start_end)-1]} " \
                    f"saatshi " \
                    f"" \
                    f"xoda waige qolga <3"
else:
    main_text = "Gogo shemdegi 12 saati kai amindi giweria da wadi sacagindodes <3"

my_email = "guropkhakadze01@Gmail.com"
my_pass = 'xxnqxhabyevifbnx'


connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_pass)
connection.sendmail(from_addr=my_email, to_addrs='pkhakadzguro88@gmail.com',
                    msg=f"Subject:Amindis Prognozi Sheni Dzmisgan\n\n{main_text}")
