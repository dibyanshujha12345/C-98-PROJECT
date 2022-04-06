
# data_a=open("sample1.txt","r")
# data_a=open("sample2.txt","r")

# data_c=open("sample1.txt","w")
# data_d=open("sample2.txt","w")

File1=input("Enter the name of 1st File to swap")
File2=input("Enter the name of 2nd file to swap")

with open(File1,'r') as a:
    data_a=a.read()

with open(File2,'r') as b:
    data_b=b.read()



with open(File1,'w') as a:
    a.write(data_b)    

with open(File2,'w') as b:
    b.write(data_a) 