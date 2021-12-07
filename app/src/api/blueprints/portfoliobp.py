import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Portfolio import Portfolio

portfoliobp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@portfoliobp.route('/get-all-portfolios', methods = ['GET'])
def get_all_portfolios():
    try:
        portfolio = dao.get_all_portfolios()
        if portfolio is None:
            return json.dumps([]), 200
        else:
            return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/get-portfolios-by-acct_id/<account_id>', methods = ['GET'])
def get_porfolios_by_acct_id(acct_id: int) -> Portfolio:
    try:
        portfolio = dao.get_portfolios_by_acct_id(acct_id)
        if portfolio is None:
            return json.dumps([]), 200
        else:
            return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/get-portfolios-by-investor-id/<investor_id>', methods = ['GET'])
def get_portfolios_by_investor_id(investor_id:int) -> Portfolio:
    try:
        portfolio = dao.get_portfolios_by_investor_id(investor_id)
        if portfolio is None:
            return json.dumps([]), 200
        else:
            return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/delete-account/<account_id>/<ticker>', methods = ['DELETE'])
def delete_portfolio(account_id, ticker):
    try:
        dao.delete_portfolio(account_id, ticker)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/buy-stock/<account_number>/<ticker>/<quantity>/<price>', methods = ['PUT'])
def buy_stock(ticker: str, price: float, quantity: int, account_number: int):
    portfolio = Portfolio(account_number, ticker, quantity, price)
    try:
        dao.buy_stock(portfolio)
        return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/sell-stock/<account_number>/<ticker>/<quantity>/<sale_price>', methods = ['PUT'])
def sell_stock(ticker: str, quantity: int, sale_price: float, account_number: int, balance: float):
    portfolio = Portfolio(account_number,ticker,quantity, sale_price)
    try:
        dao.sell_stock(portfolio)
        return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500
