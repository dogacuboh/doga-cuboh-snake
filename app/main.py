import json
import os
import bottle
import time


from app.api import ping_response, start_response, move_response, end_response
from app.board import  update_board
from app.random_snake import random_move
from app.food_snake import food_move
from app.wall_snake import wall_move
from app.smart_snake import smart_move
from app.doga_snake import doga_move

snake_num = 0

@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='./static/')

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='./static/')


@bottle.post('/ping')
def ping():
    return ping_response()


@bottle.post('/start')
def start():
    game_state = bottle.request.json
    snake_colour = "#ff0000"
    return start_response(snake_colour)


@bottle.post('/move')
def move():
    game_state = bottle.request.json
    new_board = update_board(game_state)
    direction = ""

    direction = doga_move(game_state, new_board)
    return move_response(direction)


@bottle.post('/end')
def end():
    game_state = bottle.request.json
    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()


def is_input(temp):
  if not temp.isnumeric():
    return False
  if not len(temp)==1:
    return False 
  if int(temp)<1 or int(temp)>5:
    return False 
  return True


if __name__ == '__main__':
    snake_num = 5
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )

