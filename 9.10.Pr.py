with open("log.txt") as f:
    content=f.read()
    
    if 'Python' in content.lower():
        print("Yes Python is present")
    else:
        print("Yes Python is not present")