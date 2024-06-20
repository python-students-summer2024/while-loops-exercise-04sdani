def get_starting_number():

    valid_input = 0
    while valid_input < 1:
        bottles_of_beer = input("How many bottles of beer on the wall? ")
        if bottles_of_beer.isnumeric() is False:
            valid_input = 0
        elif int(bottles_of_beer) < 1:
            valid_input = 0
        else:
            valid_input = 1
            return bottles_of_beer


def sing(bottles_of_beer):
    for i in range(int(bottles_of_beer), 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle of beer on the wall.")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!")