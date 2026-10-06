water = int(input("Enter water in litres: "))

b500 = water // 500
remaining = water % 500

b200 = remaining // 200
remaining = remaining % 200

b50 = remaining // 50
remaining = remaining % 50

b10 = remaining // 10
remaining = remaining % 10

b1 = remaining // 1
remaining = remaining % 1

print(b500, b200, b50, b10, b1)