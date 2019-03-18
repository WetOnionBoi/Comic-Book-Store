    #Ver 1.1 Created test data for comic store variable and added server functionality
        

from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Comic:

    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)

    def __init__(self, comic_name, image, comic_stock):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = comic_name
        self.image = image
        self.stock = comic_stock


    #Test Data
comics  = [
          Comic("Super-Dude","Superd.jpg", 8),
          Comic("Lizard-Man","lizard.jpg",  12),
          Comic("Water-Woman","Waterwoman.jpg", 3)
          ]




#index page
@route("/")
@view("index")
def index():
    #need this function to attach the decorators above.
    pass

@route('/sell_comics')
@view('sell_comics')
def sell_comics():
    data = dict (comics_list=comics)
    return data

@route('/buy_comics')
@view('buy_comics')
def buy_comics():
    pass

@route('/comic_bought', method = 'POST')
@view('comic_bought')
def comic_bought():
    pass

@route('/picture/<filename>')
def serve_picture(filename):
    return static_file(filename, root = './Images')




#bottom of code
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)