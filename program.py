# Setup
from os import environ, path

ACCOUNT_URI = environ['ACCOUNT_URI']
ACCOUNT_KEY = environ['ACCOUNT_KEY']
TITANIC_DATA_FILE = path.expanduser('~/usability/data/titanic.json')

# 1) Connect to the Azure Cosmos SQL DB account using the ACCOUNT_KEY and ACCOUNT_URI retreived above

# 2) Create a new database named 'uxstudy'

# 3) create a new container named 'titanic' in the database 'uxstudy'

# 4) Upload each of the items in the titanic dataset into the titanic container

import json
with open(TITANIC_DATA_FILE, 'r') as f:
    data = json.load(f)

for item in data:
    # Ensure that each item is in the collection
    pass

# Interlude: Go to the portal and look at the uploaded data...

# 5) Execute a query that returns all passengers that do not have a registered age,
#    and print the result.
#
#    You can use the following Azure Cosmos DB SQL Query:
#
#       SELECT * FROM passenger WHERE passenger.age = ''
#


# 6) Delete all items that do not have a registered age (returned in step #5) from the container

# 7) Find the average age for passengers that survived from first class
#
# You can use the following parameterized query 
#       SELECT * from passenger WHERE passenger.pclass=@class AND passenger.survived=1
#


# 8) Update/add a boolean attribute 'younger' to each item indicating if the person was younger or older than the average survivor for first class

