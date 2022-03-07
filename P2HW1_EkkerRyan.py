#This program is a shopping calculator, taking in at least 5 individual items
#then giving you a subtotal, sales tax, and overal total
#March 7, 2021
#CTI-110 P2HW1- Total Purchases
#Ryan Ekker

#Display 'Enter the price of item #1: '
#input item 1
#Display 'Enter the price of item #2: '
#input item 2
#Display 'Enter the price of item #3: '
#input item 3
#Display 'Enter the price of item #4: '
#input item 4
#Display 'Enter the price of item #5: '
#input item 5
#Set Subtotal = items 1-5 added together
#Set Sales_tax = subtotal *(7/100), rounded up to the 2nd decimal place
#Set Total = Subtotal + Sales_tax
#print '-------Results-------'
#print 'Subtotal', Subtotal
#print 'Sales Tax', Sales_tax
#print 'Total', total

#User inputs 5 items theyre purchasing
item_1 = float(input('Enter the price of item #1: '))
item_2 = float(input('Enter the price of item #2: '))
item_3 = float(input('Enter the price of item #3: '))
item_4 = float(input('Enter the price of item #4: '))
item_5 = float(input('Enter the price of item #5: '))

#Math calculations for subtotal, tax amount, and total amount
Subtotal = round(item_1 + item_2 + item_3 + item_4 + item_5,2)
Sales_tax = round(Subtotal *(7/100), 2)
Total = round(Subtotal + Sales_tax,2)

print('-------Results-------')
print('Subtotal:', Subtotal)
print('Sales tax:', Sales_tax)
print('Total:', Total)
