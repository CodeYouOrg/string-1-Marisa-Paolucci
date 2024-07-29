# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    donut_amount = count
    if(count >= 10):
        donut_amount = 'many'
    return_statement = 'Number of donuts: ' + str(donut_amount)
    return return_statement

# def donuts(count) defines the function donuts that takes a single parameter called 'count'. 
# donut_amount is the variable created to set equal to 'count'. This new variable will store the number of donuts or the "many" if the amount of donuts is too high.
# the if statement checks to see if the value of 'count' is greater than or equal to 10.
# if the if statement is true, then it executes and sets the 'donut_amount to the string 'many'.
# 'return_statement' creates a string that combines "Number of donuts: " with the string representation of 'donut_amount'. 'str' makes sure that the function is used to create a string, even if it is a number.
# the return line is necessary to return the output of the function. 


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(s):
    new_word = ''
    if (len(s)>2):
        new_word = s[0:2] + s[-2:]
    return new_word


# def both_ends(s) defines the function both_ends and s is the expected string.
# new-word = ' ' creates a new variable with an empty string so that it can store the result of the function.
# in this if statement we are checking to see if the length of the string 's' is greater than 2. This is to make sure that the string is long enough to have both its first two and last two letters.
# if the "if" statement is met, then this line will execute and create a new string called "new_word". 's[0:2]' will slice the string 's' by taking the first two letters (from index 0 to index 2, but not including index 2). 's[-2:] is another slice that takes the last two letters of string 's'. '-2' is the start index and ':' will take all of the letters from index '-2' to the end of the string.
# the return line is required to return the new_word

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(s):
     if len(s) == 0:
         return s
     first_letter = s[0]
     result = s[0] + s[1:].replace(first_letter, '*')
     return result

# the if statement keeps the string unchanged if it is empty. 
# first_letter is variable created to store the first letter of the string. We need this so that the first letter is not lost once we change the letters to '*'
# s[1:] creates a substring. It is starting at index 1 (the second letter of the word). ':' goes to the end of the word. 
# 's[1:].replace(first_letter, '*')' uses the replace function to replace all occurrences of first_letter with '*' in the substring.
# 's[0] + ' adds the original first letter to the modified substring so that the first letter remains unchanged. 



# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

def mix_up(a, b):
    a_switched = b[:2] + a[2:]
    b_switched = a[:2] + b[2:]

    new_words = (a_switched + ' ' + b_switched)
    return new_words

# first line defines mix-up with two parameters (a,b). These parameters are placeholders for the values that you pass into the function when you call it. 
# for a_switched - b[:2]  extracts the first two letters from word 'b'. a[2:] extracts the remaining letters from 'a'. Adding them together gives us the new modified 'a' word.
# for b_switched - a[:2] extracts the first letter from word 'a'. b[2:] extracts the remaining letters from 'b'. Adding them together gives us the new modified 'b' word.
# the new_words variable is created to give us the new combined words. We need the ' ' added between the words to create a space between the words. 


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
