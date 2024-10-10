def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
        
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5])) #should return -1 (because it appears 1 time)")
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))# should return 5 (because it appears 3 times)")
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) # should return 5 (because it appears 3 times)")
