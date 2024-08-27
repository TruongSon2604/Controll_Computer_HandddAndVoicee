import datetime
import re
import webbrowser
import requests
from youtubesearchpython import VideosSearch
from comtypes import CLSCTX_ALL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import Basic
file_path = 'Resource/dict_website.json'
def addJson(name,url):
    new_data = {name:url}
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
    data.update(new_data)
    with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

#mở website
def open_website(text):
    with open('Resource/dict_website.json', encoding='utf-8') as file:
        data = json.load(file)
    if text in data:
        query = data[text]
        url = query[0]
        webbrowser.open(url)
# mở nhạc youtube
def play_Video(text):
    mysong = text
    while True:
        result = VideosSearch(mysong, limit=1).result()
        if result['result']:
            break
    video_url = 'https://www.youtube.com/watch?v=' + result['result'][0]['id']
    webbrowser.open(video_url)

# mở nhạc zingmp3
def play_song_mp3(song_name):
    search_url = "https://zingmp3.vn/tim-kiem/tat-ca?q={}".format(song_name.replace(" ", "+"))
    webbrowser.open(search_url)

# tìm kiếm trên google
def googleSearch(text):
    search_url = f"https://www.google.com/search?q={text}"
    webbrowser.open(search_url)

# lấy thông tin từ trang dự báo thời tiết
def current_weather(text):
    text = text.strip()
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = text
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """ Thời tiết tại {address} hôm nay:
             Nhiệt độ trung bình: {temp} độ C
             Áp suất không khí: {pressure} héc tơ Pascal
             Độ ẩm: {humidity}%
             Tình trạng: {weather_description}
             Mặt trời mọc vào {sunrise_time} và lặn vào {sunset_time}.
             Hiện tại là {current_time},
            Bạn nhớ chọn quần áo phù hợp khi ra đường
            """.format(address=city, temp=current_temperature, pressure=current_pressure, humidity=current_humidity, weather_description=weather_description, sunrise_time=sunrise.strftime("%H:%M"), sunset_time=sunset.strftime("%H:%M"), current_time=now.strftime("%H:%M, %d/%m/%Y"))
        print('OK')
        Basic.speak(text=content)
    
def send_email(title,text, email_receive):
    email_send = 'nhataaghjkl@gmail.com'
    password = 'llur licc ffkl zaix'
    email_to = email_receive
    message = MIMEMultipart()
    message['From'] = email_send
    message['To'] = email_to
    message['Subject'] = title
    content = MIMEText(text, 'plain', 'utf-8')
    message.attach(content)
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(email_send, password)
        session.sendmail(email_send, email_to, message.as_string())
