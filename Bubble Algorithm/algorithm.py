print("-----BUBBLE SORTING ALGORITHM-----")

numbers = []

insercao = True
while insercao:
    number = int(input("Type a number for the list (type -1 to see the sorted list): "))
    if(number == -1):
        insercao = False
    else:
        numbers.append(number)

swapped = True

while swapped:

    swapped = False

    for i in range(len(numbers) - 1):
        if (numbers[i] > numbers[i + 1]):
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)