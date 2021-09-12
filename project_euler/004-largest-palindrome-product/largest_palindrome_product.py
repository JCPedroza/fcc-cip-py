reverse_str = lambda string: string[::-1]

is_num_palindrome = lambda num: str(num) == reverse_str(str(num))

ndigit_range = lambda ndigit: range(10**(ndigit - 1), 10**(ndigit))

def largest_palindrome_product(ndigit):
    ndigit_nums = ndigit_range(ndigit)
    palindrome_products = []

    for num in ndigit_nums:
        for factor in range(num, ndigit_nums[-1] + 1):
            product = num * factor
            if is_num_palindrome(product):
                palindrome_products.append(product)

    return max(palindrome_products)
