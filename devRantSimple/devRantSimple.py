# devRantSimple
# by: Evan Pratten <ewpratten>

# Required libs: requests, enum34
import requests
from enum import Enum
# import classes as classes

# devrant api app id
appid = 3

# Enums
RantType = Enum("RantType", "algo top recent")
ImageSize = Enum("ImageSize", "large small")
NotifType = Enum("NotifType", "vote mention content sub")

InvalidResponse = "dRS.INVALID.."


def genRantCode(rid):
	return str('{0:x}'.format(int(rid)))

def genRantId(rcode):
	return int(rcode, 16)

def getUserId(username):
	data = rawGet("get-user-id", {"username":username})
	return data["user_id"]

def userExsists(username):
	data = rawGet("get-user-id", {"username":username})
	if data["success"]:
		return True
	else:
		return False
	
def rawGet(endpoint, params):
	params.update({"app":appid})
	rawrant = requests.get("https://devrant.com/api/" + endpoint, params=params)
	return rawrant.json()

def rawGetnj(endpoint, params):
	params.update({"app":appid})
	rawrant = requests.get("https://devrant.com/api/" + endpoint, params=params)
	return rawrant

def getUserData(userid, params):
	return rawGet("users/" + str(userid), params)


def getRant(Rtype, Rnum):
	offset = Rnum - 1
	if Rtype == RantType.algo:
		sort = "algo"
	elif Rtype == RantType.top:
		sort = "top"
	elif Rtype == RantType.recent:
		sort = "recent"
	else:
		print("[dRS]: ERROR! Invalid rant type given in function getRant()\n       Valid types: algo, top, recent")
	
	rant = rawGet("devrant/rants", {"sort":sort, "limit":1, "skip":offset})
	if rant["success"]:
		returndata = {"id":rant["rants"][0]["id"], "text":rant["rants"][0]["text"], "score":rant["rants"][0]["score"], "username":rant["rants"][0]["user_username"], "tags":rant["rants"][0]["tags"]}
	else:
		returndata = InvalidResponse
	return returndata

def getUserRant(user, Rnum):
	offset = Rnum - 1
	if not userExsists(user):
		print("[dRS]: ERROR! Invalid username given in function getUserRant()")
	else:
		userid = getUserId(user)
		userdata = getUserData(userid, {"skip":offset, "content":"rants"})
		
		if userdata["success"] and userdata["profile"]["content"]["content"]["rants"] != []:
			returndata = {"text":userdata["profile"]["content"]["content"]["rants"][0]["text"], "score":userdata["profile"]["content"]["content"]["rants"][0]["score"], "tags":userdata["profile"]["content"]["content"]["rants"][0]["tags"], "id":userdata["profile"]["content"]["content"]["rants"][0]["id"]}
		else:
			returndata = InvalidResponse
		
		return returndata

def getAvatar(username, size=ImageSize.small):
	if not userExsists(username):
		print("[dRS]: ERROR! Invalid username given in function getUserRant()")
	else:
		uid = getUserId(username)
		userdata = getUserData(uid, {})
		if size == ImageSize.small:
			imgdata = userdata["profile"]["avatar_sm"]["i"]
			return "https://avatars.devrant.com/" + imgdata
		elif size == ImageSize.large:
			imgdata = userdata["profile"]["avatar"]["i"]
			return "https://avatars.devrant.com/" + imgdata
		else:
			print("[dRS]: ERROR! Invalid avatar size given in function getAvatar()")
			return InvalidResponse

def login(username, password):
	if not userExsists(username):
		print("[dRS]: ERROR! Invalid username given in function login()")
		return InvalidResponse
	else:
		rawdata = requests.post("https://devrant.com/api/users/auth-token", data={"username":username, "password":password, "app":3})
		rawdata = rawdata.json()
		if not rawdata["success"]:
			print("[dRS]: Login error. Wrong password?")
			return InvalidResponse
		else:
			return {"token_id":rawdata["auth_token"]["id"], "token_key":rawdata["auth_token"]["key"], "user_id":rawdata["auth_token"]["user_id"]}

def postRant(text, tags, uid, token, key):
	rsp = requests.post("https://devrant.com/api/devrant/rants", data={"app":3, "user_id":uid, "token_id":token, "token_key":key, "rant":text, "tags":tags})
	return rsp

def comment(rantid, text, uid, token, key):
	rsp = requests.post("https://devrant.com/api/devrant/rants/" + str(rantid) + "/comments", data={"app":3, "user_id":uid, "token_id":token, "token_key":key, "comment":text, "plat":2})
	return rsp.json()

def getNotifs(uid, token, key):
	rsp = requests.get("https://devrant.com/api/users/me/notif-feed", params={"user_id":uid, "token_id":token, "token_key":key, "app":"3"})
	return rsp.json()

def clearNotifs(uid, token, key):
	rsp = requests.delete("https://devrant.com/api/users/me/notif-feed", params={"user_id":uid, "token_id":token, "token_key":key, "app":"3"})
	return rsp.json()

def vote(rantid, uid, token, key, vote):
	rsp = requests.post("https://devrant.com/api/devrant/rants/" + str(rantid) + "/vote", data={"app":3, "user_id":uid, "token_id":token, "token_key":key, "vote":vote, "plat":3})
	return rsp.json()

def getIdRant(rantid):
	rsp = rawGet("devrant/rants/" + str(rantid), {})
	return rsp

def getRantFromId(rantid):
	# print(rantid)
	rant = getIdRant(rantid)
	# print(rant)
	if rant["success"]:
		returndata = {"id":rant["rant"]["id"], "text":rant["rant"]["text"], "score":rant["rant"]["score"], "username":rant["rant"]["user_username"], "tags":rant["rant"]["tags"], "comments":rant["comments"]}
	else:
		returndata = InvalidResponse
	return returndata
	
def getIdComment(rid, cid, uid, token, key):
	rsp = requests.get("https://devrant.com/api/comments/"+ str(cid), params={"user_id":uid, "token_id":token, "token_key":key, "app":3})
	return rsp.json()
# debug
