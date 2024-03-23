usernames = ["Dude","Bro","Mister"]
passwords = ["P@ssword","abc123","Guest"]

user = dict(zip(usernames,passwords))

for key,value in user.items():
   print(key+":"+value)