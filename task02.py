#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
data = req.text

# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

cafateria = json.loads(data)
for dayMenu in cafateria['menu']:
    print('\n')
    print(f"The date is {dayMenu['date']}")
    print(f"The soup of the day for {dayMenu['dayname']} is {dayMenu['soup']}")
    print(f"The short order for {dayMenu['dayname']} is {dayMenu['shortorder']}")
    print(f"The entree for {dayMenu['dayname']} is {dayMenu['entree']}")
    print(f"Notes for for {dayMenu['dayname']} are:\n{dayMenu['notes']}")