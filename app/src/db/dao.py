# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete
import typing as t
import mysql.connector
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection
import config
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio

def get_cnx() -> MySQLConnection:
    return connect(**config.dbparams)

'''
    Investor DAO functions
'''

def get_all_investor() -> list[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors

def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where id = %s'
    cursor.execute(sql, (id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        investor = Investor(row['name'], row['status'], row['id'])
        return investor 

def get_investors_by_name(name: str) -> list[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where name = %s'
    cursor.execute(sql, (name,))
    rows = cursor.fetchall()
    for row in rows:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors
    

def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()

def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s'
    cursor.execute(sql, (id,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set name = %s where id = %s'
    cursor.execute(sql, (id, name))
    db_cnx.commit()
    db_cnx.close()

def update_investor_status(id: int, status: str) -> None:
    '''
        Update the inestor status [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set status = %s where id = %s'
    cursor.execute(sql, (id, status))
    db_cnx.commit()
    db_cnx.close()

'''
    Account DAO functions
'''
def get_all_accounts() -> list[Account]:
    # Code goes here
    cnx = get_cnx()
    cur = cnx.cursor(Dictionary=True)
    cur.execute('Select investor_id, balance, account_number from account')
    rows = cur.fetchall()
    if len(rows) == 0:
        cnx.close()
        return []
    accounts = []
    for row in rows:
        accounts.append(
            Account(row['account_number'], row['investor_id'], row['balance'])
        )
    cnx.close()

def get_account_by_account_number(account_number: int) -> Account:
    # Code goes here
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        account = Account(row['account_number'], row['investor_id'], row['balance'])
        return account 


def get_accounts_by_investor_id(investor_id: int) -> list[Account]:
    db_cnx: MySQLConnection = get_cnx()
    cur = db_cnx.cursor(dictionary=True)
    sql = 'select * from account where investor_id = %s'
    cur.execute(sql, (investor_id,)) #rememeber a tuple of 1 needs an additional comma: (1) -> Not a tuple; (1,) -> a tuple
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    accounts = []
    for row in rows:
        accounts.append(Account(row['investor_id'], row['balance'], row['account_number']))
    db_cnx.close()
    return accounts

def delete_account(id: int) -> None:
    # Code goes here
    cnx = get_cnx()
    cur = cnx.cursor()
    sql = 'delete from account where investor_id = %s'
    cur.execute(sql, (id,))
    cnx.commit()
    cnx.close()

def update_acct_balance(id: int, bal: float) -> None:
    # Code goes here
    cnx = get_cnx()
    cur = cnx.cursor()
    sql = 'update account set balance = %s where id = %s'
    cur.execute(sql, (id, bal))
    cnx.commit()
    cnx.close()

def create_account(account: Account) -> None:
    # Code goes here
    cnx = get_cnx()
    cur = cnx.cursor()
    sql = 'insert into account (investor_id, balance) values (%s, %s)'
    cur.execute(sql, (account.investor_id, account.balance))
    cnx.commit()
    cnx.close()

'''
    Portfolio DAO functions
'''
def get_all_portfolios() -> list[Portfolio]:
    # code goes here
    portfolio: list[Portfolio] = []
    cnx = MySQLConnection = get_cnx()
    cur = cnx.cursor(dictionary=True)
    sql = str = 'select * form portfolio'
    cur.execute(sql)
    results: list[dict] = cur.fetchall()
    for row in results:
        portfolio.append(
            Portfolio(row['account_id'], row['ticker'], row['quantity'], row['purchase_price'])
            )
    cnx.close()
    return portfolio

def get_porfolios_by_acct_id(acct_id: int) -> list[Portfolio]:
    # code goes here
    portfolio: list[Portfolio] = []
    cnx = MySQLConnection = get_cnx()
    cur = cnx.cursor(dictionary=True)
    sql = str = 'select * form portfolio where acct_id = %s'
    cur.execute(sql, (acct_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    portfolio = []
    for row in rows:
        portfolio.append(
            Portfolio(row['account_id'], row['ticker'], row['quantity'], row['purchase_price'])
        )
    cnx.close()
    

def get_portfolios_by_investor_id(investor_id: int) -> list[Portfolio]:
    # code goes here
    portfolio: list[Portfolio] = []
    cnx = MySQLConnection = get_cnx()
    cur = cnx.cursor(dictionary=True)
    sql = str = 'select * form portfolio where investor_id = %s'
    cur.execute(sql, (investor_id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return []
    portfolio = []
    for row in rows:
        portfolio.append(
            Portfolio(row['account_id'], row['ticker'], row['quantity'], row['purchase_price'])
        )
    cnx.close()
    
    results: list[dict] = cur.fetchall()

def delete_portfolio(account_id: int, ticker:str) -> None:
    # code goes here
    cnx = get_cnx()
    cur = cnx.cursor()
    sql = 'delete from portfolio where account_id = %s and ticker = %s'
    cur.execute(sql, (account_id, ticker))
    cnx.commit()
    cnx.close()
    pass

def buy_stock(ticker: str, price: float, quantity: int, account_number: int) -> None:
    # code goes here
    cnx = get_cnx()
    cur = cnx.cursor()
    sql = 'buy stock where ticker = %s, where price = %s, where quantity = %s, where account_number = %s'
    cur.execute(sql)
    cnx.commit()
    cnx.close()

def sell_stock(ticker: str, quantity: int, sale_price: float, account_number: int, balance: float) -> None:
    # 1. update quantity in portfolio table
    # 2. update the account balance:
    # Example: 10 APPL shares at $1/share with account balance $100
    # event: sale of 2 shares for $2/share
    # output: 8 APPLE shares at $1/share with account balance = 100 + 2 * (12 - 10) = $104
    cnx = get_cnx()
    cur = cnx.cursor()
    buy_stock(ticker, sale_price, quantity, account_number)
    new_balance = balance + quantity * sale_price
    update_acct_balance(account_number, new_balance)
    sql = 'update balance is new_balance = %s, where balance = %s, where quantity = %s, wher sale_price is %s'
    cur.execute(sql, (ticker, quantity, sale_price, account_number, balance))
    cnx.commit()
    cnx.close()
