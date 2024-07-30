import random


class Room(object):
    def __init__(self, state="dirty"):  # CONSTRUCTOR TO INITIALISE VALUES
        self.state = state


class VaccumCleaner(object):
    def __init__(self, location=1):  # CONSTRUCTOR TO INITIALISE VALUES
        self.location = location

    def sense(self, room1, room2, location):  # SENSES THE CONDITION OF ROOMS AND LOCATION OF VACUUM CLEANER
        if (room1.state == "dirty" and room2.state == "dirty" and location == 1):
            return "dirty,dirty,1"

        elif (room1.state == "dirty" and room2.state == "dirty" and location == 2):
            return "dirty,dirty,2"

        elif (room1.state == "dirty" and room2.state == "clean" and location == 1):
            return "dirty,clean,1"

        elif (room1.state == "dirty" and room2.state == "clean" and location == 2):
            return "dirty,clean,2"

        elif (room1.state == "clean" and room2.state == "dirty" and location == 1):
            return "clean,dirty,1"

        elif (room1.state == "clean" and room2.state == "dirty" and location == 2):
            return "clean,dirty,2"

        elif (room1.state == "clean" and room2.state == "clean" and location == 1):
            return "clean,clean,1"

        elif (room1.state == "clean" and room2.state == "clean" and location == 2):
            return "clean,clean,2"

    def decide(self, sensedData):  # DECIDES THE SEQUENCE OF ACTIONS TO PERFORM IN RESPONSE TO THE DATA THAT IS SENSED
        if (sensedData == "dirty,dirty,1"):
            return "clean1,moveright,clean2"

        elif (sensedData == "dirty,dirty,2"):
            return "clean2,moveleft,clean1"

        elif (sensedData == "dirty,clean,1"):
            return "clean1"

        elif (sensedData == "dirty,clean,2"):
            return "moveleft,clean1"

        elif (sensedData == "clean,dirty,1"):
            return "moveright,clean2"

        elif (sensedData == "clean,dirty,2"):
            return "clean2"

        elif (sensedData == "clean,clean,1"):
            return "null"

        elif (sensedData == "clean,clean,2"):
            return "null"

    def actuate(self, decision, room1, room2):  # PERFORMS THE APPROPRIATE ACTION ON THE BASIS OF DECISION
        if (decision == "clean1,moveright,clean2"):
            self.suckDirt()
            room1.state = "clean"
            self.moveRight()
            self.suckDirt()
            room2.state = "clean"

        elif (decision == "clean2,moveleft,clean1"):
            self.suckDirt()
            room2.state = "clean"
            self.moveLeft()
            self.suckDirt()
            room1.state = "clean"

        elif (decision == "clean1"):
            self.suckDirt()
            room1.state = "clean"

        elif (decision == "moveleft,clean1"):
            self.moveLeft()
            self.suckDirt()
            room1.state = "clean"

        elif (decision == "moveright,clean2"):
            self.moveRight()
            self.suckDirt()
            room2.state = "clean"

        elif (decision == "clean2"):
            self.suckDirt()
            room2.state = "clean"

    # MOVES THE VACUUM CLEANER TO LEFT IN ROOM 1
    def moveLeft(self):
        print("MOVED TO LEFT!")
        self.location = 1

    # MOVES THE VACUUM CLEANER TO RIGHT IN ROOM 2
    def moveRight(self):
        print("MOVED TO RIGHT!")
        self.location = 2

    # CLEANS THE ROOM BY SUCKING DIRT
    def suckDirt(self):
        print(f"CLEANED ROOM {self.location}")

    # STARTS THE VACUUM CLEANER
    def powerOnVaccum(self, room1, room2):
        if (room1.state != "clean" or room2.state != "clean"):
            sensedData = self.sense(room1, room2, self.location)
            decision = self.decide(sensedData)
            self.actuate(decision, room1, room2)

        self.powerOffVaccum()

    # SHUTS DOWN THE VACUUM CLEANER
    def powerOffVaccum(self):
        print("BOTH ROOMS ARE CLEAN SO VACCUM IS POWERING OFF!")

    # GENERATES A RANDOM NUMBER 1 OR 2 TO IDENTIFY INITIAL LOCATION OF THE VACUUM CLEANER


def generateRandLoc():
    return random.randint(1, 2)


# CONTAINS THE DRIVER CODE OF THE AGENT i.e. VACCUM CLEANER
def main():
    room1 = Room()  # TWO ROOMS' OBJECTS DECLARED
    room2 = Room()

    if __name__ == "__main__":

        # FOR INPUTTING VALID STATE OF ROOM 1
        validState = False
        while (validState != True):
            roomState = int(
                input("CHOOSE THE INITIAL STATE OF ROOM 1, ENTER (1) FOR ""DIRTY"" AND (2) FOR ""CLEAN"": "))
            if (roomState != 1 and roomState != 2):
                print("INVALID ENTRY, ENTER AGAIN!")

            else:
                validState = True

        if (roomState == 1):
            state = "dirty"

        else:
            state = "clean"

        room1.state = state

        # FOR INPUTTING VALID STATE OF ROOM 2
        validState = False
        while (validState != True):
            roomState = int(
                input("CHOOSE THE INITIAL STATE OF ROOM 2, ENTER (1) FOR ""DIRTY"" AND (2) FOR ""CLEAN"": "))
            if (roomState != 1 and roomState != 2):
                print("INVALID ENTRY, ENTER AGAIN!")

            else:
                validState = True

        if (roomState == 1):
            state = "dirty"

        else:
            state = "clean"

        room2.state = state

        # validRoom = False
        # while(validRoom != True)1:
        # startingRoom = int(input("ENTER THE STARTING LOCATION OF THE VACCUM CLEANER, NOTE THAT THERE ARE ONLY TWO LOCATIONS AND YOU CAN ENTER (1) FOR ROOM A AND (2) FOR ROOM B: "))
        startingRoom = generateRandLoc()
        print(f"RANDOMLY CHOSEN INITIAL LOCATION OF THE VACCUM CLEANER IS ROOM {startingRoom}")
        if (startingRoom != 1 and startingRoom != 2):
            print("INVALID ENTRY, ENTER AGAIN!")

        else:
            validRoom = True

        vc = VaccumCleaner(startingRoom)  # VACCUM CLEANER OBJECT DECLARED

        vc.powerOnVaccum(room1, room2)  # STARTING FUNCTIONALITY OF VACCUM CLEANER


main()