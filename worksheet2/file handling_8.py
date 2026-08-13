with open("student.txt","r") as f:
    string=f.read()
print(string)  
count = 0
for name in string.splitlines(): #splitlines:converts the text into a list:
    count = count + 1

print("Total students:", count)
