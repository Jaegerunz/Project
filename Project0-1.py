#This is the start of Project 0-1
#AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
import sys
vehicleFile= r"C:\COP1000 Files\Project\AllowedVehiclesList.txt"
def readVehicleModels(vehicleFile):
        with open (r"C:\COP1000 Files\Project\AllowedVehiclesList.txt", 'r') as file:
            data = file.read().strip()
            allowedVehicleList= [car.strip() for car in data.split (',')]
        return allowedVehicleList
linebreak= "********************************"
allowedVehiclesList = readVehicleModels(vehicleFile)
menuSelect= 0
#Function for car searches called in step 2
def find_Car(searchCar):
    found = False
    for car in allowedVehiclesList:
        if car == searchCar:
            found = True
            break

    if found:
        print(searchCar + " is an authorized vehicle.")
    else:
        print(searchCar + " is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
#v0.4 remove vehicle
def deleteCar(searchCar, allowedVehiclesList):
    if searchCar in allowedVehiclesList:
         confirm= input("Are you sure you want to remove "+ searchCar + "from the Authorized Vehicles List Y/N?")
         if confirm == "Y":
              allowedVehiclesList = [car for car in allowedVehiclesList if car != searchCar]
              with open(vehicleFile, 'w') as file:
                   file.write(','.join(allowedVehiclesList))
              print("You have REMOVED "+searchCar +"as an authorized Vehicle")

         else:
            print ("REMOVE Cancelled.")
    else:
         print(searchCar+" is not on the authorized vehicle list and cannot be removed.")
         
def displayMenu():
    print(linebreak)
    print("AutoCountry Vehicle Finder v0.4")
    print(linebreak)
    menuSelect=int(input(
        "Please make a selection from the following menu: ""\n "
        "\n1.PRINT all Authorized Vehicles"
        "\n2.SEARCH for Authorized Vehicle"
        "\n""3.ADD Authorized Vehile"
        "\n""4.DELETE Authorized Vehicle" 
        "\n5.Exit""\n" ))
    return menuSelect
#replacing old menu with looping menu so I dont have to run the program over and over
#i had to google some For syntax but this is much neater, i'm leaving the old print statements in comment as a reference
while True:
     menuSelect = displayMenu()
     if menuSelect == 1:
          for car in allowedVehiclesList:
               print(car)
          input("Press Enter to return to the main menu.")
     elif menuSelect ==2:
          print(linebreak)
          searchCar = input("Please Enter the full Vehicle name: ")
          find_Car(searchCar)
          input("Press Enter to return to the main menu.")
     elif menuSelect == 3:
          addVehicle = input("Please Enter the full Vehicle name you would like to add: ")
          with open(vehicleFile, "a") as file:
               file.write(", " + addVehicle.strip())
          print("YOu have added "+ addVehicle + "as an authorized vehicle.")
          input("Press Enter to return to the main menu.")
     elif menuSelect == 4:
          searchCar =input("Please Enter the full Vehicle name you would like to REMOVE: ")
          deleteCar(searchCar, allowedVehiclesList)
          input("Press Enter to return to the main menu.")

     elif menuSelect ==5:
          print("Thank you for using AutoCountry Vehicle Finder, good-bye!")
          sys.exit()