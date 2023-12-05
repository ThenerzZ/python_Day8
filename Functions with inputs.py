something = "bitch"

def greet(something):
    print(something)


greet(something)

#positional  vs keyword arguments

#func with mroe than 1 inpout
#positiuion arg
#def greet_with(name, location):
    #print(f"Hello {name}")
    #print(f"how is it in {location} ?")

#greet_with("jack bauer", "nowhere") #inpouts assinged xd

#keyword arg

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"nice here in {location}")

greet_with(location="London", name="Selli")
