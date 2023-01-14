# LOOPS

# Note 1 
# Task: code to accept the name of 5 people and print it

# for loop method
for i in range(5): 
    # the loop always starts from here
    name = input('enter your name >> ')
    print('hello ' + name)


    # the loop ends after your last line of code 
    # and it will go back to the start


# while loop method 

i = 0
while i < 5: 
    name = input('enter your name >> ')
    print('hello ' + name)
    i += 1 
    # we have to increase 'i' because of the condition otherwise 
    # 'i' will be a constant and the loop will run forever
# --------------------------------------------------------------


# Note 2
# note that the variables in the loop conditions 
# can be used in the loop itself 

# for example 
# Task: write code to sum the first 10 natural numbers

# for loop method 
final_sum = 0 
for n in range(1, 11):
    # note range does not include the end number
    #  so we have to increase by 1 so it reaches 
    # the number we want

    final_sum += n 



# while loop method 
n  = 1 
final_sum = 0 
while n <= 10:
    final_sum += n 
    n += 1  # to avoid an infinite loop
# ---------------------------------------------------------------


# Note 3
# Task: Write code to perform 1 + 1/2 + 1/3 + 1/4 + ......+ 1/n 
# accept 'n' BEFORE you start the loop

# ------------------------------------------------------























