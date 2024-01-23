dict = {
    "777": "Jesus",
    "666": "Oh hell, no",
    "1000": "10^3",
    "bool": False
}

dict["color"] = "orange"
dict.update({"weight": "50kg"})

dict.pop("777")
print(dict)

dict.popitem()
print(dict)

del dict["bool"]
print(dict)

dict.clear()
print(dict)