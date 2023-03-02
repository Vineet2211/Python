f=open('poems.txt')
t=f.read()
if 'Twinkle' in t:
    print("Twinkle is Present")
else:
    print("Twinkle is not Present")
    f.close()