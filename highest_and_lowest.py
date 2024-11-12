def high_and_low(numbers):

    num_list = list(map(int, numbers.split()))

    
    high = max(num_list)
    low = min(num_list)
    
    print(f"{high} {low}")





high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9"
high_and_low("1 2 3"), "3 1"