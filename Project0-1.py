#This is the start of Project 0-1
#AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
import sys
vehicleFile=open(r"C:\COP1000 Files\Project\AllowedVehiclesList.txt", "r")
linebreak= "********************************"
allowedVehiclesList = [vehicleFile.read()]
menuSelect= 0
searchCar="string"
#Function for car searches called in step 2
def find_Car(searchCar):
    if searchCar in allowedVehiclesList:
        print(searchCar + " is an authorized vehicle.")
    else:
        print(searchCar + " is not an authorized vehicle, if you recieved this in error please check the spelling and try again.")
#Menu
print(linebreak)
print("AutoCountry Vehicle Finder v0.3")
print(linebreak)
#input request
menuSelect=int(input("Please make a selection from the following menu: ""\n " "\n1.PRINT all Authorized Vehicles" "\n2.SEARCH for Authorized Vehicle""\n""3.ADD Authorized Vehile" "\n4.Exit" "\n" ))
#selection logic
#i had to google some For syntax but this is much neater, i'm leaving the old print statements in comment as a reference
if menuSelect == 1:
    for car in allowedVehiclesList:
        print(car)
    #print(allowedVehiclesList[0])
    #print(allowedVehiclesList[1])
    #print(allowedVehiclesList[2])
    #print(allowedVehiclesList[3])
    #print(allowedVehiclesList[4])
#Menu Selection Opperations
if menuSelect == 2:
    print(linebreak)
    searchCar=input("Please Enter the full Vehicle name: ")
    find_Car(searchCar)
if menuSelect == 3:
    addVehicle=input("Please Enter the full Vehicle name you woud like to add:")
    with open(r"C:\COP1000 Files\Project\AllowedVehiclesList.txt", "a") as file:
        file.write(str(", "+addVehicle))
    print("You have added "+ addVehicle +" as an authorized vehicle")
if menuSelect ==4:
    print("Thank you for using AutoCountry Vehicle Finder, good-bye!")
    sys.exit()


