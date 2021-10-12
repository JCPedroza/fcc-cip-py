def num_to_fb(num: int) -> str:
    fb = ''

    if num % 3 == 0:
        fb += 'Fizz'
    if num % 5 == 0:
        fb += 'Buzz'

    return fb or str(num)


def fizz_buzz() -> list[str]:
    return [num_to_fb(num) for num in range(1, 101)]
