print("Numbers from 1 to 10:")
for number in range(1, 11):
    print(number, end=" ")

print("\nEven numbers from 1 to 10:")
for number in range(2, 11, 2):
    print(number, end=" ")

print("\nSum of numbers from 1 to 10:", sum(range(1, 11)))

counter = 1
print("While loop:")
while counter <= 5:
    print(counter, end=" ")
    counter += 1
print()