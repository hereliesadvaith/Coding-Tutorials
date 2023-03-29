fav_colour: str = input("Enter your favourite colour:")
match fav_colour.lower():
    case "black":
        print("Adi has a black shirt")
    case "white":
        print("Adi has a white shoe")
    case "grey":
        print("Adi has  grey pants")
    case _:
        print(f"Adi has nothing in {fav_colour} ")
