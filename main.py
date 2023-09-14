exit = "no"
while exit == "no":
  your_animal = input("What's your animal sound?")
  if your_animal == "dog" or your_animal == "Dog":
    print("🦮 bow-wow")
  elif your_animal == "cat" or your_animal == "Cat":
    print("🐈 miaow")
  elif your_animal == "cow" or your_animal == "Cow":
    print("🐄 moo")
  else:
    print("None of these sounds. Try again!")
    exit = input("Do you want to exit? ")
