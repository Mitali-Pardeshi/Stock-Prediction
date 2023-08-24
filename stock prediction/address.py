book = {}
book["tom"] = {
    "name":"tom",
    "address":"gurudatta nagar",
    "phone": 9876544356
}

book["bob"] = {
    "name":"bob",
    "address":"kalpataru",
    "phone":9265341657
}

import json
s=json.dumps(book) #dumps s=string
with open("c://data//book.txt","w") as f:
    f.write(s)

f=open("c://data//book.txt","r")
s=f.read()
print(s)

import json
book = json.loads(s)
print(book)