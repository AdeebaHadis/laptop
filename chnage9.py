@eel.expose
def allcommand();
    quary=takecommand()
    print(quary)

    if 'open'in quary:
        print('I run')
    else:
        print('not run')


        def PlayYouTube(query):
            search_term=extract_yt_term(query)
            if search_term:
                speak("playing"+search_term+"on YouTube")
                kit.playonyt(serach_term)
            else:
                speak("sorry,i couldn't find what to play on YouTube.")

                 line 7 in features: import pywhatkit as kit


                def extract_yt_term(command):
                    pattern=r'play\s+(.*?)\s+on\s+youtube'
                    match=re.search(pattern,command,re.IGNORECASE)
                    return match.group(1) if match else none
                

                
            elif 'on youtube':
from engine.features import PlayYoutube
playYoutube(query)


time.sleep(2)

eel.showHood()

eel.displaymessage(text)



import sqlite3

conn = aqlite3.connect("sophia.db")

cursor=con.cursor()

# to create a table
query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

#to insert values
quary="INSERT INTO sys_command VALUES(null,'visual studio code','')"
cursor.execute(query)
con.commit()
con.clsoe() # don't forget to close the connection when done

query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)


if query!="":
    try:
        #Try to find the application in sys_command table
        cursor.execute('SELECT path FROM sys_command WHERE LOWER(name)=?',(wuery,))
        results=cursor.fetchall()

        if len(results)!=0:
            speak("opening"+query)
            os.startfile(results[0][0])
            return
        
        # if not found,try to find the URL in web_command table
        cursor.execute('SELECT url FROM web_command WHERE LOWER(name)=?',(query,))
        results=cursor.fetchall()

        if len(results)!=0:
            speak("opening"+query)
            webbrowser.open(results[0][0])
            return
        
        # if still not found,try to open using os.system
        speak("opening"+query)
        try:
            os.system('start'+query)
        except exception as e:
            speak(f"unable to open{query}.error:{str(e)}")

        except Exception as e:
            speak(f"something went wrong:{str(e)}")