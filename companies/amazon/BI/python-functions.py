

 def pallindrome(inp):

     inp = list(str(inp))
     indexes = list(range(len(inp)))
     indexes_rev = list(range(len(inp)-1, -1, -1))

     for (begin_itr, end_itr) in zip(indexes, indexes_rev):

         if inp[begin_itr] != inp[end_itr]:
             return False

     return True


 
def fibinocci(n):

    if n < 0:
        return "Wrong input!"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibinocci(n-1) + fibinocci(n-2)


def print_fib(limit):

    print([fibinocci(i) for i in range(1, limit+1)])



