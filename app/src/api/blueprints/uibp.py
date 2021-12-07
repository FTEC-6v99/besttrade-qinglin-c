from flask import Blueprint

uibp = Blueprint('ui', __name__, url_prefix = '/ui')

@uibp.route('/', methods = ['GET'])
def main():
    return '<h1>Hello world<h1>'
