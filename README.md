# devRantSimple
A simple devRant api wrapper for the lazy people

## Installation
First, get it from pip
```bash
pip install devRantSimple
```

Then, import the library
```python
import devRantSimple as dRS
```
That's it!

## Usage
These are the avalible functions and vars:
```python
import devRantSimple as dRS

# Rant Types
# These are passed in to some functions to specify what data you want returned
dRS.RantType.algo   # Algo
dRS.RantType.top    # Top
dRS.RantType.recent # Recent

# Invalid Response
# This is a string returned by some functions when something goes wrong.
# It is always a smart idea to check if the thing returned by the function you are using is equal to this
# If it is, you messsed up somewhere. (or the api changed)
dRS.InvalidResponse

# Functions
dRS.getUserId("<username>")   # Get a user id from a username (returns an int)
dRS.userExists("<username>")  # Check to see if a user exists with this username (returns a bool)

dRS.getRant(dRS.RantType.<type>, <n>) # Get the n'th rant from list <type> 
# Example return data for these parameters: (dRS.RantType, 1):
# {'id': 1604103, 'text:': "Oh yeah. Hey guys. 2 things. \nFirst off. Forgot to say. Officially got a job. Finally. So thank you for all the help/advice and patience with my depressive rants!! \n\nI'm in a new chapter of my life now so thanks. \n\nAnd secondly. \n\nI FUCKING HATE MY JOB", 'score': 66, 'username': 'al-m'}

dRS.getUserRant("<username>", <n>)  # Get the n'th most recent rant posted by <username>
# Example return data for these parameters: ("ewpratten", 1):
# {'text': 'I wonder..\n\nDo the new devduck capes say "devrant.com" on the back? Or do they still say "devrant.io"', 'score': 20, 'tags': ['devrant', 'i wonder'], 'id': 1600704}
```
More functions, data, and info will come soon.

## Example
This is an example script that gets every rant posted by a user (one at a time) and prints it to the screen:
```python
import devRantSimple ad dRS

username = "ewpratten

prevdata = ""
i = 0
while prevdata != dRS.InvalidResponse:
	prevdata = dRS.getUserRant(username, i)["text"]
	print(prevdata)
	i+=1
```
