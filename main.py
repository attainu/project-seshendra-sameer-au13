from functions import Solution

def solve(cmd):
    if cmd[0] == "create_parking_lot":
        if len(cmd) == 2:
            s.create_parking_lot(int(cmd[1]))
        else:
            print("Invalid command")
            return
    elif cmd[0] == "park":
        if len(cmd) == 3:
            s.park(cmd[1], cmd[2])
        else:
            print("Invalid command")
            return
    elif cmd[0] == "leave":
        if len(cmd) == 2:
            s.leave(int(cmd[1]))
        else:
            print("Invalid command")
            return
    elif cmd[0] == "status":
        s.status()
    elif cmd[0] == "registration_numbers_for_cars_with_colour":
        if len(cmd) == 2:
            s.registration_numbers_for_cars_with_colour(cmd[1])
        else:
            print("Invalid command")
            return
    elif cmd[0] == "slot_numbers_for_cars_with_colour":
        if len(cmd) == 2:
            s.slot_numbers_for_cars_with_colour(cmd[1])
        else:
            print("Invalid command")
            return
    elif cmd[0] == "slot_number_for_registration_number":
        if len(cmd) == 2:
            s.slot_number_for_registration_number(cmd[1])
        else:
            print("Invalid command")
            return
    else:
        print("Invalid command")
        return

def main():
    while True:
        dummy = input("$ ")
        
        if len(dummy) < 1:
            continue
        if dummy == "exit":
            return
        if dummy.endswith(".txt"):
            with open(dummy) as f:
                for line in f:
                    line = line.rstrip('\n')
                    solve(line.strip().split())
            break
        else:
            solve(dummy.strip().split())

if __name__ == "__main__":
    s = Solution() 
    main()
    
