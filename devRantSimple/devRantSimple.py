# devRantSimple
# by: Evan Pratten <ewpratten>

# Required libs: requests, enum34
import requests
from enum import Enum

# devrant api app id
appid = 3

# Enums
RantType = Enum("RantType", "algo top recent")
InvalidResponse = "dRS.INVALID.."

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


def getRant(Rtype, Rnum):
	offset = Rnum - 1
	if Rtype == RantType.algo:
		sort = "algo"
	elif Rtype == RantType.top:
		sort = "top"
	elif Rtype == RantType.recent:
		sort = "recent"
	else:
		print("[dSR]: ERROR! Invalid rant type given in function getRant()\n       Valid types: algo, top, recent")
	
	rant = rawGet("devrant/rants", {"sort":sort, "limit":1, "skip":offset})
	if rant["success"]:
		returndata = {"id":rant["rants"][0]["id"], "text:":rant["rants"][0]["text"], "score":rant["rants"][0]["score"], "username":rant["rants"][0]["user_username"]}
	else:
		returndata = InvalidResponse
	return returndata

def getUserRant(user, Rnum):
	offset = Rnum - 1
	if not userExsists(user):
		print("[dSR]: ERROR! Invalid username given in function getUserRant()")
	else:
		userid = getUserId(user)
		userdata = rawGet("users/" + str(userid), {"skip":offset, "content":"rants"})
		
		if userdata["success"] and userdata["profile"]["content"]["content"]["rants"] != []:
			returndata = {"text":userdata["profile"]["content"]["content"]["rants"][0]["text"], "score":userdata["profile"]["content"]["content"]["rants"][0]["score"], "tags":userdata["profile"]["content"]["content"]["rants"][0]["tags"], "id":userdata["profile"]["content"]["content"]["rants"][0]["id"]}
		else:
			returndata = InvalidResponse
		
		return returndata
	
	