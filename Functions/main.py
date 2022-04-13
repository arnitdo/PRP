awesomeString = "FizzBuzz"

def myFunction():
    awesomeString = "BuzzFizz"
    # Here, "BuzzFizz" overwrites the global value for the function scope
    # "FizzBuzz" remains unchanged outside the function
    print("awesomeString inside myFunction =", awesomeString)


myFunction()
print("awesomeString outside myFunction =", awesomeString)


# Manipulating global values

def mySecondFunction():
    global magicWords
    # magicWords now belongs to the global scope
    # Will not be garbage-collected when function scope ends
    magicWords = "Lorem Ipsum"


mySecondFunction()
print(f"The magic words are '{magicWords}'")