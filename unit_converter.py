#program to convert units 

username = input("Please enter your username:")
print("welcome to my challenge, " + username + "!!!!")
#we print the list of conversion units
units = ["convert km to m",  "convert m to cm",  "convert cm to inches"]
print(username + ",please pick units you want to convert to.")
for number, name in enumerate(units, 1):
    print("{} {}".format(number, name))
# ask user to enter a unit int
inpt = input("choice in number form:")
n = int(inpt)
# carring conversion
if n == 1:
    dg = input("Enter number  in kilometres:")
    t = int(dg)
    print("converting ...%s kilometers to meters."%(t))
    out = t * 1000
    print("it's, " + str(out) + " meters.")
elif n == 2:
    dg = input("Enter number in metres:")
    t = int(dg)
    print("converting ...%s meters to centimeters."%(t))
    out = t * 100
    print("it's, " + str(out) + " centimeters.")
elif n == 3:
    dg = input("Enter number  in centimetres:")
    t = int(dg)
    print("converting ...%s centimeter to inches."%(t))
    out = t * 0.394
    print("it's, " + str(out) + " inches.")
else:
    print("ERROR!!!")

print("BYE! BYE!" + username)
