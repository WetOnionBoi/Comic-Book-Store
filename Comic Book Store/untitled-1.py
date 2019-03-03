    #Ver 1.1 Created test data for ticket variable and added server functionality
        

from bottle import run, route, view, get, post, request
from itertools import count


class Ticket:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__():
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = name
        self.email =  email
        self.dob = date_of_birth
        self.check_in = check_in




    #Test Data
tickets = [
          Ticket("Super Dude", 8),
          Ticket("Lizard Man",  12),
          Ticket("Water Woman", 3)
          ]

#Pages

#index page
@route("/")
@view("Index")
def index():
    pass


#bottom of code
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)