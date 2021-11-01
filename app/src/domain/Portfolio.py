class Portfolio():
    # create a class that mimics the database table: portfolio

    def __init__(self, ticker:str, quantity:int, purchase_price:float, account_id:int = -1):
        self.account_id = account_id
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.ticker = ticker