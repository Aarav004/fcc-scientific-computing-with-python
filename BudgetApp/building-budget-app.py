class Category:   
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.amount = 0
        self.initial_deposit_done = False
    
    def deposit(self, amount, description=""):    
        self.amount += amount
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if amount <= self.amount:
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False 
    
    def get_balance(self):
        return self.amount
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self,amount):
        if amount > self.amount:
            return False
        else:
            return True

    def __str__(self):
        transactions = ""
        title = self.name.center(30 ,'*') + '\n'
        for entry in self.ledger:
            description = entry['description'][:23]
            amount = entry['amount']
            transactions += f"{description:<23}{amount:>7.2f}\n"
        footer = f"Total: {self.get_balance():.2f}"

        return title + transactions + footer





def create_spend_chart(categories):
    with_dict = {}
    total = 0
    for category in categories:
        sumt = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                sumt += abs(transaction["amount"])

        total += sumt
        with_dict[category.name] = sumt
    for category in with_dict:
        with_dict[category] = int((with_dict[category] / total) * 100)

    
    chart_title = "Percentage spent by category\n"
    chart =""

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"

        for percent in with_dict.values():
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"
        bar_chart = chart_title + chart.rstrip('\n')
    

    return(bar_chart)
        


        




