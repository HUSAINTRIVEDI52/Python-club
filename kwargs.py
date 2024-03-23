def hello(**kwargs):
    # print("Hello"+" "+kwargs['first']+" "+kwargs['last'])
      print("Hello")
      for key,value in kwargs.items():
         print(value)

hello(first="Husain",middle="Trivedi",last="IS here")