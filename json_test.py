import json

my_dict = {
	"averages" : {
		"16570": 12000,
		"BLNR": 16000
	},
	"minimum" : 9000
}

# Serializing json
json_object = json.dumps(my_dict, indent=4)

print(json_object)
# print(type(json_object))
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object2 = json.load(openfile)
 
print(json_object2)
print(type(json_object2))
print(json_object2["averages"]["16570"])