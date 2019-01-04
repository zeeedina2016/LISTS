#get low range
low_range = int(input("Enter the low end of the range: "))


#get high range
high_range = int(input("Enter the high end of the range: "))


#enter the number
num = int(input("Enter the number: "))

#num_list = []
#for i in range(low_range,high_range):
    #if i <= low_range:
        #if i >= high_range:
            #num_list.append(i)


div_list = []

#get the answer and put it in a list
for j in range(low_range,high_range+1):
    if j % num == 0:
        div_list.append(j)

#print list
print("The resulting list is ", div_list)
