arr = [10,20,30,40,50]

# add value at index, number
arr.insert(1,15)

# delete values from array
# arr.pop(3)
# arr.remove(10)
# del arr[0]
arr.remove(15)

print(f"Numbers: ", arr)

# search for number with if statement
if 30 in arr:
    print("30 in array")
else:
    print("not in array")

index = arr.index(30) #finds index for 30
print(index)

element = 50
found = False

for i in range(len(arr)):
    if arr[i] == element:
        print("found!")
        found = True
        break

if not found:
    print(f"not found {element}")


#slice parts of an array:
#arr[start : end : step]





# Hello world
# git init
# git remote add origin link
# git add.
# git commit -m "dscrpt"
# git push origin master
# git status

#testing 