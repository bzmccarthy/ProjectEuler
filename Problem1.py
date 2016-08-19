# Project Euler Problem 1

"""

If we list all the natural numbers
below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples
is 23.

Find the sum of all the multiples
of 3 or 5 below 1000.

"""

limit = 1000
divisor_a = 3
divisor_b = 5

def main():

    #multiples = find_multiples()
    multiples = find_multiples2()
    answer = sum(multiples)
    print(answer)    

def find_multiples():

    multiples = []
    
    for integer in range(1,limit):

        if (integer % divisor_a == 0)\
           or (integer % divisor_b == 0):

            multiples.append(integer)

    return multiples

def find_multiples2():

    multiples = [i for i in range(1,limit) if i % divisor_a==0 or i % divisor_b == 0]

    return multiples

if __name__ == '__main__':
    main()
