a= { "tobi":"name"}
b=dict(lathbrok="king",place="kategette")
c=dict(b)
print(c["place"])
print(c.keys())
print(a.values())
print(c.items())
print(list(a.items()))
print(type(list(a.items())[0]))
a["name"]="Floki"
print(a)
del a["tobi"]
print(a)
print(b.pop("place"))
b['edam']=b.pop("lathbrok")
print(b)

