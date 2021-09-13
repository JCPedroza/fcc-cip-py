def num_to_fizz_buzz(num):
    fizz_buzz = ''
    if num % 3 == 0:
        fizz_buzz += 'Fizz'
    if num % 5 == 0:
        fizz_buzz += 'Buzz'
    return fizz_buzz if fizz_buzz else str(num)

fizz_buzz = lambda: [num_to_fizz_buzz(num) for num in range(1, 101)]
