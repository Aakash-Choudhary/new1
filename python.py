#!/usr/bin/python3
import time
import webbrowser 
import subprocess
option"""

press 3 to open your search in web browser :
"""
print(option)

choice=int(input())

#if choice == 5:
	#current_time=time.ctime()
	#print(current_time) 
if choice == 3: 
	data = input("enter the search")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data) 

x = ["https://en.wikipedia.org/wiki/hello_(adele_song)","https://hello.com/", "https://supersimple.com/song/hello/","https://www.hellomagazine.com/","https://en.oxforddictionaries.com/definition/hello/"]
print("the list is :: ")

print(x)

for i  in range(5) :
	webbrowser.open_new_tab(x[i])
	i = i+1
	time.sleep(2)	


