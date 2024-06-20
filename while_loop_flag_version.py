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
    beer_count = int(bottles_of_beer)
    flag = True
    while flag:
        if beer_count > 2:
            print(f"{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.")
            print(f"Take one down, pass it around, {beer_count-1} bottles of beer on the wall.")
            beer_count = beer_count - 1
        elif beer_count == 2:
            print(f"{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.")
            print(f"Take one down, pass it around, {beer_count-1} bottle of beer on the wall.")
            beer_count = beer_count - 1
        else:
            print(f"{beer_count} bottle of beer on the wall, {beer_count} bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!")
            flag = False