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



