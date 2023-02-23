def informations(city,country):
    full= city +country
    return full.title()
while True:
    c=input()
    co=input()
    if c=='q':
        break
    total=informations(c,co)
    print(total)