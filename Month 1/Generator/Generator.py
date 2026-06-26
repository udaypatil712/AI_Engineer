def demo():
# yield pauses the function and remembers its state.

    yield 2
    yield 3 
    yield 4

res = demo()
print(next(res))  #this is single 



# this is for streaming data that we dont know how many it will come 

def stream_response():
    words = ["Hello", "Uday", "How", "Are", "You"]

    for word in words:
        yield word

for word in stream_response():
    print(word)