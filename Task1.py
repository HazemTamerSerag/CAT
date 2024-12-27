list = [10, 20, 23, 45, 96, 10, 21, 22, 21]

clearlist = []
for i in list:
    if i not in clearlist:
        clearlist.append(i)

print(clearlist)
clearlist.reverse()
print(clearlist)