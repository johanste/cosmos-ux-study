# Setup
from os import environ, path

ACCOUNT_URI = environ['ACCOUNT_URI']
ACCOUNT_KEY = environ['ACCOUNT_KEY']
TITANIC_DATA_FILE = path.expanduser('~/usability/data/titanic.json')

# 1) Connect to the Azure Cosmos SQL DB account using the ACCOUNT_KEY and ACCOUNT_URI retreived above

# 2) Create a new database named 'uxstudy'

# 3) create a new container named 'titanic' in the database 'uxstudy'

# 4) Upload each of the items in the titanic dataset into the titanic container
def upload_data():
    """ Upload (insert) all the data into the Azure Cosmos SQL DB Container
    """
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
def get_passengers_with_no_age():
    """ Query for all passengers where the age is missing (age is set to an empty string)
    """
    pass

# 6) Delete all items that do not have a registered age (returned in step #5) from the container
def delete_passengers_with_no_age():
    """ Cleans up the data in the container by deleting all passengers that have no
    known age (age set to an empty string)
    """
    pass

# 7) Find the average age for passengers that survived from first class
#
# You can use the following parameterized query 
#       SELECT * from passenger WHERE passenger.pclass=@class AND passenger.survived=1
#
def compute_average_age(passenger_class=1):
    """ Query for and compute the average age for each of the surviving passengers in the given 
    class
    """
    pass

# 8) Update/add a boolean attribute 'younger' to each item indicating if the person was younger or older than the average survivor for first class
def augment_data():
    """ Update each passenger with a new boolean property 'younger' indicating if the 
    passenger was younger or older than the average age of first class surviving passengers
    """
    pass