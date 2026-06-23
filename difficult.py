def one():
    number = 12
    for factor in range(2, number + 1):
        if number % factor == 0:
            prime_factor = True
            
            for i in range(2, factor):
                if factor % i == 0:
                    prime_factor = False

            if prime_factor:
                print(factor)

def two():
    n = 20
    term_1 = 0
    term_2 = 1
    i = 1
    while i < n:
        next_term = term_1 + term_2
        term_1 = term_2
        term_2 = next_term
        i = i + 1
    print(term_1)

def three():
    string = "hello"
    string_1 = "bye"
    anagram = True
    for i in string:
        if i not in string_1:
            anagram = False
    if anagram:
        print(f"{string} is an anagram.")
    elif not anagram:
        print(f"{string} is not an anagram.")

def four():
    first = 2
    common_difference = 2
    n = 20
    i = 0
    while i < n:
        print(first)
        first = first + common_difference
        i = i + 1

def five(number):
    list = []
    for i in range(1, number + 1):
        list.append(i)
    if len(list) % 2 == 1:
        median = list[len(list) // 2]
    elif len(list) % 2 == 0:
        mid = list[len(list) // 2 - 1]
        mid1 = list[len(list) // 2]
        median = (mid + mid1) / 2
    print(median)
        
def six(number):
    sum = 0
    proper_divisor = 1
    while proper_divisor < number:
        if number % proper_divisor == 0:
            sum = sum + proper_divisor
        proper_divisor = proper_divisor + 1
    if sum == number:
        print(f"{number} is a perfect number!")
    elif sum != number:
        print(f"{number} is not a perfect number!")

def seven():
    number = 67676767
    number = str(number)
    sum = 0
    for i in number:
        sum = sum + int(i)
    print(sum)

def eight(number):
    sentence = "I love eating ice cream."
    split = sentence.split()
    longest = split[0]
    i = 0
    while i < len(split):
        if len(split[i]) > len(longest):
            longest = split[i]
        i = i + 1
    print(longest)

def nine():
    sentence = "The quick brown fox jumps over the lazy dog."
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pangram = True
    for i in alphabet:
        if i not in sentence.lower():
            pangram = False
    if pangram:
        print(f"{sentence} is a pangram!")
    elif not pangram:
        print(f"{sentence} is not a pangram!")

def ten():
    i = 2
    while i <= 1000:
        is_prime = True
        divisor = i - 1
        while divisor > 1:
            if i % divisor == 0:
                is_prime = False
                break
            divisor = divisor - 1
        if is_prime:
            print(i)
        i = i + 1
