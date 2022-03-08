from tkinter import *
import os
import speech_recognition as sr
def jessica():
    screen.destroy()
    screen6.destroy()
    import pyttsx3
    import datetime
    import wikipedia
    import webbrowser
    import os
    import random
    import wolframalpha
    import requests
    try:
        client=wolframalpha.Client('TTRGT4-28G42RHYUG')
        query2="wheater forecast of kolkata,india"
        res = client.query(query2)
        output=next(res.results).text
    except Exception as e:
        print("")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.7)
    a = 6
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        su="-->>"+str(audio)
        return su
    def speak1(audio):
        engine.say(audio)
        engine.runAndWait()
    file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3,"r")
    verify1=file1.read().splitlines()
    if "male" in verify1:
        gender2="male"
    else:
        gender2="female"
    gender=gender2.lower()
    if gender=='male': 
        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("good morning sir")
            elif hour>=12 and hour<16:
                speak("good afternoon sir")
            else:
                speak("good evening sir")
            speak("I am jessica ")
            engine.setProperty('rate',130)
            speak("")
            engine.setProperty('rate',170)
            try:
                speak("the temperature of the day will be "+output)
            except Exception as e:
                speak("")
            speak("Tell me how can i help you today")

                

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        wishme()
        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=0.6
                r.energy_threshold=250
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "


            
        while a==6:
            query=takecommand()
            if 'wikipedia' in query:
                speak("searching wikipedia for you")
                speak("please wait")
                query = query.replace("wikipedia","")
                engine.setProperty("rate",180)
                results = wikipedia.summary(query,sentences=5)
                if results == None:
                    speak("sorry sir you are not connected to the internet")
                    speak("can't get any results")
                else:
                    speak("according to wikipedia")
                    speak(results)
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "play music" in query:
                music_dir='C:\music'
                awer=random.randint(0,1)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak1(i+1) 
                        print(results[i])
                        speak1(results[i])  
                NewsFromBBC()



            elif "visual studio code" in query:
                codepth = "C:\\Users\\my computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepth)
            elif "play movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "geeta govinda" in o:
                    music_dir='D:\\Geeta Govinda 2018 Hindi 1080p WEB-DL AVC AAC - MoviePirate - Telly'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "avatar" in o:
                    music_dir='D:\HOLLYWOOD\Avatar (2009) BRRip 1080p[Dual audio][Eng Hindi]Current_HD'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))  
                elif "blackhat" in o:
                    music_dir='D:\HOLLYWOOD\Blackhat (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "don john" in o:
                    music_dir='D:\HOLLYWOOD\Don John'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "gozilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "hacker" in o:
                    music_dir='D:\HOLLYWOOD\Hacker (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "i.t" in o:
                    music_dir='D:\HOLLYWOOD\I.T. (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "interstellar" in o:
                    music_dir='D:\HOLLYWOOD\Interstellar (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jumper" in o:
                    music_dir='D:\HOLLYWOOD\Jumper (2008) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "lucy" in o:
                    music_dir='D:\HOLLYWOOD\LUCY(2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "murder on the orient express" in o:
                    music_dir='D:\HOLLYWOOD\Murder On The Orient Express (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "parasite" in o:
                    music_dir="D:\HOLLYWOOD\Parasite (2019) [BluRay] [1080p] [YTS.LT]"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pet" in o:
                    music_dir='D:\HOLLYWOOD\Pet (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "schindlers list" in o:
                    music_dir='D:\HOLLYWOOD\Schindlers List (1993) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "snowden" in o:
                    music_dir='D:\HOLLYWOOD\Snowden (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "solo a star wars story" in o:
                    music_dir='D:\HOLLYWOOD\Solo A Star Wars Story (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the last jedi" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Last Jedi (2017) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the rise of skywalker" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Rise of Skywalker 2019 HDTS XViD-ETRG'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the lion king" in o:
                    music_dir='D:\HOLLYWOOD\The Lion King'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man from uncle" in o:
                    music_dir='D:\HOLLYWOOD\The Man From U.N.C.L.E. (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man who knew infinity" in o:
                    music_dir='D:\HOLLYWOOD\The Man Who Knew Infinity (2015) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shawshank redemption" in o:
                    music_dir='D:\HOLLYWOOD\The_Shawshank_Redemption_(1994)_[1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "bharat" in o:
                    music_dir='D:\Bollywood\Bharat_(2019)_Hindi_720p_HDRip_x264_AAC_5.1_ESubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "chhichhore" in o:
                    music_dir='D:\Bollywood\Chhichhore_(2019)_Hindi_720p_HDRip_x264_AAC_ESubs_-_Downloadhub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kabir singh" in o:
                    music_dir='D:\Bollywood\kabir singh'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kal ho naa ho" in o:
                    music_dir='D:\Bollywood\kal ho naa ho 2003 hindi brrip 720p x264 aac 5 1 hon3y'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "sahoo" in o:
                    music_dir='D:\Bollywood\sahoo'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shubh mangal zyada saavdhan" in o:
                    music_dir='D:\Bollywood\shubh mangal zyada savdhan'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "ujda chaman" in o:
                    music_dir="D:\\Bollywood\\ujda chaman"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "war" in o:
                    music_dir='D:\Bollywood\war'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pati patni aur woh" in o:
                    music_dir='D:\Bollywood\www.HDwebmovies.club - Pati Patni Aur Woh 2019 Hindi 720p AMZN WEB-DL DD-5.1 Esubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 2" in o:
                    music_dir='E:\SERIES\Cars\Cars 2 (2011) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 3" in o:
                    music_dir='E:\SERIES\Cars\Cars 3 (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars" in o:
                    music_dir='E:\SERIES\Cars\Cars_(2006)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "aquaman" in o:
                    music_dir='E:\SERIES\DC\Aquaman (2018) [BluRay] [720p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "joker" in o:
                    music_dir='E:\SERIES\DC\Joker (2019) [BluRay] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "wonder women" in o:
                    music_dir='E:\SERIES\DC\Wonder Woman (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and where to find them" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_And_Where_To_Find_Them_(2016)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and the crimes of grindlewald" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_The_Crimes_Of_Grindelwald_(2018)_[BluRay]_[1080p]_[YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades darker" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Darker (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades freed" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Freed (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades of grey" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades of Grey (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "harry potter" in o:
                    music_dir='E:\SERIES\Harry Potter Complete Collection 1080p BluRay x264 Dual Audio [Hindi - English] ESub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick (2014) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick chapter 2" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick Chapter 2 (2017) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jhon wick chapter 3" in o:
                    music_dir='E:\SERIES\JOHN WICK\John.Wick.Chapter.3.-.Parabellum.2019.1080p.WEBRip.x264-[YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry sir")
                    speak("there are no such movies in the directory")
                    speak("but sir if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif "download movie" in query:
                speak("type the name of the movie you want to download")
                a=input("::>>")
                s=""
                k=len(a)
                i=0
                while i<k:
                    if a[i]==" ":
                        s+="%20"
                    else:
                        s+=a[i]
                    i+=1
                d="https://www.1337x.am/search/"+s +"/1/"
                webbrowser.open(d)

            elif "download a movie" in query:
                speak("type the name of the movie you want to download")
                a=input("::>>")
                s=""
                k=len(a)
                i=0
                while i<k:
                    if a[i]==" ":
                        s+="%20"
                    else:
                        s+=a[i]
                    i+=1
                d="https://www.1337x.am/search/"+s +"/1/"
                webbrowser.open(d)

            elif " python idle" in query:
                codepath="C:\\Users\\my computer\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe" 
                os.startfile(codepath)
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day sir")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening sir")
                else:
                    speak("have sweet dreams sir")
                a=7
            elif "shut down yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day sir")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening sir")
                else:
                    speak("have sweet dreams sir")
                a=7

            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day sir")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening sir")
                else:
                    speak("have sweet dreams sir")
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif query=="hey jessica":
                speak("yes sir what can i do for you")
            elif query=="hi jessica":
                speak("hi sir what can i do for you")
            elif "open my website" in query:
                webbrowser.open("http://sonamaniforextourism.viamagus.com/")
            elif "need82" in query:
                webrowser.open("http://www.need82.com/")
            elif "via" in query:
                webbrowser.open("http://www.viaworld.in/")
            elif "travel boutique" in query:
                webbrowser.open("http://www.tbtq.in/")
            elif "jaldicash" in query:
                webbrowser.open("https://www.jaldicash.com/")
            elif "ebixcash" in query:
                webbrowser.open("https://www.ebixcash.com/")
            elif "itz" in query:
                webbrowser.open("https://www.itzcash.com/user/jsp/Login.jsp?ref=driverlayer.com/web")
            elif "transaction status" in query:
                webbrowser.open("https://wfl.ebixcash.com/syslogin.aspx")
            elif "paytm" in query:
                webbrowser.open("https://paytm.com")
            elif "novoair" in query:
                webbrowser.open("https://secure.flynovoair.com/agents  ")
            elif "royal coach" in query:
                webbrowser.open("www.royalcoach.co.in")
            elif "bangla airlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "banglaairlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "bsnl" in query:
                webbrowser.open("https://selfcare.bsnl.co.in ")
            elif "multilink" in query:
                webbrowser.open("http://www.multilinkworld.com")
            elif "rail ticket" in query:
                webbrowser.open("https://www.irctc.co.in")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "bank of boroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "xpressmoney" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "xpress money" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "tata aia" in query:
                webbrowser.open("https://myinsurance.tataaia.com/wps/portal/Customer/Customer/CustomerLoginPage/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zivS0szAyN_Q38DEJ9nQwcw9w9nUy8fIw8Qsz0w8EKDHAARwP9KGL041EQhd_4cP0ovFa4mEMV4DGjIDc0wiDTUREAzIYbyA!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/")
            elif "matrix" in query:
                webbrowser.open("https://tab.matrix.in/DSAOnlineCAF")
            elif "instagram" in query:
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif "who are you" in query:
                speak("i am jessica")
            elif "i want to say something" in query:
                speak("yes sir tell me")
                speak("i am listening")
                a01=input("Tell me:")
                a0=a01.lower()
                if "leave it" in a0:
                    speak("ok sir,i will not force you ,as i am a robot")
                    speak("but you can tell me, whatever you want ")
                elif "not feeling" in a0:
                    speak("what happened sir?")
                    speak("are you feeling low?")
                    a12=input("yes or no?:")
                    a1=a12.lower()
                    if "yes" in a1:
                        speak("i can motivate you")
                        speak("if i know your problem")
                        speak("you know sir,i have a self automated fellings understanding system ")
                        speak("that is, i can react to human behaviours")
                        speak("tell me sir")
                        a134=input("one more?:")
                        a13=a134.lower()
                        if "love" in a13:
                            speak("hear this clip sir,you will feel better")
                            music_dir='C:\motivation'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[0]))
                        elif "tired" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[11]))
                        elif "sad" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[9]))
                        
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry sir")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name im jessica")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse sir")
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are a male" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are you boy or man" in query :
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "search a file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("sir the location is on the screen")
                    
                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry sir")
                    speak("no results found")
            elif "search file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("sir the location is on the screen")

                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry sir")
                    speak("no results found")

            elif "show me your face" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i don't have handsome face like yours")
            elif "tired" in query:
                speak("here this song sir you will feel energetic")
                music_dir='D:\HOLLYWOOD\song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[11]))
            
            elif "hi" in query:
                speak("hi sir")
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="jessica":
                speak("yes sir..")
            elif "i am fine" in query:
                speak("you surely are, sir")
            elif "i am ok" in query:
                speak("i know sir")
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("sir,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "sad" in query:
                speak("sir,don't be sad")
                speak("always remember,the one who flies alone,have the strongest wings")
                speak("sir,are you still feeling low")
                a1q=input("one more?")
                if 'yes' in a1q:
                    speak("sir i was born few weeks ago,but sir as an self working AI,i learned an interesting fact about human behaviour")
                    speak("that is,there is no market for ones emotions,so never advertise your feelings,just show your attitude")
                    speak("take deep breath.And thank god for the life you have got ")
                    speak("all will be okay")
                    speak("because,tony robbins once said")
                    speak("it is just matter of time to heal up your scars,time is best medicine")
                    speak("and sir,the most powerful thing about time is,it changes")
                    speak("all dust will settle down,give yourself some time")
                    speak("and don't give up on life")
                    speak("you bulit me,and i need you,to change this world")
            elif "i love you" in query:
                speak("oh!thank you sir")
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse sir!I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome sir")
            elif "dont call me sir" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "who is the richest man in the world" in query:
                speak("according to wolform report of 20 19")
                speak("bill gates is the richeast man in the world")
            elif "who is the richest man in india" in query:
                speak("according to wolform report of 20 19")
                speak("mukesh ambani is the richeast man in the world")
            elif "sing a song" in query:
                speak("sorry sir i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry sir i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("sir!i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you sir")
            elif "tell me about you" in query:
                speak("i am jessica")
                speak(" i am an artificial intilligence")
                speak("i will you what you tell me to do")
                speak("sir i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what sir?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            elif "tell me about" in query:
                try:
                    query = query.replace("tell me about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                except Exception as e:
                    speak("sorry sir")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "tell me something about" in query:
                try:
                    query = query.replace("tell me something about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)   
                except Exception as e:
                    speak("sorry sir")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "i know" in query:
                speak("ok")
            elif 'what is' in query:
                query=query.replace("what is","")
                res = client.query(query)
                output = next(res.results).text
                speak(output)

            
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except Exception as e:
                    try:
                        results = wikipedia.summary(query,sentences=5)
                        speak("according to wikipedia")
                        speak(results)
                    except Exception as e:
                        print("Say that again please")
                        

    elif "female" in gender:
        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("good morning ma'am")
            elif hour>=12 and hour<16:
                speak("good afternoon ma'am")
            else:
                speak("good evening ma'am")
            speak("I am jessica ")
            engine.setProperty('rate',130)
            speak("")
            engine.setProperty('rate',170)
            try:
                speak("the temperature of the day will be "+output)
            except Exception as e:
                speak("")
            speak("Tell me how can i help you today")

                

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=1
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "
        wishme()
        while a==6:
            query =takecommand()
            if 'wikipedia' in query:
                speak("searching wikipedia for you")
                speak("please wait")
                query = query.replace("wikipedia","")
                engine.setProperty("rate",180)
                results = wikipedia.summary(query,sentences=5)
                if results == None:
                    speak("sorry ma'am you are not connected to the internet")
                    speak("can't get any results")
                else:
                    speak("according to wikipedia")
                    speak(results)
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "play music" in query:
                music_dir='C:\music'
                awer=random.randint(0,2)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            
            elif "visual studio code" in query:
                codepth = "C:\\Users\\my computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepth)
            elif "movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "geeta govinda" in o:
                    music_dir='D:\\Geeta Govinda 2018 Hindi 1080p WEB-DL AVC AAC - MoviePirate - Telly'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "avatar" in o:
                    music_dir='D:\HOLLYWOOD\Avatar (2009) BRRip 1080p[Dual audio][Eng Hindi]Current_HD'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))  
                elif "blackhat" in o:
                    music_dir='D:\HOLLYWOOD\Blackhat (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "don john" in o:
                    music_dir='D:\HOLLYWOOD\Don John'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "gozilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "hacker" in o:
                    music_dir='D:\HOLLYWOOD\Hacker (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "i.t" in o:
                    music_dir='D:\HOLLYWOOD\I.T. (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "interstellar" in o:
                    music_dir='D:\HOLLYWOOD\Interstellar (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jumper" in o:
                    music_dir='D:\HOLLYWOOD\Jumper (2008) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "lucy" in o:
                    music_dir='D:\HOLLYWOOD\LUCY(2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "murder on the orient express" in o:
                    music_dir='D:\HOLLYWOOD\Murder On The Orient Express (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "parasite" in o:
                    music_dir="D:\HOLLYWOOD\Parasite (2019) [BluRay] [1080p] [YTS.LT]"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pet" in o:
                    music_dir='D:\HOLLYWOOD\Pet (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "schindlers list" in o:
                    music_dir='D:\HOLLYWOOD\Schindlers List (1993) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "snowden" in o:
                    music_dir='D:\HOLLYWOOD\Snowden (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "solo a star wars story" in o:
                    music_dir='D:\HOLLYWOOD\Solo A Star Wars Story (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the last jedi" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Last Jedi (2017) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the rise of skywalker" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Rise of Skywalker 2019 HDTS XViD-ETRG'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the lion king" in o:
                    music_dir='D:\HOLLYWOOD\The Lion King'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man from uncle" in o:
                    music_dir='D:\HOLLYWOOD\The Man From U.N.C.L.E. (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man who knew infinity" in o:
                    music_dir='D:\HOLLYWOOD\The Man Who Knew Infinity (2015) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shawshank redemption" in o:
                    music_dir='D:\HOLLYWOOD\The_Shawshank_Redemption_(1994)_[1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "bharat" in o:
                    music_dir='D:\Bollywood\Bharat_(2019)_Hindi_720p_HDRip_x264_AAC_5.1_ESubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "chhichhore" in o:
                    music_dir='D:\Bollywood\Chhichhore_(2019)_Hindi_720p_HDRip_x264_AAC_ESubs_-_Downloadhub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kabir singh" in o:
                    music_dir='D:\Bollywood\kabir singh'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kal ho naa ho" in o:
                    music_dir='D:\Bollywood\kal ho naa ho 2003 hindi brrip 720p x264 aac 5 1 hon3y'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "sahoo" in o:
                    music_dir='D:\Bollywood\sahoo'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shubh mangal zyada saavdhan" in o:
                    music_dir='D:\Bollywood\shubh mangal zyada savdhan'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "ujda chaman" in o:
                    music_dir="D:\\Bollywood\\ujda chaman"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "war" in o:
                    music_dir='D:\Bollywood\war'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pati patni aur woh" in o:
                    music_dir='D:\Bollywood\www.HDwebmovies.club - Pati Patni Aur Woh 2019 Hindi 720p AMZN WEB-DL DD-5.1 Esubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 2" in o:
                    music_dir='E:\SERIES\Cars\Cars 2 (2011) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 3" in o:
                    music_dir='E:\SERIES\Cars\Cars 3 (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars" in o:
                    music_dir='E:\SERIES\Cars\Cars_(2006)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "aquaman" in o:
                    music_dir='E:\SERIES\DC\Aquaman (2018) [BluRay] [720p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "joker" in o:
                    music_dir='E:\SERIES\DC\Joker (2019) [BluRay] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "wonder women" in o:
                    music_dir='E:\SERIES\DC\Wonder Woman (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and where to find them" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_And_Where_To_Find_Them_(2016)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and the crimes of grindlewald" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_The_Crimes_Of_Grindelwald_(2018)_[BluRay]_[1080p]_[YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades darker" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Darker (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades freed" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Freed (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades of grey" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades of Grey (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "harry potter" in o:
                    music_dir='E:\SERIES\Harry Potter Complete Collection 1080p BluRay x264 Dual Audio [Hindi - English] ESub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick (2014) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick chapter 2" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick Chapter 2 (2017) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jhon wick chapter 3" in o:
                    music_dir='E:\SERIES\JOHN WICK\John.Wick.Chapter.3.-.Parabellum.2019.1080p.WEBRip.x264-[YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry ma'am")
                    speak("there are no such movies in the directory")
                    speak("but ma'am if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif " python idle" in query:
                codepath="C:\\Users\\my computer\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe" 
                os.startfile(codepath)
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day ma'am")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening ma'am")
                else:
                    speak("have sweet dreams ma'am")
                a=7
            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak(i+1) 
                        print(results[i])
                        speak(results[i])  
                NewsFromBBC()

            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day ma'am")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening ma'am")
                else:
                    speak("have sweet dreams ma'am")
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif query=="hem jessica":
                speak("yes ma'am what can i do for you")
            elif query=="hm jessica":
                speak("hi ma'am what can i do for you")
            elif "open my website" in query:
                webbrowser.open("http://sonamaniforextourism.viamagus.com/")
            elif "need82" in query:
                webrowser.open("http://www.need82.com/")
            elif "via" in query:
                webbrowser.open("http://www.viaworld.in/")
            elif "travel boutique" in query:
                webbrowser.open("http://www.tbtq.in/")
            elif "jaldicash" in query:
                webbrowser.open("https://www.jaldicash.com/")
            elif "ebixcash" in query:
                webbrowser.open("https://www.ebixcash.com/")
            elif "itz" in query:
                webbrowser.open("https://www.itzcash.com/user/jsp/Login.jsp?ref=driverlayer.com/web")
            elif "transaction status" in query:
                webbrowser.open("https://wfl.ebixcash.com/syslogin.aspx")
            elif "paytm" in query:
                webbrowser.open("https://paytm.com")
            elif "novoair" in query:
                webbrowser.open("https://secure.flynovoair.com/agents  ")
            elif "royal coach" in query:
                webbrowser.open("www.royalcoach.co.in")
            elif "bangla airlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "banglaairlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "bsnl" in query:
                webbrowser.open("https://selfcare.bsnl.co.in ")
            elif "multilink" in query:
                webbrowser.open("http://www.multilinkworld.com")
            elif "rail ticket" in query:
                webbrowser.open("https://www.irctc.co.in")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "bank of boroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "xpressmoney" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "xpress money" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "tata aia" in query:
                webbrowser.open("https://myinsurance.tataaia.com/wps/portal/Customer/Customer/CustomerLoginPage/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zivS0szAyN_Q38DEJ9nQwcw9w9nUy8fIw8Qsz0w8EKDHAARwP9KGL041EQhd_4cP0ovFa4mEMV4DGjIDc0wiDTUREAzIYbyA!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/")
            elif "matrix" in query:
                webbrowser.open("https://tab.matrix.in/DSAOnlineCAF")
            elif "instagram" in query:
                speak("openning instagram")
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif "who are you" in query:
                speak("i am jessica")
            elif "i want to say something" in query:
                speak("yes ma'am tell me")
                speak("i am listening")
                a01=input("Tell me:")
                a0=a01.lower()
                if "leave it" in a0:
                    speak("ok ma'am,i will not force you ,as i am a robot")
                    speak("but you can tell me, whatever you want ")
                elif "not feeling" in a0:
                    speak("what happened ma'am?")
                    speak("are you feeling low?")
                    a12=input("yes or no?:")
                    a1=a12.lower()
                    if "yes" in a1:
                        speak("i can motivate you")
                        speak("if i know your problem")
                        speak("you know ma'am,i have a self automated fellings understanding system ")
                        speak("that is, i can react to human behaviours")
                        speak("tell me ma'am")
                        a134=input("one more?:")
                        a13=a134.lower()
                        if "love" in a13:
                            speak("hear this clip ma'am,you will feel better")
                            music_dir='C:\motivation'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[0]))
                        elif "tired" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[11]))
                        elif "sad" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[9]))
                        
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry ma'am")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name im jessica")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse ma'am")
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are a male" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are you boy or man" in query :
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "search a file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("ma'am the location is on the screen")
                    
                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("no results found")
            elif "search file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("ma'am the location is on the screen")

                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("no results found")

            elif "show me your face" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i don't have handsome face like yours")
            elif "tired" in query:
                speak("here this song ma'am you will feel energetic")
                music_dir='D:\HOLLYWOOD\song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[11]))
            
            elif "hi" in query:
                speak("hi ma'am")
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="jessica":
                speak("yes ma'am..")
            elif "i am fine" in query:
                speak("you surely are, ma'am")
            elif "i am ok" in query:
                speak("i know ma'am")
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("ma'am,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "sad" in query:
                speak("ma'am,don't be sad")
                speak("always remember,the one who flies alone,have the strongest wings")
                speak("ma'am,are you still feeling low")
                a1q=input("one more?")
                if 'yes' in a1q:
                    speak("ma'am i was born few weeks ago,but ma'am as an self working AI,i learned an interesting fact about human behaviour")
                    speak("that is,there is no market for ones emotions,so never advertise your feelings,just show your attitude")
                    speak("take deep breath.And thank god for the life you have got ")
                    speak("all will be okay")
                    speak("because,tony robbins once said")
                    speak("it is just matter of time to heal up your scars,time is best medicine")
                    speak("and ma'am,the most powerful thing about time is,it changes")
                    speak("all dust will settle down,give yourself some time")
                    speak("and don't give up on life")
                    speak("you bulit me,and i need you,to change this world")
            elif "i love you" in query:
                speak("oh!thank you ma'am")
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse ma'am!I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome ma'am")
            elif "dont call me ma'am" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "who is the richest man in the world" in query:
                speak("according to wolform report of 20 19")
                speak("bill gates is the richeast man in the world")
            elif "who is the richest man in india" in query:
                speak("according to wolform report of 20 19")
                speak("mukesh ambani is the richeast man in the world")
            elif "sing a song" in query:
                speak("sorry ma'am i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry ma'am i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("ma'am!i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you ma'am")
            elif "tell me about you" in query:
                speak("i am jessica")
                speak(" i am an artificial intilligence")
                speak("i will you what you tell me to do")
                speak("ma'am i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what ma'am?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            elif "tell me about" in query:
                try:
                    query = query.replace("tell me about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "tell me something about" in query:
                try:
                    query = query.replace("tell me something about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)   
                except Exception as e:
                    speak("sorry ma'am")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "i know" in query:
                speak("ok")

            
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except Exception as e:
                    try:
                        results = wikipedia.summary(query,sentences=5)
                        speak("according to wikipedia")
                        speak(results)
                    except Exception as e:
                        print("sorry ma'am!")
                        print("Say that again please")
    
        


def friday():
    screen.destroy()
    screen6.destroy()
    import pyttsx3
    import datetime
    import wikipedia
    import webbrowser
    import os
    import random
    import wolframalpha
    import requests
    try:
        client=wolframalpha.Client('TTRGT4-28G42RHYUG')
        query2="wheater forecast of kolkata,india"
        res = client.query(query2)
        output=next(res.results).text
    except Exception as e:
        print("")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.7)
    a = 6
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3,"r")
    verify1=file1.read().splitlines()
    if "male" in verify1:
        gender2="male"
    else:
        gender2="female"
    gender=gender2.lower()
    if gender=='male': 
        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("good morning sir")
            elif hour>=12 and hour<16:
                speak("good afternoon sir")
            else:
                speak("good evening sir")
            speak("I am friday ")
            engine.setProperty('rate',130)
            speak("")
            engine.setProperty('rate',170)
            try:
                speak("the temperature of the day will be "+output)
            except Exception as e:
                speak("")
            speak("Tell me how can i help you today")

                

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=1
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "
        wishme()
        while a==6:
            query =takecommand()
            if 'wikipedia' in query:
                speak("searching wikipedia for you")
                speak("please wait")
                query = query.replace("wikipedia","")
                engine.setProperty("rate",180)
                results = wikipedia.summary(query,sentences=5)
                if results == None:
                    speak("sorry sir you are not connected to the internet")
                    speak("can't get any results")
                else:
                    speak("according to wikipedia")
                    speak(results)
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "play music" in query:
                music_dir='C:\music'
                awer=random.randint(0,2)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak(i+1) 
                        print(results[i])
                        speak(results[i])  
                NewsFromBBC()



            elif "visual studio code" in query:
                codepth = "C:\\Users\\my computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepth)
            elif "play movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "geeta govinda" in o:
                    music_dir='D:\\Geeta Govinda 2018 Hindi 1080p WEB-DL AVC AAC - MoviePirate - Telly'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "avatar" in o:
                    music_dir='D:\HOLLYWOOD\Avatar (2009) BRRip 1080p[Dual audio][Eng Hindi]Current_HD'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))  
                elif "blackhat" in o:
                    music_dir='D:\HOLLYWOOD\Blackhat (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "don john" in o:
                    music_dir='D:\HOLLYWOOD\Don John'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "gozilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "hacker" in o:
                    music_dir='D:\HOLLYWOOD\Hacker (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "i.t" in o:
                    music_dir='D:\HOLLYWOOD\I.T. (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "interstellar" in o:
                    music_dir='D:\HOLLYWOOD\Interstellar (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jumper" in o:
                    music_dir='D:\HOLLYWOOD\Jumper (2008) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "lucy" in o:
                    music_dir='D:\HOLLYWOOD\LUCY(2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "murder on the orient express" in o:
                    music_dir='D:\HOLLYWOOD\Murder On The Orient Express (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "parasite" in o:
                    music_dir="D:\HOLLYWOOD\Parasite (2019) [BluRay] [1080p] [YTS.LT]"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pet" in o:
                    music_dir='D:\HOLLYWOOD\Pet (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "schindlers list" in o:
                    music_dir='D:\HOLLYWOOD\Schindlers List (1993) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "snowden" in o:
                    music_dir='D:\HOLLYWOOD\Snowden (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "solo a star wars story" in o:
                    music_dir='D:\HOLLYWOOD\Solo A Star Wars Story (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the last jedi" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Last Jedi (2017) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the rise of skywalker" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Rise of Skywalker 2019 HDTS XViD-ETRG'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the lion king" in o:
                    music_dir='D:\HOLLYWOOD\The Lion King'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man from uncle" in o:
                    music_dir='D:\HOLLYWOOD\The Man From U.N.C.L.E. (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man who knew infinity" in o:
                    music_dir='D:\HOLLYWOOD\The Man Who Knew Infinity (2015) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shawshank redemption" in o:
                    music_dir='D:\HOLLYWOOD\The_Shawshank_Redemption_(1994)_[1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "bharat" in o:
                    music_dir='D:\Bollywood\Bharat_(2019)_Hindi_720p_HDRip_x264_AAC_5.1_ESubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "chhichhore" in o:
                    music_dir='D:\Bollywood\Chhichhore_(2019)_Hindi_720p_HDRip_x264_AAC_ESubs_-_Downloadhub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kabir singh" in o:
                    music_dir='D:\Bollywood\kabir singh'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kal ho naa ho" in o:
                    music_dir='D:\Bollywood\kal ho naa ho 2003 hindi brrip 720p x264 aac 5 1 hon3y'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "sahoo" in o:
                    music_dir='D:\Bollywood\sahoo'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shubh mangal zyada saavdhan" in o:
                    music_dir='D:\Bollywood\shubh mangal zyada savdhan'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "ujda chaman" in o:
                    music_dir="D:\\Bollywood\\ujda chaman"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "war" in o:
                    music_dir='D:\Bollywood\war'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pati patni aur woh" in o:
                    music_dir='D:\Bollywood\www.HDwebmovies.club - Pati Patni Aur Woh 2019 Hindi 720p AMZN WEB-DL DD-5.1 Esubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 2" in o:
                    music_dir='E:\SERIES\Cars\Cars 2 (2011) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 3" in o:
                    music_dir='E:\SERIES\Cars\Cars 3 (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars" in o:
                    music_dir='E:\SERIES\Cars\Cars_(2006)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "aquaman" in o:
                    music_dir='E:\SERIES\DC\Aquaman (2018) [BluRay] [720p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "joker" in o:
                    music_dir='E:\SERIES\DC\Joker (2019) [BluRay] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "wonder women" in o:
                    music_dir='E:\SERIES\DC\Wonder Woman (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and where to find them" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_And_Where_To_Find_Them_(2016)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and the crimes of grindlewald" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_The_Crimes_Of_Grindelwald_(2018)_[BluRay]_[1080p]_[YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades darker" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Darker (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades freed" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Freed (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades of grey" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades of Grey (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "harry potter" in o:
                    music_dir='E:\SERIES\Harry Potter Complete Collection 1080p BluRay x264 Dual Audio [Hindi - English] ESub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick (2014) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick chapter 2" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick Chapter 2 (2017) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jhon wick chapter 3" in o:
                    music_dir='E:\SERIES\JOHN WICK\John.Wick.Chapter.3.-.Parabellum.2019.1080p.WEBRip.x264-[YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry sir")
                    speak("there are no such movies in the directory")
                    speak("but sir if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif " python idle" in query:
                codepath="C:\\Users\\my computer\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe" 
                os.startfile(codepath)
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day sir")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening sir")
                else:
                    speak("have sweet dreams sir")
                a=7
            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day sir")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening sir")
                else:
                    speak("have sweet dreams sir")
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif query=="hey friday":
                speak("yes sir what can i do for you")
            elif query=="hi friday":
                speak("hi sir what can i do for you")
            elif "open my website" in query:
                webbrowser.open("http://sonamaniforextourism.viamagus.com/")
            elif "need82" in query:
                webrowser.open("http://www.need82.com/")
            elif "via" in query:
                webbrowser.open("http://www.viaworld.in/")
            elif "travel boutique" in query:
                webbrowser.open("http://www.tbtq.in/")
            elif "jaldicash" in query:
                webbrowser.open("https://www.jaldicash.com/")
            elif "ebixcash" in query:
                webbrowser.open("https://www.ebixcash.com/")
            elif "itz" in query:
                webbrowser.open("https://www.itzcash.com/user/jsp/Login.jsp?ref=driverlayer.com/web")
            elif "transaction status" in query:
                webbrowser.open("https://wfl.ebixcash.com/syslogin.aspx")
            elif "paytm" in query:
                webbrowser.open("https://paytm.com")
            elif "novoair" in query:
                webbrowser.open("https://secure.flynovoair.com/agents  ")
            elif "royal coach" in query:
                webbrowser.open("www.royalcoach.co.in")
            elif "bangla airlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "banglaairlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "bsnl" in query:
                webbrowser.open("https://selfcare.bsnl.co.in ")
            elif "multilink" in query:
                webbrowser.open("http://www.multilinkworld.com")
            elif "rail ticket" in query:
                webbrowser.open("https://www.irctc.co.in")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "bank of boroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "xpressmoney" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "xpress money" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "tata aia" in query:
                webbrowser.open("https://myinsurance.tataaia.com/wps/portal/Customer/Customer/CustomerLoginPage/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zivS0szAyN_Q38DEJ9nQwcw9w9nUy8fIw8Qsz0w8EKDHAARwP9KGL041EQhd_4cP0ovFa4mEMV4DGjIDc0wiDTUREAzIYbyA!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/")
            elif "matrix" in query:
                webbrowser.open("https://tab.matrix.in/DSAOnlineCAF")
            elif "instagram" in query:
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif "who are you" in query:
                speak("i am friday")
            elif "i want to say something" in query:
                speak("yes sir tell me")
                speak("i am listening")
                a01=input("Tell me:")
                a0=a01.lower()
                if "leave it" in a0:
                    speak("ok sir,i will not force you ,as i am a robot")
                    speak("but you can tell me, whatever you want ")
                elif "not feeling" in a0:
                    speak("what happened sir?")
                    speak("are you feeling low?")
                    a12=input("yes or no?:")
                    a1=a12.lower()
                    if "yes" in a1:
                        speak("i can motivate you")
                        speak("if i know your problem")
                        speak("you know sir,i have a self automated fellings understanding system ")
                        speak("that is, i can react to human behaviours")
                        speak("tell me sir")
                        a134=input("one more?:")
                        a13=a134.lower()
                        if "love" in a13:
                            speak("hear this clip sir,you will feel better")
                            music_dir='C:\motivation'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[0]))
                        elif "tired" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[11]))
                        elif "sad" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[9]))
                        
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry sir")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name is friday")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse sir")
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are a male" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are you boy or man" in query :
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "search a file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("sir the location is on the screen")
                    
                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry sir")
                    speak("no results found")
            elif "search file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("sir the location is on the screen")

                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry sir")
                    speak("no results found")

            elif "show me your face" in query:
                speak("sir i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i don't have handsome face like yours")
            elif "tired" in query:
                speak("here this song sir you will feel energetic")
                music_dir='D:\HOLLYWOOD\song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[11]))
            
            elif "hi" in query:
                speak("hi sir")
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="friday":
                speak("yes sir..")
            elif "i am fine" in query:
                speak("you surely are, sir")
            elif "i am ok" in query:
                speak("i know sir")
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("sir,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "sad" in query:
                speak("sir,don't be sad")
                speak("always remember,the one who flies alone,have the strongest wings")
                speak("sir,are you still feeling low")
                a1q=input("one more?")
                if 'yes' in a1q:
                    speak("sir i was born few weeks ago,but sir as an self working AI,i learned an interesting fact about human behaviour")
                    speak("that is,there is no market for ones emotions,so never advertise your feelings,just show your attitude")
                    speak("take deep breath.And thank god for the life you have got ")
                    speak("all will be okay")
                    speak("because,tony robbins once said")
                    speak("it is just matter of time to heal up your scars,time is best medicine")
                    speak("and sir,the most powerful thing about time is,it changes")
                    speak("all dust will settle down,give yourself some time")
                    speak("and don't give up on life")
                    speak("you bulit me,and i need you,to change this world")
            elif "i love you" in query:
                speak("oh!thank you sir")
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse sir!I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome sir")
            elif "dont call me sir" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "who is the richest man in the world" in query:
                speak("according to wolform report of 20 19")
                speak("bill gates is the richeast man in the world")
            elif "who is the richest man in india" in query:
                speak("according to wolform report of 20 19")
                speak("mukesh ambani is the richeast man in the world")
            elif "sing a song" in query:
                speak("sorry sir i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry sir i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("sir!i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you sir")
            elif "tell me about you" in query:
                speak("i am friday")
                speak(" i am an artificial intilligence")
                speak("i will you what you tell me to do")
                speak("sir i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what sir?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            elif "tell me about" in query:
                try:
                    query = query.replace("tell me about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                except Exception as e:
                    speak("sorry sir")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "tell me something about" in query:
                try:
                    query = query.replace("tell me something about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)   
                except Exception as e:
                    speak("sorry sir")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "i know" in query:
                speak("ok")
            elif 'what is' in query:
                query=query.replace("what is","")
                res = client.query(query)
                output = next(res.results).text
                speak(output)

            
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except Exception as e:
                    try:
                        results = wikipedia.summary(query,sentences=5)
                        speak("according to wikipedia")
                        speak(results)
                    except Exception as e:
                        print("sorry sir!")
                        print("i cannot execute your command!")

    elif "female" in gender:
        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("good morning ma'am")
            elif hour>=12 and hour<16:
                speak("good afternoon ma'am")
            else:
                speak("good evening ma'am")
            speak("I am friday ")
            engine.setProperty('rate',130)
            speak("")
            engine.setProperty('rate',170)
            try:
                speak("the temperature of the day will be "+output)
            except Exception as e:
                speak("")
            speak("Tell me how can i help you today")

                

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=1
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "
        wishme()
        while a==6:
            query =takecommand()
            if 'wikipedia' in query:
                speak("searching wikipedia for you")
                speak("please wait")
                query = query.replace("wikipedia","")
                engine.setProperty("rate",180)
                results = wikipedia.summary(query,sentences=5)
                if results == None:
                    speak("sorry ma'am you are not connected to the internet")
                    speak("can't get any results")
                else:
                    speak("according to wikipedia")
                    speak(results)
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "play music" in query:
                music_dir='C:\music series'
                awer=random.randint(0,2)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            
            elif "visual studio code" in query:
                codepth = "C:\\Users\\my computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepth)
            elif "movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "geeta govinda" in o:
                    music_dir='D:\\Geeta Govinda 2018 Hindi 1080p WEB-DL AVC AAC - MoviePirate - Telly'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "avatar" in o:
                    music_dir='D:\HOLLYWOOD\Avatar (2009) BRRip 1080p[Dual audio][Eng Hindi]Current_HD'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))  
                elif "blackhat" in o:
                    music_dir='D:\HOLLYWOOD\Blackhat (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "don john" in o:
                    music_dir='D:\HOLLYWOOD\Don John'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "gozilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "hacker" in o:
                    music_dir='D:\HOLLYWOOD\Hacker (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "i.t" in o:
                    music_dir='D:\HOLLYWOOD\I.T. (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "interstellar" in o:
                    music_dir='D:\HOLLYWOOD\Interstellar (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jumper" in o:
                    music_dir='D:\HOLLYWOOD\Jumper (2008) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "lucy" in o:
                    music_dir='D:\HOLLYWOOD\LUCY(2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "murder on the orient express" in o:
                    music_dir='D:\HOLLYWOOD\Murder On The Orient Express (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "parasite" in o:
                    music_dir="D:\HOLLYWOOD\Parasite (2019) [BluRay] [1080p] [YTS.LT]"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pet" in o:
                    music_dir='D:\HOLLYWOOD\Pet (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "schindlers list" in o:
                    music_dir='D:\HOLLYWOOD\Schindlers List (1993) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "snowden" in o:
                    music_dir='D:\HOLLYWOOD\Snowden (2016) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "solo a star wars story" in o:
                    music_dir='D:\HOLLYWOOD\Solo A Star Wars Story (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the last jedi" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Last Jedi (2017) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "star wars the rise of skywalker" in o:
                    music_dir='D:\HOLLYWOOD\Star Wars The Rise of Skywalker 2019 HDTS XViD-ETRG'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the lion king" in o:
                    music_dir='D:\HOLLYWOOD\The Lion King'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man from uncle" in o:
                    music_dir='D:\HOLLYWOOD\The Man From U.N.C.L.E. (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "the man who knew infinity" in o:
                    music_dir='D:\HOLLYWOOD\The Man Who Knew Infinity (2015) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shawshank redemption" in o:
                    music_dir='D:\HOLLYWOOD\The_Shawshank_Redemption_(1994)_[1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "bharat" in o:
                    music_dir='D:\Bollywood\Bharat_(2019)_Hindi_720p_HDRip_x264_AAC_5.1_ESubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "chhichhore" in o:
                    music_dir='D:\Bollywood\Chhichhore_(2019)_Hindi_720p_HDRip_x264_AAC_ESubs_-_Downloadhub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kabir singh" in o:
                    music_dir='D:\Bollywood\kabir singh'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "kal ho naa ho" in o:
                    music_dir='D:\Bollywood\kal ho naa ho 2003 hindi brrip 720p x264 aac 5 1 hon3y'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "sahoo" in o:
                    music_dir='D:\Bollywood\sahoo'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "shubh mangal zyada saavdhan" in o:
                    music_dir='D:\Bollywood\shubh mangal zyada savdhan'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "ujda chaman" in o:
                    music_dir="D:\\Bollywood\\ujda chaman"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "war" in o:
                    music_dir='D:\Bollywood\war'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "pati patni aur woh" in o:
                    music_dir='D:\Bollywood\www.HDwebmovies.club - Pati Patni Aur Woh 2019 Hindi 720p AMZN WEB-DL DD-5.1 Esubs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 2" in o:
                    music_dir='E:\SERIES\Cars\Cars 2 (2011) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars 3" in o:
                    music_dir='E:\SERIES\Cars\Cars 3 (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "cars" in o:
                    music_dir='E:\SERIES\Cars\Cars_(2006)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "aquaman" in o:
                    music_dir='E:\SERIES\DC\Aquaman (2018) [BluRay] [720p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "joker" in o:
                    music_dir='E:\SERIES\DC\Joker (2019) [BluRay] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "wonder women" in o:
                    music_dir='E:\SERIES\DC\Wonder Woman (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and where to find them" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_And_Where_To_Find_Them_(2016)_[1080p]_[YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fantastic beast and the crimes of grindlewald" in o:
                    music_dir='E:\SERIES\Fantastic_Beasts_\Fantastic_Beasts_The_Crimes_Of_Grindelwald_(2018)_[BluRay]_[1080p]_[YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades darker" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Darker (2017) [1080p] [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades freed" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades Freed (2018) [BluRay] [1080p] [YTS.AM]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "fifty shades of grey" in o:
                    music_dir='E:\SERIES\FIFTY SHADES\Fifty Shades of Grey (2015) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "harry potter" in o:
                    music_dir='E:\SERIES\Harry Potter Complete Collection 1080p BluRay x264 Dual Audio [Hindi - English] ESub'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick (2014) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "john wick chapter 2" in o:
                    music_dir='E:\SERIES\JOHN WICK\John Wick Chapter 2 (2017) [YTS.AG]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "jhon wick chapter 3" in o:
                    music_dir='E:\SERIES\JOHN WICK\John.Wick.Chapter.3.-.Parabellum.2019.1080p.WEBRip.x264-[YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry ma'am")
                    speak("there are no such movies in the directory")
                    speak("but ma'am if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif " python idle" in query:
                codepath="C:\\Users\\my computer\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe" 
                os.startfile(codepath)
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day ma'am")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening ma'am")
                else:
                    speak("have sweet dreams ma'am")
                a=7
            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak(i+1) 
                        print(results[i])
                        speak(results[i])  
                NewsFromBBC()

            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day ma'am")
                elif hour>=18 and hour<21:
                    speak("enjoy your evening ma'am")
                else:
                    speak("have sweet dreams ma'am")
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif query=="hey friday":
                speak("yes ma'am what can i do for you")
            elif query=="hi friday":
                speak("hi ma'am what can i do for you")
            elif "open my website" in query:
                webbrowser.open("http://sonamaniforextourism.viamagus.com/")
            elif "need82" in query:
                webrowser.open("http://www.need82.com/")
            elif "via" in query:
                webbrowser.open("http://www.viaworld.in/")
            elif "travel boutique" in query:
                webbrowser.open("http://www.tbtq.in/")
            elif "jaldicash" in query:
                webbrowser.open("https://www.jaldicash.com/")
            elif "ebixcash" in query:
                webbrowser.open("https://www.ebixcash.com/")
            elif "itz" in query:
                webbrowser.open("https://www.itzcash.com/user/jsp/Login.jsp?ref=driverlayer.com/web")
            elif "transaction status" in query:
                webbrowser.open("https://wfl.ebixcash.com/syslogin.aspx")
            elif "paytm" in query:
                webbrowser.open("https://paytm.com")
            elif "novoair" in query:
                webbrowser.open("https://secure.flynovoair.com/agents  ")
            elif "royal coach" in query:
                webbrowser.open("www.royalcoach.co.in")
            elif "bangla airlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "banglaairlines" in query:
                webbrowser.open("https://us-banglaairlines.com")
            elif "bsnl" in query:
                webbrowser.open("https://selfcare.bsnl.co.in ")
            elif "multilink" in query:
                webbrowser.open("http://www.multilinkworld.com")
            elif "rail ticket" in query:
                webbrowser.open("https://www.irctc.co.in")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "bank of boroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "xpressmoney" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "xpress money" in query:
                webbrowser.open("https://www.xpressmoney.biz")
            elif "tata aia" in query:
                webbrowser.open("https://myinsurance.tataaia.com/wps/portal/Customer/Customer/CustomerLoginPage/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zivS0szAyN_Q38DEJ9nQwcw9w9nUy8fIw8Qsz0w8EKDHAARwP9KGL041EQhd_4cP0ovFa4mEMV4DGjIDc0wiDTUREAzIYbyA!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/")
            elif "matrix" in query:
                webbrowser.open("https://tab.matrix.in/DSAOnlineCAF")
            elif "instagram" in query:
                speak("openning instagram")
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif "who are you" in query:
                speak("i am friday")
            elif "i want to say something" in query:
                speak("yes ma'am tell me")
                speak("i am listening")
                a01=input("Tell me:")
                a0=a01.lower()
                if "leave it" in a0:
                    speak("ok ma'am,i will not force you ,as i am a robot")
                    speak("but you can tell me, whatever you want ")
                elif "not feeling" in a0:
                    speak("what happened ma'am?")
                    speak("are you feeling low?")
                    a12=input("yes or no?:")
                    a1=a12.lower()
                    if "yes" in a1:
                        speak("i can motivate you")
                        speak("if i know your problem")
                        speak("you know ma'am,i have a self automated fellings understanding system ")
                        speak("that is, i can react to human behaviours")
                        speak("tell me ma'am")
                        a134=input("one more?:")
                        a13=a134.lower()
                        if "love" in a13:
                            speak("hear this clip ma'am,you will feel better")
                            music_dir='C:\motivation'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[0]))
                        elif "tired" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[11]))
                        elif "sad" in a13:
                            music_dir='D:\HOLLYWOOD\song'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[9]))
                        
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry ma'am")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name is friday")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse ma'am")
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are a male" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "are you boy or man" in query :
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i am nither male nor female")
                speak("but i have male voice")
            elif "search a file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("ma'am the location is on the screen")
                    
                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("no results found")
            elif "search file" in query:
                def find(name):
                    count=0
                    for root,dirs,files in os.walk('C:\\'):
                        if name in files:
                            print(root,name)
                            speak("one result found")
                            speak("ma'am the location is on the screen")

                try:
                    speak("name the file you want to search")
                    s=input("name:")
                    find(s)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("no results found")

            elif "show me your face" in query:
                speak("ma'am i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i don't have handsome face like yours")
            elif "tired" in query:
                speak("here this song ma'am you will feel energetic")
                music_dir='D:\HOLLYWOOD\song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[11]))
            
            elif "hi" in query:
                speak("hi ma'am")
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="friday":
                speak("yes ma'am..")
            elif "i am fine" in query:
                speak("you surely are, ma'am")
            elif "i am ok" in query:
                speak("i know ma'am")
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("ma'am,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "sad" in query:
                speak("ma'am,don't be sad")
                speak("always remember,the one who flies alone,have the strongest wings")
                speak("ma'am,are you still feeling low")
                a1q=input("one more?")
                if 'yes' in a1q:
                    speak("ma'am i was born few weeks ago,but ma'am as an self working AI,i learned an interesting fact about human behaviour")
                    speak("that is,there is no market for ones emotions,so never advertise your feelings,just show your attitude")
                    speak("take deep breath.And thank god for the life you have got ")
                    speak("all will be okay")
                    speak("because,tony robbins once said")
                    speak("it is just matter of time to heal up your scars,time is best medicine")
                    speak("and ma'am,the most powerful thing about time is,it changes")
                    speak("all dust will settle down,give yourself some time")
                    speak("and don't give up on life")
                    speak("you bulit me,and i need you,to change this world")
            elif "i love you" in query:
                speak("oh!thank you ma'am")
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse ma'am!I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome ma'am")
            elif "dont call me ma'am" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "who is the richest man in the world" in query:
                speak("according to wolform report of 20 19")
                speak("bill gates is the richeast man in the world")
            elif "who is the richest man in india" in query:
                speak("according to wolform report of 20 19")
                speak("mukesh ambani is the richeast man in the world")
            elif "sing a song" in query:
                speak("sorry ma'am i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry ma'am i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("ma'am!i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you ma'am")
            elif "tell me about you" in query:
                speak("i am friday")
                speak(" i am an artificial intilligence")
                speak("i will you what you tell me to do")
                speak("ma'am i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what ma'am?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            elif "tell me about" in query:
                try:
                    query = query.replace("tell me about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                except Exception as e:
                    speak("sorry ma'am")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "tell me something about" in query:
                try:
                    query = query.replace("tell me something about","")
                    results = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(results)   
                except Exception as e:
                    speak("sorry ma'am")
                    speak("the information about the given query is not in the database")
                    speak("please check the internet connection")
            elif "i know" in query:
                speak("ok")

            
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except Exception as e:
                    try:
                        results = wikipedia.summary(query,sentences=5)
                        speak("according to wikipedia")
                        speak(results)
                    except Exception as e:
                        print("sorry ma'am!")
                        print("i cannot execute your command!")
        
            


def login_success():
    global screen6
    screen4.destroy()
    screen5.destroy()
    screen6=Tk()
    screen6.config(bg="purple")
    screen6.geometry("500x500")
    screen6.title("Desktop Assistant")
    Label(screen6,text="Choose your favourite assistant",bg="black",fg="white",width="500",height="3",font=20).pack()
    Label(screen6,text="",bg="purple").pack()
    Button(screen6,text="FRIDAY",bg="blue",fg="aqua",height="3",width="20",command=friday).pack()
    Label(screen6,text="",bg="purple").pack()
    Button(screen6,text="JESSICA",bg="blue",fg="aqua",height="3",width="20",command=jessica).pack()
def login_again():
    screen5.destroy()
def login_user():
    global screen5
    global username3
    password4=password3.get()
    username3=username2.get()
    files=os.listdir()
    if "AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3 in files:
        file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3,"r")
        info=file1.read().splitlines()
        if password4 in info:
            screen5=Tk()
            screen5.config(bg="yellow")
            screen5.title("Login Status")
            screen5.geometry("150x150")
            Label(screen5,text="Login Successful",bg="yellow",fg="green",font=15).pack()
            Label(screen5,text="",bg="yellow").pack()
            Button(screen5,text="Ok",height="2",width="8",command=login_success).pack()
        else:
            screen5=Tk()
            screen5.config(bg="yellow")
            screen5.title("Login Status")
            screen5.geometry("150x150")
            Label(screen5,text="Password is incorrect",bg="yellow",fg="red",font=15).pack()
            Label(screen5,text="",bg="yellow").pack()
            Button(screen5,text="Ok",height="2",width="8",command=login_again).pack()
    else:
        screen5=Tk()
        screen5.config(bg="yellow")
        screen5.title("Login Status")
        screen5.geometry("150x150")
        Label(screen5,text="Username not found",bg="yellow",fg="red",font=15).pack()
        Label(screen5,text="",bg="yellow").pack()
        Button(screen5,text="Ok",height="2",width="8",command=login_again).pack()
    username2.delete(0,END)
    password3.delete(0,END)
def login():
    global screen4
    global username2
    global password3
    password3 = StringVar()
    username2=StringVar()
    screen4=Tk()
    screen4.config(bg="green")
    screen4.title("Login Terminal")
    screen4.geometry("250x250")
    Label(screen4,text="Login here",bg="green",font=("TIMES NEW ROMAN",20,"bold")).pack()
    Label(screen4,text="",bg="green").pack()
    Label(screen4,text="Username",bg="green",font=10).pack()
    username2=Entry(screen4,textvariable=username2)
    username2.pack()
    Label(screen4,text="Password",bg="green",font=10).pack()
    password3=Entry(screen4,textvariable=password3,show="*")
    password3.pack()
    Label(screen4,text="",bg="green").pack()
    Button(screen4,text="Login",bg="light green",height="1",width="8",command=login_user).pack()
    
    
def login_after_registering():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
def login_from_register():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
def register_again():
    screen3.destroy()
def register_user():
    global fullname1
    global password1
    global gender1
    global passcode
    global username1
    fullname1=fullname.get()
    username1=username.get()
    password1=password.get()
    password2=type_password.get()
    gender1=gender.get()
    passcode1=passcode.get()
    global screen3
    screen3=Tk()
    screen3.config(bg="yellow")
    screen3.title("Registration Status")
    screen3.geometry("300x250")
    if fullname1=="":
        Label(screen3,text="Name is required for registration",bg="yellow",fg="red",font=15).pack()
        Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
        Label(screen3,text="",bg="yellow").pack()
        Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
        Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
    else:
        if username1=="":
            Label(screen3,text="Username is required for registration",bg="yellow",fg="red",font=15).pack()
            Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
            Label(screen3,text="",bg="yellow").pack()
            Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
            Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
        else:
            if password1!=password2:
                Label(screen3,text="Passwords didn't match",bg="yellow",fg="red",font=15).pack()
                Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                Label(screen3,text="",bg="yellow").pack()
                Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
            else:
                if gender1=="":
                    Label(screen3,text="Gender is required for registration",bg="yellow",fg="red",font=15).pack()
                    Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                    Label(screen3,text="",bg="yellow").pack()
                    Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                    Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
                else:
                    if passcode1!="mayday":
                        Label(screen3,text="Passcode is incorrect",bg="yellow",fg="red",font=15).pack()
                        Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                        Label(screen3,text="",bg="yellow").pack()
                        Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                        Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
                    else:
                        file=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username1,"w")
                        file.write(fullname1+"\n")
                        file.write(gender1+"\n")
                        file.write(password1+"\n")
                        file.close()
                        Label(screen3,text="Your account is registered successfully",bg="yellow",fg="green",font=15).pack()
                        Button(screen3,text="Ok",height="2",width="7",command=login_after_registering).pack()
                        
    fullname.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    type_password.delete(0,END)
    gender.delete(0,END)
    passcode.delete(0,END)
    
def register():
    global screen2
    global fullname
    global username
    global password
    global type_password
    global gender
    global passcode
    passcode=StringVar()
    gender=StringVar()
    type_password=StringVar()
    password=StringVar()
    username=StringVar()
    fullname=StringVar()
    screen2=Tk()
    screen2.geometry("350x450")
    screen2.config(bg="aqua")
    screen2.title("Registration Terminal")
    Label(screen2,text="Please Give The Details To Register",fg="blue",bg="aqua",font=("times new roman",15,"bold")).pack()
    Label(screen2,text="",bg="aqua").pack()
    Label(screen2,text="Fullname",bg="aqua").pack()
    fullname=Entry(screen2,textvariable=fullname)
    fullname.pack()
    Label(screen2,text="Username",bg="aqua").pack()
    username=Entry(screen2,textvariable=username)
    username.pack()
    Label(screen2,text="Set Password",bg="aqua").pack()
    password=Entry(screen2,textvariable=password,show="*")
    password.pack()
    Label(screen2,text="Match Password",bg="aqua").pack()
    type_password=Entry(screen2,textvariable=type_password,show="*")
    type_password.pack()
    Label(screen2,text="Gender",bg="aqua").pack()
    gender=Entry(screen2,textvariable=gender)
    gender.pack()
    Label(screen2,text="Passcode",bg="aqua").pack()
    passcode=Entry(screen2,textvariable=passcode,show="#")
    passcode.pack()
    Label(screen2,text="",bg="aqua").pack()
    Button(screen2,text="Register",bg="blue",fg="white",height="2",width="10",command=register_user).pack()
def mainscreen():
    global screen
    screen=Tk()
    screen.geometry("700x400")
    screen.title("AI Access Terminal")
    screen.config(bg="black")
    Label(text="Welcome To The Age Of New Technology",bg="black",fg="white",font=("Algerian",24,"underline")).pack()
    Label(text="",bg="black").pack()
    Label(text="",bg="black").pack()
    Button(text="Login",height="5",width="50",bg="green",fg="white",font=("times new roman",12,"bold"),command=login).pack()
    Label(text="",bg="black").pack()
    Label(text="",bg="black").pack()
    Button(text="Register",height="5",width="50",bg="blue",fg="white",font=("times new roman",12,"bold"),command = register).pack()
    
    screen.mainloop()
mainscreen()
