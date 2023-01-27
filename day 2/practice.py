# List in list - printing specific element
'''
item1= ['car', 'bike', 'scooter']
item2= ['zomato', 'facebook', 'whatsapp']
item3= 'true'
list1= []
if item3 != []:
    item4= [item3]
    if list1 == []:
        list1.append(item4)
        list1.append(item2)
        list1.append(item1)
        for x in list1:
            for y in x:
                print(y)

'''
# Dictionary in list

l1= [{'1':'apple', '2':'banana', '3':'cherry'}, {'1':'maruti','2':'jaguar'}]
for x in l1:
    # print (x)
    y=x['2']
    print(y)




