import discord
from discord import message
import requests
from bs4 import BeautifulSoup
import re


#Bot code
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(1150634132444020756);
    await channel.send(embed=embed)
   


#Web-Scraping from site
URL = 'https://my3.my.umbc.edu/groups/seb/events'
page = requests.get(URL)

site = BeautifulSoup(page.content, "html.parser")




eventTitle = site.find_all('div', attrs={"class": "content"})
date = site.find_all('div', attrs={"class": "times",})
time = site.find_all('div', attrs={"class": "starts-at",})
num = 1

dates = {}
times = {}
event = {}
#Event Dictionary
for i in eventTitle:
    event["title"+str(num)] =  i.find('a').string
    event["link"+str(num)] =  ("https://my3.my.umbc.edu" + i.find('a')["href"])
    x = (i.find("span", attrs={"class":"blurb"}))
    x = re.sub("<span class=\"blurb\">" ,"", str(x))
    event["description"+str(num)] = re.sub("</span>" ,"", str(x))       
    l =  i.find("span", attrs={"class":'location'})                    
    l = re.sub("<span class=\"location\">","", str(l))
    event["location"+str(num)] = re.sub("·</span>" ,"", str(l)) 

    num+=1
## Dates 
num = 1
for j in date:
    x = j.find('div', attrs={"class":'date'})
    x = re.sub("<div class=\"date\">" ,"", str(x))
    dates["date"+str(num)] = re.sub("</div>" ,"", str(x)) 
    num+=1
#Times
num = 1
for j in time:
    x = j.find('div', attrs={"class":'time'})
    x = re.sub("<div class=\"time\">" ,"", str(x))
    times["time"+str(num)] = re.sub("</div>" ,"", str(x)) 
    num+=1



 
num2 = 1

embed=discord.Embed( color=0xBEBEFE, title="SEB Weekly Events:", type='rich', url="https://my3.my.umbc.edu/groups/seb" , description= "Events happening this week!")

for i in eventTitle:
    embed.add_field(name= str(dates["date"+str(num2)]) + ", @ " + str(times["time"+str(num2)]) + "\n"+ str(event["title"+str(num2)]) + "\nWhere: " + str(event["location"+str(num2)]) + "\n"  , value=str(event["description"+str(num2)]) + "\n", inline=False)
    num2+=1
    if num2 == 6:
        break


  
  
  

client.run('MTIwODI1NjA2NDExMDIwMjkyMA.GdwlOO.E_ZrhwviRs1Hta55ipObh95xxSs5LC5FMBMWEs')

 
