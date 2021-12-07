import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Investor import Investor

investorbp = Blueprint('investor', __name__, url_prefix= '/investor')

@investorbp.route('/get-investor-by-id/<id>', methods = ['GET'])
def get_investor_by_id(id: int) -> Investor:
    try:
        investor = dao.get_account_by_id(id)
        if investor is None:
            return json.dumps([]), 200
        else:
            return json.dumps(investor.__dict__), 200
    except Exception as e:
        return 'Oops an error occured: ' + str(e), 500

@investorbp.route('/get-all-investor', methods = ['GET'])
def get_all_investors():
    try:
        investor = dao.get_all_investor()
        if investor is None:
            return json.dumps([]), 200
        else:
            return json.dumps(investor.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/get-investor-by-name/<name>', methods = ['GET'])
def get_investor_by_name(name:str) -> Investor:
    try:
        investor = dao.get_investors_by_name(name)
        if investor is None:
            return json.dumps([]), 200
        else:
            return json.dumps(investor.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/create-investor/<name>/<status>', methods = ['POST'])
def create_investor(name, status):
    try:
        investor = Investor(name, status)
        dao.create_investor(investor)
        return  json.dumps(investor.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/delete-investor/<id>', methods= ['DELETE'])
def delete_investor(id):
    try:
        dao.delete_investor(id)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/update-investor-name/<id>/<name>', methods= ['PUT'])
def update_investor_name(id, name):
    try:
        dao.update_investor_name(id, name)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/update_investor_status/<id>/<status>', methods= ['PUT'])
def update_investor_status(id, status):
    try:
        dao.update_investor_status(id, status)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500
