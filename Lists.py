#initialize speed list
speed_list = []

#get how many cars
cars = int(input( "How many cars passed the sensor? "))


i = 0
#loop to figure out percentage of cars under speed limit
while i < cars:

    #get speed for each car and impend it into speed_list
    speed = int(input("Enter speed for car " + str(i+1) + ": "))
    speed_list.append(speed)
    i = i + 1

#print carsList
print(speed_list)   

#initialize total that accumulates cars under speed limit
total = 0
#initialize counter to count how many cars are less than or equal to speed limit
counter = 0
#get speed limit
speed_limit = int(input("what is speed limit?"))

#for each car in the list
for i in range(len(speed_list)):
    if speed_list[i] <= speed_limit:
        total = total + speed_list[i]
        counter = counter + 1


#comupute percentage (part/whole)*100
if counter > 0:
    per =(counter/cars)*100
    print("The percentage of cars that were within the speed limit is " + str(per) + "%")
else:
    print("You may need to slow down or speed up!!")
