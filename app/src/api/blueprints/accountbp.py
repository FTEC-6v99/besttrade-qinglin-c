import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Account import Account

accountbp = Blueprint('account', __name__, url_prefix='/account')

@accountbp.route('/get-all-accounts', methods = ['GET'])
def get_all_accounts():
    try:
        account = dao.get_all_accounts()
        if account is None:
            return json.dumps([]), 200
        else:
            return json.dumps(account.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/get-account-by-account_number/<account_number>', methods = ['GET'])
def get_account_by_account_number(account_number:int) -> Account:
    try:
        account = dao.get_account_by_account_number(account_number)
        if account is None:
            return json.dumps([]), 200
        else:
            return json.dumps(account.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/get-accounts-by-investor_id/<investor_id>', methods = ['GET'])
def get_accounts_by_investor_id(investor_id:int) -> Account:
    try:
        account = dao.get_accounts_by_investor_id(investor_id)
        if account is None:
            return json.dumps([]), 200
        else:
            return json.dumps(account.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/delete-accounts/<id>', methods = ['DELETE'])
def delete_account(id):
    try:
        dao.delete_account(id)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/update-acct-balance/<id>/<balance>', methods = ['PUT'])
def update_acct_balance(id: int, bal: float) -> None:
    try:
        dao.update_acct_balance(id, bal)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/create-account/<investor_id>/<balance>', methods = ['POST'])
def create_account(investor_id, balance):
    try:
        account = Account(investor_id, balance)
        dao.create_account(account)
        return json.dumps(account.__dict__)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500