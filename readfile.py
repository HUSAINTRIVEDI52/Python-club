# # text="\nHello,Husain this side\nHow are you??"
# # # with open('text.txt','w')as file:
# # #     file.write(text)

# # with open('text.txt' ,'a') as file:
# #         file.write(text)

# with open('F:\\c language\\ar_smallest.c') as file:
#     print(file.read())
try:
    with open('F:\\c language\\ar_smallest.c') as file:
       print(file.read())
except FileNotFoundError:
             print("This file is not found!!")
            
             print(file.closed)