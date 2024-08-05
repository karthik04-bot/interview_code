date_1 = "03-02-2024"
date_2 = "04-01-2024"

d1 = date_1.split('-')
d2 = date_2.split('-')
l = []
for i in range(len(d1)):
    if int(d1[i]) > int(d2[i]):
        diff = int(d1[i]) - int(d2[i])
    elif int(d2[i]) > int(d1[i]):
        diff = int(d2[i]) - int(d1[i])
    else:
        diff = int(d2[i]) - int(d1[i])

    if i == 1:
        print("number of diff in months is {}".format(diff))
        diff *= 25
    elif i == 2:
        print("number of diff in years is {}".format(diff))
        diff *= 300
    l.append(diff)
    print(l)
print("Difference between the days {}".format(sum(l)))