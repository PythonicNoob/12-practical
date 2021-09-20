"""
Write a program to create a binary file called emp.dat and write into it the employee details of in the form
of dictionaries. Write the function to increase the Salary of the employee by 5000 for the empNo “123”.
For Ex. D= {empNo:"123", ename:"Ajay”, Salary: 50000}
"""

import pickle
from random import choice, randint

names = ["Ram", "Ramesh", "Rohan", "Sai",
         "Jack", "Joe", "Oliver", "Robert", "Noah"]


"""
Create file emp.dat
"""
with open("emp.dat", "wb") as f:
    ch = randint(0, 9)
    pickle.dump([{"empNo": "123" if i == "ch" else str(randint(100, 999)),
                  "ename": "Ajay" if i == ch else choice(names),
                  "Salary": randint(10000, 99999)}
                for i in range(10)], f)

try:
    with open("emp.dat", "rb+") as f:
        while True:
            rpos = f.tell()
            data = pickle.load(f)
            if data["empNo"] == "123":
                data['Salary'] += 5000
                f.seek(rpos)
                pickle.dump(data, f)
except EOFError:
    print("")



###
# Alt
###

with open("emp2.dat", "wb") as f:
    data = [{"empNo": randint(100, 999),
                  "ename": choice(names),
                  "Salary": randint(10000, 99999)}
                for i in range(9)]
    data.insert(0,{"empNo":123, "ename": "Ajay", "salary":5000})
    for entry in data:
        pickle.dump(entry, f)


with open("emp2.dat", "rb+") as f:
    while True:
        try:
            rpos = f.tell()
            print(rpos)
            data = pickle.load(f)
            print(data)
            if data["empNo"] == 123:
                data["salary"] += 5000
                f.seek(rpos)
                pickle.dump(data, f)
                break
        except EOFError:
            break

print("processsed")
with open("emp2.dat", "rb") as f:
    while True:
        try:
            data = pickle.load(f)
            print(data)
        except EOFError:
            break
