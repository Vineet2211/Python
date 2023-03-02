# Use open function to read the content of file!
# f=open('sample.txt','r') 
f=open('sample.txt') #By default the mode is 'r'
# data=f.read()
data=f.read()
#data=f.read(5) #Reads first 5 charcter in the File
print(data)
f.close()