# Setup
from os import environ, path

ACCOUNT_URI = environ['ACCOUNT_URI']
ACCOUNT_KEY = environ['ACCOUNT_KEY']
TITANIC_DATA_FILE = path.expanduser('~/usability/data/titanic.json')

# Connect to the Azure Cosmos SQL DB account

from azure.cosmos.cosmos_client import CosmosClient
from azure.cosmos.errors import HTTPFailure
client = CosmosClient(url_connection=ACCOUNT_URI, auth=dict(masterKey=ACCOUNT_KEY))

# Create a new database named 'uxstudy'

try:
    database = client.CreateDatabase(dict(id='uxstudy'))
except HTTPFailure:
    database = client.ReadDatabase('dbs/uxstudy')

# create a new container named 'titanic'

try:
    container = client.CreateContainer(database_link=database['_self'], collection=dict(id='titanic'))
except HTTPFailure:
    database_link = 'dbs/uxstudy/'
    container = client.ReadContainer(f'{database_link}colls/titanic')

# Upload each of the items in the titanic dataset into the titanic container

import json
with open(TITANIC_DATA_FILE, 'r') as f:
    data = json.load(f)

for item in data:
    client.CreateItem(database_or_Container_link=container['_self'], document=item)

# Find and delete all passengers that do not have a registered age

items = client.QueryItems(database_or_Container_link=container['_self'], query="SELECT * FROM passenger WHERE passenger.age = ''")
for item in items:
    client.DeleteItem(item['_self'])

# Find the average age for passengers that survived from first class, excluding any 
# passengers where age is unknown
#
items = list(client.QueryItems(database_or_Container_link=container['_self'], query=dict(query="SELECT * from passenger WHERE passenger.pclass=@class AND passenger.survived=1",
    parameters=[
        {'name': '@class', 'value': 1}
])))

average_age = sum([item['age'] for item in items]) / len(items)

print(f'Average age is: {average_age}')

# Update/add an attribute to each item indicating if the person was younger or older than the average survivor for first class
for item in client.ReadItems(collection_link=container['_self']):
    item['olderThanAverageSurvivorFirstClass'] = None if item['age'] == '' else (item['age'] > average_age)
    client.UpsertItem(database_or_Container_link=container['_self'], document=item)
