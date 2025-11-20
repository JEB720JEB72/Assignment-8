#main(): is for information gathering to get a number
#parse_input(): will figure out if what's given is hex or decimal
#convert_to_binary: will convert the above number to binary


def main():
    #abc
    user_text = input("please enter a number, which can be hex or decimal")
    
    number, flavor = parse_input(user_text)
    results = convert_to_binary(number,flavor)
    print(results)

def parse_input(new):
    #deliniate between hex and decimal and convert
    if new.lower().startswith("0x"): 
        number = int(new,16)
        flavor = "hex"
    else:
        number = int(new)
        flavor = "dec"
    return number, flavor

def convert_to_binary (number,flavor):
    #abc
    binary_string = bin(number)[2:]
    return "excellent, the binary is: " + binary_string

main()
