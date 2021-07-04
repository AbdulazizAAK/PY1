__author__ = "Galvanize_DSDE"


# declare variables
#sales = 150
sales = input("\nEnter total sales:")
print("Input data type is string = {}".format(isinstance(sales,str)))

# input validation
if not sales.isnumeric():
    raise Exception("The input entered should be numeric")

sales = float(sales)

average_price = 2100
cogs_percentage = 0.59

# gross revenue
annual_gross_revenue = sales * average_price
quarterly_gross_revenue = annual_gross_revenue / 4.0
monthly_gross_revenue = annual_gross_revenue / 12.0

# net revenue
cogs = annual_gross_revenue * cogs_percentage
annual_net_revenue = annual_gross_revenue - cogs
quarterly_net_revenue = annual_net_revenue / 4.0
monthly_net_revenue = annual_net_revenue / 12.0

# print summary
print("\n")
print("-"*30)
print("Total sales: {}".format(sales))
print("Average price: {}".format(average_price))
print("COGS %: {}".format(cogs_percentage))
print("COGS: {}".format(cogs))
print("-"*30)

print("-"*30)
print("Gross Revenue")
print("..... annual: ${:.2f}".format(annual_gross_revenue))
print(".. quarterly: ${:.2f}".format(quarterly_gross_revenue))
print(".... monthly: ${:.2f}".format(monthly_gross_revenue))
print("-"*30)

print("-"*30)
print("Net Revenue")
print("..... annual: ${:.2f}".format(annual_net_revenue))
print(".. quarterly: ${:.2f}".format(quarterly_net_revenue))
print(".... monthly: ${:.2f}".format(monthly_net_revenue))
print("-"*30)