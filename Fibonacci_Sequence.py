# --- My different attempts and variation of the Fibonacci Sequence --- #


# --- Final iteration --- #
def fib_seq(number):
    fib_list = []
    [fib_list.append(n) if n < 2 else fib_list.append(fib_list[-2] + fib_list[-1]) for n in range(int(number) + 1)]
    return fib_list


up_to_number = input('Stop at what number? ')
print(fib_seq(up_to_number))


# --- My first attempt --- #
def fib(factors):
    fib_seq = [0, 1]
    a = 0
    b = 1
    for _ in range(factors):
        c = a + b
        a = b
        b = c
        fib_seq.append(c)
    return fib_seq


factors = input('Stop at what number? ')
print(fib(factors - 1))


# --- This one only works up to 30 or so --- #
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

  
up_to = input('Stop at what number? ')
x = [fib(n) for n in range(int(up_to) + 1)]
print(x)

# --- Attempt using a List --- #
fib_seq = [0, 1]
up_to = input('Stop at what number? ')
for n in range(2, int(up_to)+1):
    fib_seq.append(fib_seq[n-1]+fib_seq[n-2])
print(fib_seq)

# --- Attempt using dictionary instead --- #
def fib(n):
    if n in fib_seq:
        return fib_seq[n]
    elif n < 2:
        return n
    else:
        calc = fib(n - 1) + fib(n - 2)
        fib_seq[n] = calc
    return fib_seq[n]


fib_seq = {}
up_to_number = input('Stop at what number? ')
print([fib(n) for n in range(int(up_to_number)+1)])
