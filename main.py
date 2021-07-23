# JSON JavaScript Object Notation

equivalent = """
Python 	JSON

dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
"""
# datetime için str kullan
# load -> from file
# loads -> from str
# dump -> to file
# dumps -> to str

import json
from random import randint, choice
from datetime import datetime

status = [True, False, None]

str_json = """
{
  "markers": [
    {
      "name": "Google, 8th Avenue",
      "position": [40.7414728,-74.0055813]
    },
    {
      "name": "Microsoft, Times Square",
      "location": [40.7565323,-73.9904037]
    },
    {
      "name": "Tesla, Washington Street",
      "location": [40.7411595,-74.0097167]    
    },
    {
      "name": "Amazon New York",
      "location": [40.7532822,-74.0010696]
    }
  ]
}"""

data = json.loads(str_json)
# print(type(data))
# print(data["markers"][0]["name"])  # Google, 8th Avenue

for item in data["markers"]:
    print(item["name"])
    # for delete item
    # del item["name"]  # key ve value siler

    # Add Key: Value
    item["is_gigantic"]=choice(status)
    item["id"]=randint(1,3 ** 8)
    item["unic"]="öişğü"
    item["now"]=datetime.now().strftime("%d/%m,%y %H:%M:%S")

new_json = json.dumps(data, indent=2)
# indendt 2: printte tek satırda olamaması için

print(data)

print(new_json)  # tr karakterler unicode olarak gözükse de geriye loads yaparsan otomatik çevirilirler ;)
print(json.loads(new_json))
# py objesinden json yaptığında unicode codu olarak gözükenler, loads methodundan sonra normal karaktere dönüşür


# dosyalama 
with open("new_json_data.json", "w") as file:
    json.dump(data, file, indent=2)

# dosyadan okuma
with open("raw_json.json", "r") as file:
    readed = json.load(file)

print(readed)
