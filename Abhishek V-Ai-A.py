from http import client
import requests
from pydoc import text
from random import choice
from IPython.display import Video, YouTubeVideo
from bs4 import BeautifulSoup
import pyttsx3
import requests
import wikipedia
import webbrowser
import wolframalpha
from datetime import datetime
import os
import speech_recognition as sr
import smtplib
import subprocess
from playsound import playsound
import pywhatkit as kit
import google.generativeai as genai
import nltk
from nltk.chat.util import Chat, reflections
import pywhatkit as kit
from bs4 import BeautifulSoup
import keyboard 


"""now = datetime.datetime().now()
hour = now.hour
minute = now.minute
second = now.second
abhi = "+91 911129xxxx"
def send_msg(text):
   speak("who do you want to send sir ")
   output_text =""
   while True:
      with open ("input.txt" ,"r") as file:
         input_text = file.read().lower()
      if input_text != output_text:
         output_text = input_text
         output_text.replace("send to", "")
         if "abhi" in output_text:
          kit.sendwhatmsg("" , "system geneterd message please ingone it!" , hour ,minute + 1)

"""



GOOGLE_API_KEY ='AIzaSyBUI3dTUgBCj0ka4OO95wPy1gyZf3z-oiuy'
genai.configure(api_key = GOOGLE_API_KEY)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)
chat_session = model.start_chat()


engine = pyttsx3.init()
voices=engine.getProperty('voices')
print("         Sir         ")
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

random = ["cool ,i'm on it sir","okay sir ,i'm working on it","just a second"]

def search(queary):
   kit.search(queary)

def youtube(video):
   kit.playonyt(video)

def music(audio):
   kit.playsound(audio)



def  get_news():
   news_headline =[]
   result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey"f"=04088e27f18b40a3a39103a8644e149d").json()
   articles = result["articles"]
   for article in articles:
      news_headline.append(article["title"])
      return news_headline[:26]

"""def Gemini(query):
   GOOGLE_API_KEY ='AIzaSyBUI3dTUgBCj0ka4OO95wPy1gyZf3-oiuy'
   genai.configure(api_key = GOOGLE_API_KEY)
   text = f"gemini response for prompt : {query} \n "
response = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
#print(response["choices"][0]["text"])
text+=response["choices"][0]["text"]
if not os.path.exists("gemini ai"):
   os.mkdir("gemini ai ")

   with open (f"prompt - {random(1 ,24585113)}","w")as f :
      f.write(text)
   
"""
def WolfRamApha(query):
   apikey = "L55GLX-2U6XLzeds"
   requester = wolframalpha.Client(apikey)
   requested = requester.query(query)

   try:
      answer = next(requested.results).text
      return answer
   except :
      speak("the value is not answerable")


def Calc(query):
   Term = str(query)
   Term = Term.replace("zira" ,"")
   Term = Term.replace("multiply" ,"*")
   Term = Term.replace("plus" ,"+")
   Term = Term.replace("minus" ,"-")
   Term = Term.replace("divide" ,"/")
   

   Final = str(Term)
   try:
      result = WolfRamApha(Final)
      print(f"{result}")
      speak(result)
   except:
      speak("the value is not anwerable")  








def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('emailid','Password')
    server.sendmail('xyz@gmail.com',to ,content)
    server.close()

def wishMe():
    hour = datetime.now().hour
    if hour>=0 and hour<12:
       speak("Good Morning Mister Singh !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mister Singh!") 

    else:
        speak("Good Evening Mister Singh !")

    speak("I am Zira !. tell me how may i help you")

listening = False

def start_listening():
   global listening
   listening = True
   print(" started listening")

def pause_listening():
   global listening
   listening = False
   print(" stopped listening")


keyboard.add_hotkey('ctrl+alt+k' , start_listening)
keyboard.add_hotkey('ctrl+alt+p' , pause_listening)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1.5
        audio = r.listen(source)

    try:
        print("Recognzing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"user said:-{query}\n")

        if not 'stop' in query or 'exit' in query:
           speak(choice(random))
        else:
           hour = datetime.now().hour
           if hour >= 21 and hour <6:
              speak("good night mister singh!")
           else:
              speak("have a good day")
              exit()
            
    except Exception as e:
        print(e)
        speak("Sorry Say that again please!")
        #print("Sorry Say that again please!")
        return "none"
    return query


if __name__ =="__main__":
    wishMe()
    while True :
        query = takecommand().lower()


        sites = [["whatsapp","https://whatsapp.com"],["youtube","https://youtube.com"],["google","https://google.com"],["wikipedia","https://wikipedia.com"],["stack overflow","https://stackoverflow.com"],["instagram","https://instagram.com"],["facebook","https://facebook.com"],["amazon","https://amazon.com"],["linkedin","https://linkedin.com"],["flipkart","https://flipkart.com"]]
        for site in sites:
           if f"open{site[0]}" in query:
              speak(f"opening {site[0]}")
              webbrowser.open(site[1])

        sites = [["whatsapp","whatsapp.com"],["youtube","https://youtube.com"],["google","https://google.com"],["wikipedia","https://wikipedia.com"],["stack overflow","https://stackoverflow.com"],["instagram","https://instagram.com"],["facebook","https://facebook.com"],["amazon","https://amazon.com"],["linkedin","https://linkedin.com"],["flipkart","https://flipkart.com"]]
        for site in sites:
           if f"close{site[0]}" in query:
              speak(f"closed{site[0]}")
              webbrowser.close(site[1])

        if 'wikipedia' in query :
          speak('searching wikipedia and Google...') 
          query = query.replace("wikipedia", " ")
          results = wikipedia.summary(query,sentences =2)
          speak("accoding to wikipedia") 
          print(results)
          speak(results)
         
        
           
        elif "open command prompt" in query:
           speak("opening command prompt")
           os.system('start cmd')


        elif "calculate" in query:
           app_id = "L55GLX-2U6XLYzeds"
           client = wolframalpha.Client(app_id)
           ind = query.split().index("calculate")
           text = query.split()[ind + 1:]
           result = client.query(" ".join(text))
           try:
              ans = next(result.results).text
              speak( "the answer is " + ans)
              print( "the answer is " + ans)
           except StopIteration:
            speak("i couldn't find that please try again")

        elif "what is" in query or "who is" in query or "which is" in query or "application" in query or "program" in query:
           app_id = "L55GLX-2U6XLYzeds"
           client = wolframalpha.Client(app_id)
           try:
              ind = query.index('what is ') if 'what is ' in query else \
              query.index('who is') if 'who is ' in query else \
              query.index('which is') if 'which is' in query else \
              query.index('application') if 'application' in query else \
              query.index('program') if 'program' in query else None
            
              if ind is not None:
                 text = query.split()[ind + 2:]
                 result = client.query(" ".join(text))
                 ans = next(result.results).text
                 speak( "the answer is " + ans)
                 print( "the answer is " + ans)
              else:
               speak (" i could not find that")
                 
           except StopIteration:
            speak("i couldn't find that please try again")
           



        elif 'open youtube' in query: #working
          speak("what do you want to play on youtube")
          video = takecommand().lower()
          youtube(video)

        elif 'open google' in query: #working
          speak("what do you want to search on google")
          query = takecommand().lower()
          search(query)


        elif 'hii zira' in query: #working
          speak("what do you want mister singh")
          query = takecommand().lower()
          search(query)

        elif 'check weather' in query: #working
          speak(" which place")
          query = takecommand().lower()
          search(query)
          

          """serach = " weather in bhopal"
          url =f"https://www.google.com/search?q={search}"
          r = requests.get(url)
          data = BeautifulSoup(r.text,"Html.parser")
          temp = data.find("div",class_="BNeawe")
          speak(f"current{serach} is {temp}")"""

        

        elif 'give me suggestion' in query: #working
          speak("what do you want ")
          query = takecommand().lower()
          search(query)

        elif 'open application' in query: #working
          speak("what do you want ")
          query = takecommand().lower()
          search(query)

        elif 'give me news' in query: 
          webbrowser.open("https://www.bbc.com/news")
          print("Here some headline from the newspaper from bbc news")
          speak("Here some headline from the newspaper from bbc news")
          """speak("what do you want ")
          query = takecommand().lower()
          search(query)"""
          """speak(" i am reading out the latest headline of todat , sir ")
          speak(get_news())
          speak(" i am printing it on screen sir")
          print(get_news(),sep="\n")"""

       
        elif 'open stack overflow' in query: #working
          webbrowser.open("https://stackoverflow.com")
          speak("opening stack overflow abhi ")
      
        elif 'the time' in query: #working
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"the time is {strTime}")

        elif 'play music' in query :
           music_path = "C:\\Users\\HP\\Videos\\Downloads\\dir_music\\Soch Na Sake(PagalWorld).mp3"
           os.startfile(music_path)
           
        
        elif 'open code' in query: #working
          codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

        elif 'shutDown PC' in query:
           os.system("shutdown -/s -/t 1") #os.system

        elif 'refresh device' in query:
           refreshPath = "C:\\Users\\HP\\Videos\\important files\\Data"
           subprocess.call(refreshPath)

        elif 'restart PC' in query:
           os.system("shutdown -/r -/t 1")

        elif 'open instagram' in query: #working
           webbrowser.open("https://instagram.com")
           speak("opening instagram abhi ")

        elif 'open Facebook' in query:
           webbrowser.open("https://facebook.com")
           speak("opening Facebook abhi ")

        elif 'open chrome' in query:
           chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(chromePath)

        elif 'open Pc manager' in query:
           managerPath = "C:\\Program Files\\Microsoft PC Manager\\MSPCManager.exe"
           os.startfile(managerPath) 

        elif 'open excel' in query:
           excelPath = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE"
           os.startfile(excelPath)

        elif 'open word' in query:
           wordPath ="C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"
           os.startfile(wordPath)

        elif 'open powerpoint' in query:
           pptPath ="C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE"
           os.startfile(pptPath)

        elif 'open mysql' in query: #working
           sqlPath ="C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
           os.startfile(sqlPath)

        elif 'open task manager' in query:
           taskPath ="%windir%\\system32\\taskmgr.exe //7"

        elif 'open microsoft edge' in query: #working
           edgePath ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
           os.startfile(edgePath)

        elif 'open linkedin' in query:
           webbrowser.open("https://linkedin.com")
           speak("opening linkedin abhi ")

        elif 'open amazon' in query: #working
           webbrowser.open("https://amazon.com")
           speak("opening amazon abhi ")

        elif 'open Flipkart' in query:
           webbrowser.open("https://flipkart.com")
           speak("opening Flipkart abhi ")

       

        elif 'email to {user}' in query: 
         try:
               speak("What should I say?")
               content = takecommand()
               to = "xyz@gmail.com"
               sendEmail(to, content)
               speak("Email has been send successfully !")
         except Exception as e:
               print(e)
               speak("sorry {user} . I am not able to send this email")

        
               