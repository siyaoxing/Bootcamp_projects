menu = ['croissant', 'coffee', 'tea', 'porridge'] #list of menu items 

stock = {'croissant':4, 'coffee': 10, 'tea': 12, 'porridge':8} #dictionary of stock levels

price = {'croissant':1.99, 'coffee':2.20, 'tea':1.50, 'porridge':3.00} #dictionary of prices

total_stock = 0

#iterate through each menu items in for loop, for range(length of menu)
for i in range(len(menu)):
    print(menu[i])
    #access item's value in the stock and price dictionary using menu[i] as the key
    #save as new variables and print out summary
    stock_item = stock[menu[i]] 
    price_item = price[menu[i]]
    print(f"\tStock: {stock_item}\n\tPrice: £{price_item}")
    #calculate total value of each item by multiplying stock and price 
    item_value = stock[menu[i]]*price[menu[i]]
    #Add to total_stock variable as a running total 
    total_stock += item_value

# round value to 2 decimals and print out final result 
assets = round(total_stock,2)

print(f"Total value of current assets is: £{assets}")



    
