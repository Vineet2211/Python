from lib2to3.pytree import LeafPattern


st="This is a String with Double  spaces"
doublespaces=st.find("  ")
print(doublespaces)

#New Programme
st="This is a String with Double  spaces ok"
st=st.replace("  ","  ")
print(st)

#New Programme
letter="Dear Vineet,This Universe is very Nice! Thanks!"
print(letter)

formatted_letter="Dear Vineet,\n\tThis Universe is Nice!\nThanks!"
print(formatted_letter)