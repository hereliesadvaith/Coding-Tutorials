def smartdiv(x: int, y: int) -> None:
    try:
        num = x / y
        print(num)
    except TypeError:
        print("Both x and y should be numbers")
    except Exception as e:
        print(f"Oops !!! something went wrong: {e}")
    else:
        print("Divided")
    finally:
        print("Get out")


smartdiv(5, 0)


def find_zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    try:
        assert name in friends
    except AssertionError:
        print(f"{name} not found!")
    else:
        print(f"Found {name}")
    finally:
        print("Goodbye")


find_zohan("Zohan")
find_zohan("Sara")


def find__zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    if name not in friends:
        raise ValueError(f"{name} not found")
    else:
        print(f"Found {name}")


find__zohan("Nihu")
