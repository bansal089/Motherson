import re
from datetime import date
x= date.today()

y= f'"{x}"'

line1 = "we are currently working in motherson@2022"
final = re.sub("2022", y, line1)
line3= f'"{final}"'
line2= line3.replace(','')
print (line3)