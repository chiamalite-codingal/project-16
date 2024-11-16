test =  {'Codingal' : 3, 'is' : 3, 'best' : 3, 'for' : 3, 'Coding' : 2}
print("The original dict is:",test)
x = 3
count = 0
for key in test:
    if test[key] == x:
        count = count+1
print("Frequency is:",count)