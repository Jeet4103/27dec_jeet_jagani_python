class student:
    name = ""
    id = 0
    def getdata(self):
        self.name = input("Enter your name: ")
        self.id = int(input("Enter your id: "))

    def putdata(self):
        print(f"Your namm is {self.name} and your id is {self.id}")

std = student()
std.getdata()
std.putdata()