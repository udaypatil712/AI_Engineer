# What is *args?

# It collects all positional arguments into a tuple.What is *args?

# It collects all positional arguments into a tuple.


def demo(*args):
    print(args)

demo(10, 20, 30) 

# output (10 20 30 ) tuple 


# it take's at time argument in tuble like js apply for array 

# ------------What is **kwargs--------------


# It collects keyword arguments into a dictionary.

def person(**kwargs):
    print(kwargs)

person(name="Uday", age=22)  

# {'name': 'Uday', 'age': 22}  .....output.....

