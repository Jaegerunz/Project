#This is the start of Project 0-1
#AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
import sys
allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Trundra', 'Nissan Titan']
menuSelect= 0
#print statements for input request
print("********************************")
print("AutoCountry Vehicle Finder v0.1")
print("********************************")
#input request
menuSelect=int(input("Please make a selection from the following menu: ""\n " "\n1. PRINT all Authorized Vehicles" "\n2.Exit""\n" ))
#selection logic
if menuSelect == 1:
    print("test")
    print(allowedVehiclesList[0])
    print(allowedVehiclesList[1])
    print(allowedVehiclesList[2])
    print(allowedVehiclesList[3])
    print(allowedVehiclesList[4])
if menuSelect ==2:
    sys.exit()