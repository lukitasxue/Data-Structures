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
#arr[start : end (not inclued) : step]
array_test = [0,1,2,3,4,5,6,7,8,9]
# print(array_test[4:6])
print(array_test[:8])
# print(array_test[4:])
# print(array_test[:])
# print(array_test[0:7:2])
# print(array_test[-3:])
# print(array_test[::-1])

#sorting elements of an array:

array_sorting = [3,2,6,8,1,9,5,0,4,7]
array_sorting.sort() #modifies original list
print(array_sorting)

array_sorting = [3,2,6,8,1,9,5,0,4,7] 
print(array_sorting)
new_array = sorted(array_sorting) # returns a new sorted list w/o modifiying the original
print(new_array)

new_array_reverse = sorted(array_sorting, reverse=True)
print(new_array_reverse)
 
# sort strings
arr = ["apple", "banana", "kiwi", "grape"]
arr.sort(key=len)  # Sort by string length
print(arr)


# Hello world
# git init
# git remote add origin link
# git add.
# git commit -m "dscrpt"
# git push origin master
# git status

#testing 