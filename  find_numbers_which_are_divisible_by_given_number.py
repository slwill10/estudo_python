def divisible_by(numbers, divisor):
    count = []
    for n in numbers:
        if n % divisor == 0:
            count.append(n)
    print(count)


divisible_by([1,2,3,4,5,6], 2), [2,4,6]
divisible_by([1,2,3,4,5,6], 3), [3,6]
divisible_by([0,1,2,3,4,5,6], 4), [0,4]
divisible_by([0], 4), [0]
divisible_by([1,3,5], 2), []