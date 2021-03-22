my_file = open("people_exercise.txt","r")
file_data = my_file.read()
print (file_data)
counter=0
files=file_data.split("\n")
i=0
for i in files:
        counter=counter+1
print("Total lines =",counter)






# num=int(input("enter a num="))
# i=2
# while i<num:
#     count=0
#     j=2
#     while j<num:
#         num1=int(input("num="))
#         if num1%j==0:
#             count=count+1
#         j=j+1
#         if count==0:
#             print(num1,"prime number")
#         else:
#             print(num1,"not prime")
#     # i=i+1