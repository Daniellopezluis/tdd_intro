def FizzBuzz(num):
    if not num % 15:
        return "fizzbuzz"

    if not num % 3:
        return "fizz"

    if not num % 5:
        return "buzz"

    return num
