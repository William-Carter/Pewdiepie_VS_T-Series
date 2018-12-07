# Pewdiepie_VS_T-Series
*Simple live subscriber comparison*
Hey there. You're probably here because you support either Pewdiepie or T-Series in this battle. You can change a few values in the script file to compare different channels.

Prerequisites:
-Python 3.7

Setup:
  Google API Key:
    First you'll need a google api key. Go here:
    https://console.developers.google.com/cloud-resource-manager
    Hit create new project. Name it whatever and hit create.
    Wait for about 30 seconds and then click into your project from the drop down at the top
    Click the menu bar in the top left and go to APIs and Services>Library
    Search for youtube and click on YouTube Data API v3
    Now click enable
    Once that is done, click on the menu in the top left again.
    Now go to APIs and Services>Credentials
    Click Create Credentials>API Key
    You should now have your API key!
    Add this into the script.py file where it says userKey (inside the quotations)
    Running the program now should give you a live update every few seconds (exact times vary on your network speed)

  Using different channels:
    To use a different channel, first locate the Info section near the top of the script.py file
    Change the name values of either channel, or both, to the name or names you want to use
    Change the jsonFile values to whatever name you want the files to have in your folder. You will also have to rename the files already there
    Finally, get the channelID. For a small channel this is just the part of the channel URL that starts with UC, but for a larger channel, go to this site (being sure to change apiKey to your API key and channelName to the name on the channel page):
    https://www.googleapis.com/youtube/v3/channels?key=apiKey&forUsername=channelName&part=id
    The "ID" value down the bottom is what you're looking for.
    Make sure the channelID is in place and go ahead and run the file.
