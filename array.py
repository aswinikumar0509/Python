#Array : Array is a special variable , which can hold more than one value at a time.

cars = ["Ford","Volvo","BMW"]
print(cars)

x = cars[0]
print(x)

cars[0] = "mercedes"
print(cars)

print(len(cars))

for x in cars:
    print(x)

cars.append(("lamborghini"))
print(cars)

cars.append("Rolls Royce")

print(cars)
