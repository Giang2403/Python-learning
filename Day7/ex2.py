"""
2
a) Take the value of following keys: album_name, release_year by 2 ways
b) Change the value of key release_year: 1973->1971
c) Delete the key track_list
d) Add new key: amount = 2000 by 2 ways
e) Empty dict album_infor
"""
import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any colour you like",
        "Brain Damage",
        "Eclipse"
    ]
}

#a
print(album_info["album_name"])
print(album_info.get("album_name"))
print(album_info["release_year"])
print(album_info.get("release_year"))

#b
album_info["release_year"] = 1971
print(json.dumps(album_info, indent = 4))

#c
album_info.pop("track_list")
print(json.dumps(album_info, indent=4))

#d
album_info.update(amount = 2000)
print(json.dumps(album_info, indent=4))
up = {
    "amount2" : 4000
}
album_info.update(up)
print(json.dumps(album_info, indent=4))

up2 = [("amount3", 5000)]
album_info.update(up2)
print(json.dumps(album_info, indent=4))

album_info.clear()
print(album_info)