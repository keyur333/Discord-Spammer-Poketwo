from webserver import keep_alive
import requests

channelID = 1069814108930723924
headers = {
    "authorization":
    "ODQ5MzAxMDM5OTc1MTA0NTQz.GtFXem.3VGGwHf6idICM3EtbbQB7v5sbxqY9pwGHWQ81k"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
