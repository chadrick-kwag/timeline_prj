import csv, datetime
from pymongo import MongoClient

client = MongoClient("localhost:27017")

db = client.coronagov

print(db)


csvfile = "/home/chadrick/Documents/corona_gov.csv"


with open(csvfile, 'r') as fd:
    reader = csv.reader(fd)

    rows = list(reader)


rows = rows[2:]


for test in rows:
    splits = test[0].split('/')

    month, day, year = splits

    month = int(month)
    day = int(day)
    year = int("20" + year)

    datevar = datetime.datetime(year, month, day, 0,0)

    jsondata={
        'date': datevar,
        'title': test[1],
        'body': test[2],
        'ref': [test[3]]
    }

    result = db.events.insert_one(jsondata)

print(result)
