
rum =[
    ["Single James Cook Mixer", 1.6],
    ["Double James Cook Mixer", 2.4],
    ["Single Kraken Mixer", 2.3],
    ["Double Kraken Mixer", 3.5],
    ["Single Morgans Mixer", 1.9],
    ["Double Morgans Mixer", 2.8],
    ]

whiskey = [
    ["Single JD Mixer", 2.3],
    ["Double JD Mixer", 3.5],
    ["Single Southern Comfort Mixer", 1.9],
    ["Double Southern Comfort Mixer", 2.8],
    ]

vodka = [
    ["Single Dirty Vodka Mixer", 1.6],
    ["Double Dirty Vodka Mixer", 2.4],
    ["Single Smirnoff Vodka Mixer", 2.0],
    ["Double Smirnoff Vodka Mixer", 2.8],
    ]

gin = [
    ["Single London Dry Mixer", 1.6],
    ["Double London Dry Mixer", 2.4],
    ["Single Gordon's Mixer", 1.9],
    ["Double Gordon's Mixer", 2.8],
    ]

amaretto = [
    ["Single Disaronno Mixer", 1.4],
    ["Double Disaronno Mixer", 2.0],
    ]

cocktails = [
    ["Godfather", 3.0],
    ["Sex on the Beach", 3.0],
    ["Woo Woo", 3.0],
    ["Blue Lagoon", 3.0],
    ["Cosmo", 3.0],
    ["Espresso Martini", 3.5],
    ["Strawberry Daiquiri", 3.5],
    ["Tequila Sunrise", 3.5],
    ["Mai Tai", 3.5],
    ["Yoda", 3.5],
    ["Chip's Signature Cuba Libre", 4.0],
    ["Long Island", 4.0],
    ["Zombie", 4.5],
    ["Large Sex on the Beach", 4.5],
    ["Large Godfather", 4.5],
    ["Large Blue Lagoon",  4.5]
    ]

bottles = [["corona", 1.5],
           ["VK Orange", 2.5]]

all_drinks = rum + whiskey + vodka + gin + amaretto + cocktails + bottles


if __name__ == "__main__":
    from tabulate import tabulate
    print(tabulate(all_drinks))
