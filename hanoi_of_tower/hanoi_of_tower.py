class HanoiOfTower:
    def __init__(self):
        self.array1 = []
        self.array2 = []
        self.array3 = []

    def setup(self):
        self.array1.append(3)
        self.array1.append(2)
        self.array1.append(1)


    def move_from_to(self, source, target):
        if len(source) > 0:
            if len(target) <= 0 or source[len(source)-1] < target[len(target)-1]:
                sub_array = source.pop()
                target.append(sub_array)
            else:
                print("source is greater than target")
        else:
            print("source is empty")

    def get_array_by_number(self, number):
        match number:
            case 1:
                return self.array1
            case 2:
                return self.array2
            case 3:
                return self.array3

    def play(self):

        while len(self.array3) <= 3:
            command = input("user enters command: ")
            if len(command) == 3:
                source = float(command[0])
                target = float(command[2])

                source_array = self.get_array_by_number(source)
                target_array = self.get_array_by_number(target)

                self.move_from_to(source_array, target_array)
                self.print_result()

                if len(self.array3) == 3:

                    print("you win")
                    break
            else:
                print("get out")
                break

                # if command[0] == "1":
                #     if command[2] == "2":
                #         self.move_from_to(self.array1,self.array2)
                #     elif command[2] == "3":
                #         self.move_from_to(self.array1,self.array3)
                #
                # if command[0] == "2":
                #     if command[2] == "1":
                #         self.move_from_to(self.array2, self.array1)
                #     elif command[2] == "3":
                #         self.move_from_to(self.array2,self.array3)
                #
                # if command[0] == "3":
                #     if command[2] == "1":
                #         self.move_from_to(self.array3, self.array1)
                #     elif command[2] == "2":
                #         self.move_from_to(self.array3, self.array2)

    def print_result(self):
        print(self.array1)
        print(self.array2)
        print((self.array3))
