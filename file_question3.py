banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
f=open("file_question3.txt","w")
for i in banks_list:
    print(i)
    f.write(i)
    f.write("\n")
f.close()