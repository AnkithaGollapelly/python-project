from datetime import datetime
Name=input('Enter your name:')
#list of items available in supermarket for knowning purpose
list='''
Milk                 Rs 55/L
Comb                 Rs 15/each
Water Bottle         Rs 30/each
Tomatoes             Rs 22/kg
Comfort              Rs 60/L
Broom Sticks         Rs 50/each
Wheat Flour(aatta)   Rs 98/kg
Ghee                 Rs 76/200g
pulses               Rs 32/500g 
Salt                 Rs 40/500g
Blankets             Rs 110/each
Study Table          Rs 300/each
Water Colors         Rs 60/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
itemslist=[]
quantitylist=[]
pricelist2=[]
#rates for items
items={
'Milk':50,
'Comb':15,
'Water Bottle':30,
'Tomatoes':22,
'Comfort':60,
'Broom Sticks':50,
'Wheat Flour(aatta)':98,
'Ghee':76,
'pulses':32, 
'Salt':40,
'Blankets':110,
'Study Table':300,
'Water Colors':60}
option=int(input('for list of options enter 1:'))
if option==1:#display of list
   print(list)
for i in range(len(items)):
   inp1=int(input('if you want to buy enter 1,if no need enter 2:'))
   if inp1==2:
       break
   if inp1==1:
     item=input('enter your items:')
     quantity=int(input('enter quantity:'))
     if item in items.keys():
        price=quantity*(items[item])#single item cost
        pricelist.append((item,quantity,items,price))#append takes as a single argument
        totalprice+=price#total amount that you shopped
        itemslist.append(item)
        quantitylist.append(quantity)
        pricelist2.append(price)
        gst=(totalprice*5)/100 # gst amount
        finalprice=gst+totalprice
     else:
      print('sorry you entered item is not available')
   else:
      print('you entered number is invalid')
   inp2=input('can i bill the items yes,if not no:')
   if inp2=='yes':
      pass 
      if finalprice!=0:
          print(40*' ','VISHAL SUPERMARKET',40*' ')
          print(40*' ','MARUTHINAGAR,KARIMNAGAR,NEAR KHAMAN',40*' ')
          print(40*' ','CONTACT NO:','XXXXXXXXXX',40*' ')
          print(110*'*')
          print(110*'*')
          print('cashier',90*' ','#1')
          print('manager',90*' ','Ankitha')
          print(110*'*')
          print(110*'*')
          print('Name:',Name,30*' ','Date:',datetime.now())
          print('SNO',8*' ','items',10*' ','quantity',3*' ','price')
          for i in range(len(pricelist)):
            print(i,10*' ',itemslist[i],14*' ',quantitylist[i],10*' ',pricelist2[i])
          print(50*' ','Total Amount:','Rs',finalprice)
          print(50*' ','GST Amount',gst)
          print(90*'-')
          print(50*' ','Final Amount',finalprice)
          print(100*' ')
          print(75*' ','Thanks For Visting')



