# myStr = input("Enter myString: ")
# myStr = "heititillo world"
myStr = "itiititi"
myStrLower = myStr.lower()
count = 0

for i in range(len(myStrLower)-2):
    if myStrLower[i:i+3]=="iti":
    # if myStrLower[i] == 'i':
    #     if myStrLower[i+1] == 't':
    #         if myStrLower[i+2] == 'i':
              count = count + 1 

print(count)


