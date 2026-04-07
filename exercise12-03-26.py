# 1_NumericDataTypes_________________________________________________________

# x = 2
# print(x)
# print(type(x))

# Exercise 1
#print(type(5+2))

# x = (1 + 2) - (3 * 4)
# y = 2 * x
# z = 27 + x + y
# print("The value of x is", x, "the value of y is", y, "and the value of z is", z)

# x = 1.25
# print(x)
# print(type(x))

# Exercise 2
#print(type(5. + 2.))

# x = 3 + 2.5
# y = 2.5 * 3
# z = (1.5 + .5) // 2
# print("The value of x is", x, "the value of y is", y, "and the value of z is", z)

# x = 3 + int(2.5)
# print(x)
# print(type(x))

# x = 3 + int("REDI")
# print(x)
# print(type(x))

# x = 3 + int("10")
# print(x)
# print(type(x))


# 2_Strings_________________________________________________________________

# print("Ciao")

# print("Hello World")

# print("Aan;EA!@#2109412")

# print("""
#     In the midst of the journey of our life
# I found myself through a dark forest
# For the straight way was lost.
#     Ah me! how hard a thing it is to say
# What was this forest savage, rough, and stern,
# Which in the very thought renews the fear.
# Inferno, Canto I, Dante Alighieri
# https://poets.org/poem/inferno-canto-i
# """)

# print("")

# print('Hello World!',"Hello World!", '''Hello World!''', """Hello World!""")

# another_definition      = str()        
# yet_another_definition  = str("Ciao")  
# string_from_a_number    = str(15) 
# print( another_definition, yet_another_definition, string_from_a_number)

# first_string  = "pine"
# second_string = "apple"
# single_space  = " "
# len(first_string)                           
                                      
# print(first_string.replace('n', 'l'))      
                                     
# print(second_string.replace('p', '[]')) 
                                     
# print(first_string.find('i')) 

# print(second_string.count('p')) 
                                     
# print(first_string + second_string) 
                                     
# All collections in Python are zero-based. 
# lyric = "While my guitar gently weeps"
# len(lyric)
# print(lyric[5])
# print(lyric[15])
# print(lyric[25])  
# print(lyric[35])
# print(lyric[-5])
# print(lyric[-15])
# print(lyric[-25])  
# print(lyric[-35])                                         

# Exercise 1
# name = input()
# nickname = input()
# favoriteColor = input()

# print(name, "--", nickname, "--", favoriteColor)

# Exercise 2
# lore_ipsum_text = """Lorem Ipsum is simply dummy text of the printing 
#  and typesetting industry. Lorem Ipsum has been the industry's standard 
#  dummy text ever since the 1500s, when an unknown printer took a galley 
#  of type and scrambled it to make a type specimen book. It has survived 
#  not only five centuries, but also the leap into electronic typesetting, 
#  remaining essentially unchanged. It was popularised in the 1960s with 
#  the release of Letraset sheets containing Lorem Ipsum passages, and 
#  more recently with desktop publishing software like Aldus PageMaker 
#  including versions of lorem Ipsum."""

# print(lore_ipsum_text)

# 1) How many times the words "Lorem" and "Ipsum" appear in the text
# text1 = lore_ipsum_text.count("Lorem")
# text2 = lore_ipsum_text.count("Ipsum")
# print("The word 'Lorem' appears", text1, "times in the text.")
# print("The word 'Ipsum' appears", text2, "times in the text.")

# 2) The indexes of the first occurrence of the two words
# index1 = lore_ipsum_text.find("Lorem")
# index2 = lore_ipsum_text.find("Ipsum")
# print("The first occurrence of the word 'Lorem' is at index", index1)
# print("The first occurrence of the word 'Ipsum' is at index", index2)

# 3) (BONUS): The index of the last occurrence of the two words.
# index3 = lore_ipsum_text.rfind("Lorem")
# index4 = lore_ipsum_text.rfind("Ipsum")
# print("The last occurrence of the word 'Lorem' is at index", index3)
# print("The last occurrence of the word 'Ipsum' is at index", index4)

# 4) (BONUS): The strings "Lorem" and "lorem" both appear in the text, but 
# are considered different strings because of the capital/non-capital 
# letters. Find how many times the word appears *disregarding capitalization*.
# HINT: Search online for additional functions for strings to solve the 
# bonus exercises!
# text3 = lore_ipsum_text.lower().count("lorem")
# text4 = lore_ipsum_text.lower().count("ipsum")
# print("The word 'Lorem' appears", text3, "times in the text disregarding capitalization.")
# print("The word 'Ipsum' appears", text4, "times in the text disregarding capitalization.")

# Exercise 3
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# multiply = int(num1) * int(num2)
# print("The multiplication of the number", num1, "and", num2, "is", multiply)


# 3_TRUTH-VALUE______________________________________________

# bool_from_int   = bool(0)      
# print(bool_from_int)                               
# bool_from_float = bool(0.1)    
# print(bool_from_float)       
# bool_from_str   = bool('False')
# print(bool_from_str)

# a = 'ab' == 'ba' 
# b = 'ab' != 'ba' 
# c = .5   >  1.5  
# d = .5   <  1.5  
# e = 2    >= 3    
# f = 2    <= 3    
# print("a =", a)
# print("b =", b)
# print("c =", c)
# print("d =", d)
# print("e =", e)
# print("f =", f)  


# 4_CONDITIONS______________________________________________

# x = 10
# if x == 10:
#     print("The content of x is 10!")

# y = 1
# if y:
#     print("The integer y is evaluated as True, so it means that the value stored is not 0.")

# if True:
#     print("First line")
#     print("Second line")
#     x = 3 + 3 - 4
#     print("Third line... and content of the variable x:", x)

# if False:
#     print("First line")
#     print("Second line")
# x = 3 + 3 - 4
# print("Third line... and content of the variable x:", x)

# Exercise 1    
# name = input("Enter your first name: ")
# surname = input("Enter your last name: ")
# age = input("Enter your age: ")

# print("True" if name=="John" and surname=="Johnson" and age>="18" else "False")

# Exercise 2
# user_string = input("Enter any string: ")
# if len(user_string) > 3:
#     print("1")
# else:
#     print("0")

# Exercise 3
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# age = int(input("Enter your age: "))

# if first_name == "John" and last_name == "Johnson" and age >= 18:
#     print("True")
# else:    
#     print("False") 


# first_test  = True
# second_test = True
# if first_test:
#     print("first_test is True.")
# else:
#     if second_test:
#         print("first_test is False and second_test is True.")
#     else:
#         print("first_test and second_test are both False.")

# first_test  = True
# second_test = True
# if first_test:
#     print("first_test is True.")
# elif second_test:
#     print("first_test is False and second_test is True.")
# else:
#     print("first_test and second_test are both False.")

# warehouse_capacity = 1000
# warehouse_content  = 300
# if warehouse_content <= warehouse_capacity * 0.25:
#     print("Capacity in the warehouse: more than 75%")
# elif warehouse_content <= warehouse_capacity * 0.5:
#     print("Capacity in the warehouse: more than 50%")
# elif warehouse_content <= warehouse_capacity * 0.75:
#     print("Capacity in the warehouse: more than 25%")
# elif warehouse_content <= warehouse_capacity:
#     print("Attention! Less than 25% capacity in the warehouse!")
# else:
#     print("Warehouse capacity exceeded!")            

# Exercise 4
# gross_salary = float(input("What was your gross earnings for 2023: "))
# computed_tax = 0.0

# if 0 <= gross_salary <= 32000.00:
#     computed_tax = gross_salary * 0
# elif 32000.01 <= gross_salary <= 50000.00:
#     computed_tax = gross_salary * 0.15
# elif 50000.01 <= gross_salary <= 100000.00:
#     computed_tax = gross_salary * 0.25
# elif 100000.01 <= gross_salary <= 250000.00:
#     computed_tax = gross_salary * 0.37
# elif 250000.01 <= gross_salary <= 500000.00:
#     computed_tax = gross_salary * 0.42
# elif gross_salary > 500000.01:
#     computed_tax = gross_salary * 0.45

# print("The tax to be paid is", computed_tax)


# 5_LOOPS______________________________________________

# current_number = 1
# max_printed_number = 10
# while current_number <= max_printed_number:
#     print("Printing number...", current_number)
#     current_number += 1

# Exercise 1
# current_number = 5
# max_printed_number = 6
# if current_number > max_printed_number:
#     print("Too bad, this text will never see the light of day!")
# else:
#     while current_number <= max_printed_number:
#         print("Printing number...", current_number)
#         current_number += 1

# negative_number = -5
# while negative_number < 0:
#     print(f"{negative_number} ainda é negativo...")
#     negative_number += 1  # Incrementa para chegar ao 0

# print("Fim do loop!")

# lines_to_print = int(input("How many lines should be printed: "))
# lines_printed = 0
# while lines_printed < lines_to_print:
#     print("This is a line!:", lines_printed + 1)
#     lines_printed += 1 

# Exercise 2
# user_input = input("Enter any whole number: ")
# x = int(user_input)
# if x < 0:
#     print("Error: Please enter a positive number.")
# else:
#      even_number = 2
#      for i in range(x):
#          print(even_number)
#          even_number += 2
# for current_number in range(1, 11):
#     print("Printing number...", current_number)

# Exercise 3
# user_input = input("Enter any whole number: ")
# x = int(user_input) 
# if x < 0:
#     print("Error: Please enter a positive number.")
# else:
#     total = 0
#     for i in range(1, x + 1):
#         total += i
#     print(f"The sum of the first {x} numbers is {total}.")

# Exercise 4
user_input = input("Enter any whole number: ")
x = int(user_input)  
if x < 0:
    print("Error: Please enter a positive number.")
else:
    total = 0
    for i in range(1, x + 1):
        total += i
    print(f"The sum of the first {x} numbers is {total}.")