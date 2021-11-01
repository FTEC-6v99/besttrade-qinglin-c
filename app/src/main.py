import app.src.db.dao as dao
from app.src.domain.Investor import Investor

def main():
    """""
    investor = Investor('Adam Gold', 'Active')
    dao.create_investor(investor)
    investors = dao.get_all_investor()
    for investor in investors:
        print(f'{investor.name}')
"""
    accounts = dao.get_accounts_by_investor_id(1)
    for account in accounts:
        print(f'Acct no: {account.acct_no} - Balance: {account.balance} ')



if __name__ == '__main__' :
    main()