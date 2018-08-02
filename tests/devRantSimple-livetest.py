import sys
sys.path.append('../devRantSimple')
import devRantSimple as dRS

# print(dRS.getUserRant("ewpratten", 10000))

prevdata = ""
i = 0
while prevdata != dRS.InvalidResponse:
	print(dRS.getUserRant("ewpratten", i)["text"])
	i+=1