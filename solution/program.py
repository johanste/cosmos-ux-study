# Setup
from os import environ, path

ACCOUNT_URI = environ['ACCOUNT_URI']
ACCOUNT_KEY = environ['ACCOUNT_KEY']
TITANIC_DATA_FILE = path.expanduser('~/usability/data/titanic.json')

# Connect to the Azure Cosmos SQL DB account

from azure.cosmos import CosmosClient, HTTPFailure
client = CosmosClient(url=ACCOUNT_URI, key=ACCOUNT_KEY)

# Create a new database named 'uxstudy'

database = client.create_database('uxstudy')

# create a new container named 'titanic'

try:
    container = database.create_container('titanic')
except HTTPFailure:
    container = database.get_container('titanic')

# Upload each of the items in the titanic dataset into the titanic container

import json
with open(TITANIC_DATA_FILE, 'r') as f:
    data = json.load(f)

for item in data:
    container.create_item(item)

# Find all passengers that do not have a registered age

items = container.query_items("SELECT * FROM passenger WHERE passenger.age = ''")

# Find the average age for passengers that survived from first class, excluding any 
# passengers where age is unknown
#
items = list(container.query_items("SELECT * from passenger WHERE passenger.pclass=@class AND passenger.age != '' AND passenger.survived=1",
    parameters=[
        {'name': '@class', 'value': 1}
]))

average_age = sum([item['age'] for item in items]) / len(items)

print(f'Average age is: {average_age}')

# Update/add an attribute to each item indicating if the person was younger or older than the average survivor for first class
for item in container.list_items():
    item['olderThanAverageSurvivorFirstClass'] = None if item['age'] == '' else (item['age'] > average_age)
    container.upsert_item(item)
