

def number_to_words(num):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num < 20:
        return words[num]
    if num < 100:
        return tens[(num // 10) - 2] + (("-" + words[num % 10]) if num % 10 != 0 else "")
    if num < 1000:
        return words[num // 100] + " hundred" + ((" " + number_to_words(num % 100)) if num % 100 != 0 else "")
    if num < 10000:
        return number_to_words(num // 1000) + " thousand" + ((" " + number_to_words(num % 1000)) if num % 1000 != 0 else "")

print(number_to_words(0)) # zero
print(number_to_words(5)) # five
print(number_to_words(8)) # eight
print(number_to_words(10)) # ten
print(number_to_words(21)) # twenty-one
print(number_to_words(77)) # seventy-seven
print(number_to_words(100)) # one hundred
print(number_to_words(303)) # three hundred three
print(number_to_words(555)) # five hundred fifty-five
print(number_to_words(2000)) # two thousand
print(number_to_words(3466)) # three thousand four hundred sixty-six
print(number_to_words(2400)) # two thousand four hundred




#code_Explaination
#The code defines a function number_to_words(num) that takes an integer num as an input and returns the string representation of the number written out as words. The function uses two lists words and tens that store the string representation of the numbers from 0 to 19 and the multiples of 10 from 20 to 90 respectively.

The function checks the value of num and returns the corresponding string representation of the number by calling itself recursively until num becomes a number smaller than 20.

The function first checks if num is smaller than 20. If so, it returns the string representation of num from the words list.

Next, it checks if num is smaller than 100. If so, it returns the string representation of num // 10 from the tens list and, if num % 10 is not equal to 0, the string representation of num % 10 from the words list, separated by a hyphen.

Then, it checks if num is smaller than 1000. If so, it returns the string representation of num // 100 from the words list followed by the string "hundred", and, if num % 100 is not equal to 0, the string representation of num % 100 obtained by calling the number_to_words() function recursively.

Finally, it checks if num is smaller than 10000. If so, it returns the string representation of num // 1000 obtained by calling the number_to_words() function recursively, followed by the string "thousand", and, if num % 1000 is not equal to 0, the string representation of num % 1000 obtained by calling the number_to_words() function recursively.

The code also includes several test cases that demonstrate the usage of the number_to_words() function.