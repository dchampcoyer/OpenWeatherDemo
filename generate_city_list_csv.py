import json

def jprint(jdict):
	print jdict["id"],jdict["country"],jdict["name"]
def cprint(aoft):
	for i in aoft:
		print i[0],"\t",i[1]

data = json.load(open("city.list.json"))

cdict = {}

print "adding data to dictionary..."
for i in data:
	if cdict.has_key(i["country"]):
		cdict[i["country"]].append((i["id"],i["name"],i["coord"]["lat"],i["coord"]["lon"]))
	else:
		cdict[i["country"]]=[(i["id"],i["name"],i["coord"]["lat"],i["coord"]["lon"])]
print "sorting individual dictionarys..."
for i in cdict:
	cdict[i].sort()

keylist = cdict.keys()

f = open("city.list.csv","r+")
print "writing to file..."
for key in keylist:
	print "\t",key
	for i in cdict[key]:
		writestring = ",".join(map(unicode,[key,i[0],i[1],i[2],i[3]]))+"\n"
		f.write(writestring.encode('utf8'))

f.close()

