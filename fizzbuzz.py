def fizzbuzz(number, fizz, buzz):
    if number%fizz == 0:
        if number%buzz == 0:
            print('FizzBuzz')
            return
        print('Fizz')
        return
    if number%buzz == 0:
        print('Buzz')
        return
    print(number)

for i in range(1, 100):
    fizzbuzz(i, 3, 5)