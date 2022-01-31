import time
import webbrowser
import pyautogui as pg

i=0
j=0
links=[]
times=[]

rows=int(input("enter number of rows in today's timetable : "))

now = time.strftime("%H:%M:%S")

for i in range(1,rows+1):
    name=input("enter name of lecture : ")
    link=links.append(input("paste link of lecture : "))
    ti=times.append(input("enter time (hh:mm:ss) :"))
    
    

for j in range(1,rows+1):
    link=links[j-1]
    tim=times[j-1]

    while (now != tim): 
        print ("Waiting, the current time is " + now +" :-( " )
        now = time.strftime("%H:%M:%S") 
        time.sleep(1) 
# Opening the webpage at alarm time
    if (now == tim): 
        print ("WEBSITE IS OPENING :D") 
        webbrowser.open(link)
    time.sleep(10)
    pg.click(1212,611)
    time.sleep(10)
    pg.click(1125,479)
    time.sleep(6)
    pg.click(1498,759)
    