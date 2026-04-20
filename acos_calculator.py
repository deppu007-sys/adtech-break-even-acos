# AdTech Break-Even ACoS Calculator

class ACOSCalculator:

    # Calculate profit margin %
    def profit_margin(self, selling_price, cost_price):
        profit = selling_price - cost_price
        margin = (profit / selling_price) * 100
        return round(margin, 2)

    # Break-even ACoS = Profit Margin %
    def break_even_acos(self, selling_price, cost_price):
        return self.profit_margin(selling_price, cost_price)

    # Check profitability
    def check_profit(self, acos, break_even_acos):
        if acos < break_even_acos:
            return "Profit"
        elif acos == break_even_acos:
            return "Break-Even"
        else:
            return "Loss"


# Example Usage
calc = ACOSCalculator()

selling_price = 1000
cost_price = 700
current_acos = 25  # %

be_acos = calc.break_even_acos(selling_price, cost_price)

print("Break-Even ACoS:", be_acos, "%")
print("Current ACoS:", current_acos, "%")
print("Status:", calc.check_profit(current_acos, be_acos))
