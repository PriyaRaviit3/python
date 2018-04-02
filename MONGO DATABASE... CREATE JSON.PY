mongo database .... create json




show dbs
admin       0.000GB
config      0.000GB
local       0.000GB
mydatabase  0.000GB
> use firstdatabase
switched to db firstdatabase
> db.demodb.insert({"Name":"Priya","Place":"Sankari","Quali":"MCA"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin          0.000GB
config         0.000GB
firstdatabase  0.000GB
local          0.000GB
mydatabase     0.000GB
db.demodb.insert({"Name":"Migen","Place":"Sankari","Quali":"MCA"})
WriteResult({ "nInserted" : 1 })
> db.demodb.insert({"Name":"Bavyaa","Place":"Sankari","Quali":"MCA"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin          0.000GB
config         0.000GB
firstdatabase  0.000GB
local          0.000GB
mydatabase     0.000GB
> db.demodb
firstdatabase.demodb
> db.demodb.find().pretty()
{
        "_id" : ObjectId("5ac1de1e8b476cffa046b663"),
        "Name" : "Priya",
        "Place" : "Sankari",
        "Quali" : "MCA"
}
{
        "_id" : ObjectId("5ac1e1c28b476cffa046b664"),
        "Name" : "Migen",
        "Place" : "Sankari",
        "Quali" : "MCA"
}
{
        "_id" : ObjectId("5ac1e1d08b476cffa046b665"),
        "Name" : "Bavyaa",
        "Place" : "Sankari",
        "Quali" : "MCA"
}