import json
#data is a dictionary
data = ''' {  
"name" : "Chuck",
"phone" : {
	"type" : "intl",
	"number" : "+1 361 522 1839"
},
"email" : {
	"hide" : "yes"
}
}'''

info = json.loads(data) #json.loads creates a list. in this case it would be list of dictionary
print('Name : ', info["name"])
print('Hide :', info["email"]["hide"])


# Example 2
import json
#input is a list of dictionary
input = ''' [
	{ "id" : "001",
	  "x" : "2",
	  "name" : "Chuck"
	},
	{
	  "id" : "009",
	  "x" : "7",
	  "name" : "Pari"
	}
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
	print('Name:', item["name"])
	print('Id :', item["id"])
	print('Attribute:', item["x"])
