my_file=open("data.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
for data in my_file:
    if "delhi" in data:
        file1.write(data)
    elif "shimla"in data:
        file2.write(data)
    else:
        file3.write(data)
file1.close()
file2.close()
file3.close()
file1=open("delhi.txt","r")
files=file1.read()
print(files)
