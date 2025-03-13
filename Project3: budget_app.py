class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.category}")
            other.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        result = f"{self.category:*^30}" + '\n'
        for item in self.ledger:
            current =  f"{item['description']:.23}"
            result += current
            result += f"{item['amount']:>7.2f}".rjust(30 - len(current))
            result += '\n'
        result += f"Total: {self.get_balance()}"
        return result


def create_spend_chart(categories):
    def get_withdrawals(category):
        return sum(item["amount"] for item in category.ledger if item["amount"] < 0)
    
    total_spent = sum(get_withdrawals(cat) for cat in categories)
    percentages = [int((get_withdrawals(cat) / total_spent) * 100) // 10 * 10 for cat in categories]
    
    answer = "Percentage spent by category\n"
    for percentage in range(100, -1, -10):
        answer += f"{str(percentage).rjust(3)}| "
        for percent in percentages:
            answer += "o  " if percent >= percentage else "   "
        answer += "\n"
    
    answer += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_length = max(len(cat.category) for cat in categories)
    
    for i in range(max_length):
        answer += "     "
        for cat in categories:
            answer += (cat.category[i] + "  ") if i < len(cat.category) else "   "
        answer += "\n" if i < max_length - 1 else ""
    
    return answer



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))
