import urllib.request, json, os
#Put your google API key here - if you don't have one you can get one for free
#Just search google api console, create a project, select credentials and create an api key
userKey = ""
dir_path = os.path.dirname(os.path.realpath(__file__))


#-------Info-------#
#Pewdiepie
channel1Name = "Pewdiepie"
channel1Json = "pewdiepieStats.json"
channel1ID = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"

#T-Series
channel2Name = "T-Series"
channel2Json = "tseriesStats.json"
channel2ID = "UCq-Fj5jknLsUf-MWSy4_brA"

#Make sure you rename the two default files to what you have setup as the Json names
def getSubCount(jsonName, chanID):
    with open(dir_path+"/"+jsonName, 'r+', encoding='utf-8-sig') as json_file:
        json_file.write(urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+chanID+"&key="+userKey).read().decode("utf-8") )
    with open(dir_path+"/"+jsonName, 'r+', encoding='utf-8-sig') as json_file:
        text = json_file.read()
        json_data = json.loads(text)


    subcount = (json_data["items"][0]["statistics"]["subscriberCount"])
    return(int(subcount))


while True:
    subCount1 = getSubCount(channel1Json, channel1ID)
    subCount2 = getSubCount(channel2Json, channel2ID)
    if subCount1 > subCount2:
        print(channel1Name, "is leading by", subCount1-subCount2)
    elif subCount2 < subCount1:
        print(channel2Name, "is leading by", subCount2-subCount1)
    else:
              print("I'TS HAPPPENING")
