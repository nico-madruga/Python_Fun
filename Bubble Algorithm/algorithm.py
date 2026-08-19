algorithm = [5, 2, 7, 3, 9, 8, 4, 6, 1]

index = -1

while algorithm != sorted(algorithm):

    index = -1

    for i in range(len(algorithm) - 1):
        index += 1
        current = algorithm[index]
        next = algorithm[index + 1]

        if (current > next):
            algorithm[index], algorithm[index + 1] = algorithm[index + 1], algorithm[index]

print(algorithm)

        

#       if(algorithm[index]) > algorithm[index + 1]:
#          algorithm[index], algorithm[index + 1] = algorithm[index + 1], algorithm[index]