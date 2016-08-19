"""Each new term in the Fibonacci sequence is
generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms.

"""

import time

def main():

    time_a = time.clock()

    number_list = []
    n2 = 1
    n1 = 0

    while n2 < 4000000:

        n_saved = n2

        n2 = n2 + n1

        if n2 % 2 == 0:
            number_list.append(n2)

        n1 = n_saved

    elapsed_time = time.clock() - time_a

    print(elapsed_time)

    print(sum(number_list))

if __name__ == '__main__':
    main()