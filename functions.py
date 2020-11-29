class Solution:
    def __init__(self):
        self.cars_arrived = []
        self.cars_parked = {}
        self.current_status_of_lot = {}

    def create_parking_lot(self, slots):
        for i in range(1, slots + 1):
            self.current_status_of_lot[i] = False
        print("Created a parking lot with %d slots" %slots)

    def park(self, registration_no, color):
        car = (registration_no, color)
        self.cars_arrived.append(car)
        for i in self.current_status_of_lot.keys():
            if self.current_status_of_lot[i] == False:
                if car in self.cars_parked.keys():
                    self.cars_parked[car].append(i)
                else:
                    self.cars_parked[car] = [i]
                self.current_status_of_lot[i] = car
                print("Allocated slot number: %d" %i)
                break
        else:
            print("Sorry, parking lot is full")

    def leave(self, slot):
        if self.current_status_of_lot[slot] == False:
            print("Slot is already empty")
        else:
            self.current_status_of_lot[slot] = False
            print("Slot number %d is free" %slot)

    def status(self):
        print("Slot No.", end = "    ")
        print("Registration No.", end = "    ")
        print("Colour")
        for i,j in self.current_status_of_lot.items():
            
            if j == False:
                continue
            else:
                print("   ", i, end = "        ")
                print(j[0], end = "")
                if len(j[0]) == 10:
                    print("          ", end = "")
                elif len(j[0]) == 11:
                    print("         ", end = "")
                elif len(j[0]) == 12:
                    print("        ", end = "")    
                elif len(j[0]) == 13:
                    print("       ", end = "")
                print(j[1])
        
    def registration_numbers_for_cars_with_colour(self, color):
        temp = []
        for i in self.cars_parked.keys():
            if i[1] == color:
                temp.append(i[0])

        if len(temp) == 0:
            print("No %s car has entered this parking lot" %color)
            return
        for i in temp[:len(temp) - 1]:
            print(i, end = ", ")
        print(temp[-1])

    def slot_numbers_for_cars_with_colour(self, color):
        temp = []
        for i, j in self.current_status_of_lot.items():
            if j[1] == color:
                temp.append(i)

        if len(temp) == 0:
            print("Not found")
            return
        for i in temp[:len(temp) - 1]:
            print(i, end = ", ")
        print(temp[-1])
    
    def slot_number_for_registration_number(self, registration_no):
        temp = []
        for i, j in self.current_status_of_lot.items():
            if j[0] == registration_no:
                temp.append(i) 

        if len(temp) == 0:
            print("Not found")
            return
        for i in temp[:len(temp) - 1]:
            print(i, end = ", ")
        print(temp[-1])