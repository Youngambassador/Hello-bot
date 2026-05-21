print("Hello! Welcome to my first python bot.")


name = input("What is your name?")
age = input("Nice to meet you," + name + "! How old are you?")
color = input("Alright " + name + ",what's your favourite color?")


print("Got it! so you're" + age + "years old.")

if color.lower() == "red":

     print("Red? You must be a fire pilot! 🔥")

elif color.lower() == "blue":

     print("Blue? Calm like the sky, Captain! 🌊")

elif color.lower() == "green":

     print("green? Nature lover detected! 🌿")
else:

   print("Cool! " + color + " is a nice color, Captain!")

print("Type 'exit' to quit.")


