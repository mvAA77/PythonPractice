print(
    "Welcome to the What Rock Are You Quiz Let's begin. Make sure to always capitalize your answers!"
)
print()
animal = input("Dogs or Cats? ")
if animal == "Cats":
  drink = input("Coffee or Tea? ")
  if drink == "Coffee":
    time = input("Morning or Night? ")
    if time == "Morning":
      print("Congrats! You are a Granite!")
    else:
      print("Congrat! You are an Obsidian!")
  if drink == "Tea":
    flavor = input("Chocolate or Vanilla? ")
    if flavor == "Chocolat":
        print("Congrats! You are Basalt!")
    if flavor == "Vanilla":
        print("Congrats! You are a Sandstone!")
if animal == "Dogs":
    when = input("Past or Future? ")
    if when == "Past":
      planet = input("Mars or Jupiter")
      if planet == "Mars":
        print("Congrats!. You are an Amethyst!")
      else:
        cereal = input("Milk or Cereal First? ")
        if cereal == "Cereal":
          print("YOU'RE JUST LIKE MEEEEE!")
        else:
          print("Congrats! You are a Serpentine!")
    if when == "Future":
      print("Congrats! You're a Jade!")
