store=[("Shirt",20.00),
       ("Pants",25.00),
       ("Jackets",50.00),
       ("Socks",10.00)]

to_euros = lambda data:(data[0],data[1]*0.82)
to_dollar = lambda data:(data[0],data[1]/0.82)
store_dollars = list((map(to_dollar,store)))
for i in store_dollars:
   print (i)