import requests
import json
import os
import sys 

 
os.system("echo Search4 | toilet -f mono12 --filter border:metal")




username = input("Enter users username : ")
print("\n")
print("\033[1;32;40m Started at :")
os.system("date")


# github

print("\n \n ")
git = requests.get('https://github.com/'+username)
gitres = (git.status_code)
gitaddress = ("https://github.com/"+username)
json_response = (git.json)

if gitres == 200: 
   if json_response == 'Account not found' :
       print("Github : Account not found on {}" .format(gitaddress))
   else:
   		print("Github (VOLA)  : Account found on {}" .format(gitaddress))
elif gitres == 404:
	print("Github (404) : Error page not found")



# twitter

print("\n \n")
twitter = requests.get('https://twitter.com/'+username)
twitterres = (git.status_code)
twitteraddress = ("https://twitter.com/"+username)
json_response = (twitter.json)

if twitterres == 200: 
   if json_response == 'Account not found':
       print("Twitter : Account not found on {}" .format(twitteraddress))
   else:
       print("Twitter (VOLA) : Account found on {}" .format(twitteraddress))
elif twitterres == 404:
	print("Twitter (404) : Error page not found")



# youtube

print("\n \n")
youtube = requests.get("https://www.youtube.com/c/"+username)
youtuberes = (youtube.status_code)
youtubeaddress = ("https://www.youtube.com/"+username)
json_response = (youtube.json)



if youtuberes == 200: 
   if json_response == 'Account not found':
       print("YouTube : Account not found on {}" .format(youtubeaddress))
   else:
   		print("YouTube (VOLA) : Account found on {}" .format(youtubeaddress))
elif youtuberes == 404:
	print("YouTube (404) : Error page not found")
	

	
# facebook

print("\n \n")
facebook = requests.get("https://www.facebook.com/"+username)
facebookres = (facebook.status_code)
facebookaddress = ("https://www.facebook.com/"+username)
json_response = (facebook.json)

if facebookres == 200: 
   if json_response == 'Account not found':
       print("Facebook : Account not found on {}" .format(facebookaddress))
   else:
       print("Facebook (VOLA) : Account found on {}" .format(facebookaddress))
elif facebookres == 404:
	print("Facebook (404) : Error page not found")
	


# Instagram

print("\n \n")
instagram = requests.get("https://instagram.com/"+username)
instagramres = (instagram.status_code)
instagramaddress = ("https://instagram.com/"+username)
json_response = (instagram.json)

if instagramres == 200:
	if json_response == 'Account not found ':
		print("Instagram : Account not found on {}" .format(instagramaddress))
	else:
		print("Instagram (VOLA) : Account found on {}" .format(instagramaddress))
elif instagramres == 404:
	print("Instagram (404) : Error page not found")
	



# Reddit

print("\n \n")
reddit = requests.get("https://www.reddit.com/r/"+username)
redditres = (reddit.status_code)
redditaddress = ("https://www.reddit.com/r/"+username)
json_response = (reddit.json)

if redditres == 200:
	if json_response == 'Account not found ':
		print("Reddit : Account not found on {}" .format(redditaddress))
	else:
		print("Reddit (VOLA) : Account found on {}" .format(redditaddress))
else:
	print("Reddit (404) : Error page not found")




# Telegram
# Indian Error 

# Discord
# problem



# Twitch

print("\n \n")
twitch = requests.get("https://m.twitch.tv/"+username)
twitchres = (twitch.status_code)
twitchaddress = ("https://m.twitch.tv/"+username)
json_response = (twitch.json)

if twitchres == 200:
	if json_response == 'Account not found ':
		print("Twitch : Account not found on {}" .format(twitchaddress))
	else:
		print("Twitch (VOLA) : Account found on {}" .format(twitchaddress))
else:
	print("Twitch (404) : Error page not found")



# LinkedIn
# problem

# google+
# error

# flickr
# not found




# Quora

print("\n \n")
quora = requests.get("https://www.quora.com/profile/"+username)
quorares = (quora.status_code)
quoraaddress = ("https://www.quora.com/profile/"+username)
json_response = (quora.json)

if quorares == 200:
	if json_response == 'Account not found ':
		print("Quora : Account not found on {}" .format(quoraaddress))
	else:
		print("Quora (VOLA) : Account found on {}" .format(quoraaddress))
else:
	print("Quora (404) : Error page not found")




# my Space
# error




# VK

print("\n \n")
vk = requests.get("https://m.vk.com/"+username)
vkres = (vk.status_code)
vkaddress = ("https://m.vk.com/"+username)
json_response = (vk.json)

if vkres == 200:
	if json_response == 'Account not found ':
		print("VK : Account not found on {}" .format(vkadress))
	else:
		print("VK (VOLA) : Account found on {}" .format(vkaddress))
else:
	print("VK (404) : Error page not found")
	

	
	
# Pinterest
	
print("\n \n")
pinterest = requests.get("https://www.pinterest.com/"+username)
pinterestres = (pinterest.status_code)
pinterestaddress = ("https://www.pinterest.com/"+username)
json_response = (pinterest.json)

if pinterestres == 200:
	if json_response == 'Account not found ':
		print("Pinterest : Account not found on {}" .format(pinterestadress))
	else:
		print("Pinterest (VOLA) : Account found on {}" .format(pinterestaddress))
else:
	print("Pinterest (404) : Error page not found")
	

	
# Snapchat
# error

# stakoverflow
# it has a unique id plus username



# Vimeo

print("\n \n")
vimeo = requests.get("https://vimeo.com/"+username)
vimeores = (vimeo.status_code)
vimeoaddress = ("https://vimeo.com/"+username)
json_response = (vimeo.json)

if vimeores == 200:
	if json_response == 'Account not found ':
		print("Vimeo : Account not found on {}" .format(vimeoadress))
	else:
		print("vimeo (VOLA) : Account found on {}" .format(vimeoaddress))
else:
	print("Vimeo (404) : Error page not found")

	
	
# Tumblr

print("\n \n")
tumblr = requests.get(f"https://{username.lower()}.tumblr.com")
tumblrres = (tumblr.status_code)
tumblraddress = (f"https://{username.lower()}.tumblr.com")
json_response = (tumblr.json)

if tumblrres == 200:
	if json_response == 'Account not found ':
		print("Tumblr : Account not found on {}" .format(tumblradress))
	else:
		print("Tumblr (VOLA) : Account found on {}" .format(tumblraddress))
else:
	print("Tumblr (404) : Error page not found")

print("\n \n")
print("DONE..! \n ")
print("Use ctrl+c to exit")
