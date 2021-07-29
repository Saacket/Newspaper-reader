import requests
import json

def speak(str):
 from win32com.client import Dispatch
 speak = Dispatch("SAPI.SpVoice")
 speak.Speak(str)

if __name__ == '__main__':
    speak ("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=205b68bcdfd94ab38d11a4440dc24b8f"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving in to the next news .. Listen Carefully")
        speak ("Thanks for Listening...")