from nsetools import Nse
nse = Nse()

#api doc http://nsetools.readthedocs.io/en/latest/
all_stock_codes = nse.get_stock_codes()
test = nse.get_quote(input("Enter NSE SYMBOL : "))

from pprint import pprint
#pprint (all_stock_codes)

#user input such as quantity and the price at which the stock was bought
qty = int(input("Enter Quantity Purchased : "))
user_price = float(input("Enter Price : "))

#calculating total price and current price
tot = qty * user_price
present_value = test['lastPrice'] * qty

#checking for profit or loss
if tot>present_value :
    difference = - (tot-present_value)

else :
    difference = + (present_value - tot)


#loop to generate lastprice traded and the symbol
for key in ['lastPrice', 'symbol']:
    print(test[key])
    
percentage = (difference/tot)*100
print("Quantity Purchased :" , qty)
print("Purchased at :" , user_price)

print("Total Price : %.2f" % tot)
print("Current Price :" , present_value)

print("Profit / Loss : %.2f" % difference)
print(percentage)
