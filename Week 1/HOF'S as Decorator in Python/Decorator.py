def logger1(func):
    print("start ")

    func()

    print("end")
#---- why here we no need write or call greet() because we are not returning anything
@logger1
def greet():
    print("hello uday")    
#  greet() 
#---- why here we no need write or call greet() because we are not returning anything

#

# logger1(greet)

# def logger(func):

#     def wrapper():

#         print("Before")

#         func()

#         print("After")

#     return wrapper

# @logger
# def hello():
#     print("Hello")


# hello()    

# new_hello = logger(hello)

# new_hello()