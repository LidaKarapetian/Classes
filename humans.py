#!/usr/bin/python

# We have Human class and need to sorting human's ages in ascending order

class Human:
    def __init__(self, n, s, a):
        self.name = n
        self.surname = s
        self.age = a

    def __str__(self):
        return f"{self.name} {self.surname} - {self.age}"
    
    def __lt__(self, other):
        return self.age < other.age

    def read_content(fname):
        humans = []
        with open(fname, "r") as f:
            for line in f:
                data = line.strip().split()
                if len(data) == 3:
                    name, surname, age = data
                    age = int(age)
                    humans.append(Human(name, surname, age))
        return humans
    
def main():

    humans = Human.read_content("info.txt")
    sorted_age= sorted(humans, key=lambda x: x.age)

    for el in sorted_age:
        print(el)


if __name__ == "__main__":
    main()