# while(True):
#     print("press q to quit")
#     a=input("Enter a number: ")
#     if a=='q': 
#         break
#     try:
#         print("trying....")
#         a=int(a)
#         if a > 6:
#             print("you entered number is gretter that 6...")
    
#     except Exception as e:
#         print(f"you entered value is wrong...{e}")

# print("thanks for playing....")







# while(True):
#     print("enter q for quite..!!")
#     a=input("Enter a number :")
#     if a=="q":
#         break
        
#     try:
#         a=float(a)
#         c=2/a
#         print(f"answer:{c}")
#     except ValueError as e:
#         print(f"enter the numbers only...!! exeption 1 is working...")
#     except ZeroDivisionError as e:
#         print(f"enter the numbers only...!!exeption 2 is working...")
#     except Exception as e:
#         print(" error got{e}")
# print("thank you for playing this game...!!")





# while(True):
#     try:
#         i=int(input("enter a number :"))
#         b=2+i
#         print(b)
#     except Exception as e:
#         print(e)
#     else:
#         print("run successfully...!!!")





# while(True):
#     try:
#         i=int(input("enter a number :"))
#         b=2+i
#         print(b)
#     except Exception as e:
#         print(e)
#     finally:                                    #its run always if try is success or except is success..
#         print("run successfully...!!!")






# list1=[1,35,44,"aadi", False,"bandhane"]

# for index,item in enumerate(list1):
#     print(index,item)




# a=[1,5,8,2,88,7,77,55,9,1459,1588]

# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)




# # print 3rd ,5th and 7th element into the list
# l=[1,2,3,4,5,6,7,8,9]

# for index,item in enumerate(l):
#     if index == 2 or index == 4 or index == 6:
#         print(index + 1,item)



# make tables of numbers..

# while(True):
#     num = int(input("enter a number:"))
#     table =[]
#     for i in range(1,11):
#         new=num * i
#         table.append(new)
#     print(table)



#save tables in different file..

# while(True):
#     num = int(input("enter a number:"))
#     table =[]
#     for i in range(1,11):
#         new=num * i
#         table.append(new)
#     print(table)
#     with open("tables.txt","a") as f:
#         f.write(str(table))
#         f.write("\n")


# #join function

# l=["Aaditya","kunal","manoj","Akshay","ritesh"]

# sentence=' and '.join(l)
# print(sentence)




# #filter function

# def greater_than_10(num):
#     if num>10:
#         return True
#     else:
#         return False

# # using lambda functions

# greater_than_25= lambda num : num >25

# lst=[1,2,6,52,85,6,54,24,10]

# print(list(filter(greater_than_10,lst)))
# print(list(filter(greater_than_25,lst)))



# from functools import reduce

# sum= lambda a,b:a+b

# l=[1,2,3,4,5]
# value=reduce(sum,l)
# print(value)




# name=input("enter your name:")
# marks=input("enter your marks:")
# phone=input("enter your phone no :")

# info=(f"my name is {name} and i got {marks}% in 12th standerd, my phone no. is {phone}")
# print(info)



# l=[1,5,2,3,6,5,22,5,66,222,55,5,66,90]

# a=filter(lambda a : a%5==0,l)
# print(list(a))



