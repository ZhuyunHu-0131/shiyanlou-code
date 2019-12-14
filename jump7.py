result = []
for i in range(1,101):

    if i%7 : 

        if i//10%10 != 7:

            if (i%10) != 7 : 
                result.append(i)
for i in result:
    print(i)

