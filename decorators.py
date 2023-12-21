def announce(f):
    def wrapper():
        print("About to run the functuion")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("hEllo world")

hello()