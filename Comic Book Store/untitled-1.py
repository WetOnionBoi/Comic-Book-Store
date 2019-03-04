    #Ver 1.1 Created test data for ticket variable and added server functionality
        

from bottle import run, route, view, get, post, request
from itertools import count


class Comic:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__(self, comic_name, Comic_stock):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_stock = stock



    #Test Data
comics  = [
          Comic("Super Dude", 8),
          Comic("Lizard Man",  12),
          Comic("Water Woman", 3)
          ]


#bottom of code
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)