def one():
    cereal = ["cheerios", "lucky charms", "fruit loops", "rice krispies", "frosted flakes"]
    largest_element = cereal[0]
    for i in cereal:
        if i > largest_element:
            largest_element = i
    print(largest_element)

def two():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    sum = 0
    while i < len(numbers):
        sum = sum + numbers[i]
        i = i + 1
    average = sum / 10
    print(average)

def three():
    word = "level"
    palindrome = True
    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:
            palindrome = False
    if palindrome:
        print(f"{word} is a palindrome!")
    elif not palindrome:
        print(f"{word} is not a palindrome!")

def four():
    i = 0
    ratio = 2
    first_term = 2
    n = 12
    while i < n:
        print(first_term)
        first_term = first_term * ratio
        i = i + 1

def five(number):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, number]
    largest_element = list[0]
    second_largest_element = list[0]
    for i in list:
        if i > largest_element:
            second_largest_element = largest_element
            largest_element = i
        elif i > second_largest_element and i != largest_element:
            second_largest_element = i
    print(second_largest_element)

def six(number):
    i = 1
    factorial = 1
    while i <= number:
        factorial = factorial * i
        i = i + 1
    print(factorial)

def seven():
    number = 10
    perfect_square = False
    for i in range (1, number + 1):
        if i * i == number:
            perfect_square = True
    if perfect_square:
        print(f"{number} is a perfect square.")
    elif not perfect_square:
        print(f"{number} is not a perfect square.")

def eight(number):
    i = 2
    sum = 0
    while i <= number:
        is_prime = True
        divisor = i - 1
        while divisor > 1:
            if i % divisor == 0:
                is_prime = False
                break
            divisor = divisor - 1
        if is_prime:
            sum = sum + i
        i = i + 1
    print(sum)

def nine():
    sentence = "I am enjoying summer break!"
    words_in_sentence = sentence.split()
    number_of_words = 0
    for i in words_in_sentence:
        number_of_words = number_of_words + 1
    print(number_of_words)

def ten():
    list_1 = ["red", "orange", "yellow"]
    list_2 = ["yellow", "green", "blue", "purple"]
    i = 0
    while i < len(list_1):
        if list_1[i] in list_2:
            print(list_1[i])
        i = i + 1