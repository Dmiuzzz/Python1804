fin_data = [int(input("Enter revenue")),
           int(input("Enter costs")), int(input("Enter the number of employees"))]
fin_res = fin_data[0] - fin_data[1]
if  fin_res > 0:
    print('Profit')
    print('Profitability of revenue = ', fin_res / fin_data[0])
    print("The company's profit per employee = ", fin_data[0] / fin_data[2])
else:
    print('Loss')