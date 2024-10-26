#This is the start of Project 0-1
#AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
import sys
linebreak= "********************************"
allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
menuSelect= 0
searchtCar="string"
#Function for car searches called in step 2
def find_Car(searchCar):
    if searchCar in allowedVehiclesList:
        print(searchCar + " is an authorized vehicle.")
    else:
        print(searchCar + " is not an authorized vehicle, if you recieved this in error please check the spelling and try again.")
#print statements for input request
print(linebreak)
print("AutoCountry Vehicle Finder v0.2")
print(linebreak)
#input request
menuSelect=int(input("Please make a selection from the following menu: ""\n " "\n1.PRINT all Authorized Vehicles" "\n2.SEARCH for Authorized Vehicle" "\n3.Exit" "\n" ))
#selection logic
#i had to google some For syntax but this is much neater, i'm leaving the old prints statements in comment as a reference
if menuSelect == 1:
    for car in allowedVehiclesList:
        print(car)
    #print(allowedVehiclesList[0])
    #print(allowedVehiclesList[1])
    #print(allowedVehiclesList[2])
    #print(allowedVehiclesList[3])
    #print(allowedVehiclesList[4])

if menuSelect == 2:
    print(linebreak)
    searchCar=input("Please Enter the full Vehicle name: ")
    find_Car(searchCar)
if menuSelect ==3:
    print("Thank you for using AutoCountry Vehicle Finder, good-bye!")
    sys.exit()


