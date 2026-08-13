def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper      

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge🥤*")  
        func(*args, **kwargs) 
    return wrapper

@add_sprinkles
@add_fudge
def getIcecream(flavor):
    print(f"Here is your {flavor} Icecream 🍧")

getIcecream("vanilla")
