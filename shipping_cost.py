"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

customer_basket_cost = 34 / 101
customer_basket_weight = 44
shipping_cost = 0
Total_cost = 0

# Write if statement here to calculate the total cost

if(customer_basket_cost >= 100):
  Total_cost = customer_basket_cost + shipping_cost
  print(Total_cost)
else:
  shipping_cost = customer_basket_weight * 1.20
  Total_cost = customer_basket_cost + shipping_cost
  print(Total_cost)