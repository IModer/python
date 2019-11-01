#string = "spOwOky OwOky pumpkin he a owange, woundo boi he woll and wobbwe wound de patch wooking fow a tastee snac! spOwOky OwOky pumpkin EYES so fuww of fwight! he’w bite youw toes n then u know he’s a evil boi tonite"
def myfunction(str):
    newstring = ""
    i = 0
    for x in str:
        if i % 2 == 1:
            newstring += x.lower() + "  "
            i += 1
        else:
            newstring += x.upper() + "  "
            i += 1
        #print(x)
    print(newstring)

#myfunction(string)
