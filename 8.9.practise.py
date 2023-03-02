def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
this="    Vineet is Good    "
n=remove_and_split(this,"Vineet")
print(n)
#print(this)
#print(this.strip())