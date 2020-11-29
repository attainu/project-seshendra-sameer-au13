## ParkingLot
Design a parking lot using Python.

## Dependencies

You just need Python. The code is compatible with Python2 as well as Python3. Visit the link https://www.python.org/downloads/ to install Python. 

## Description

This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy(nearest slot first) approach while being parked in the slots.

ParkingLot.py script defines the following functions -

1. `create_parking_lot n` - Given n number of slots, create a parking lot
2. `park car_regno car_color` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
3. `status` - Prints the slot number, registration number and color of the parked vehicles.
4. `leave x` - Removes vehicle from slot number x
5. There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.

ParkingLot.py can be run through shell or through file containing test cases. An example file `test_case.txt` has been provided in repo.


## Setup

To create your own ParkingLot - 

1. Clone the repository

2. Run `python main.py`. This opens a shell where you can write your commands.
  
3. To run with a file enter, the name of the file, i.e.. `test_case.txt` in the shell . You can modify the test cases.