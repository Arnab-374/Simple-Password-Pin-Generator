"""The following is the code base for the simple password/pin generator using the basic features of python programming language. This was created in an attempt
   to use all of the basic knowledge i have obtained after going through a python (basic) course.
   Created by: Arnab Bindu Laha
   Date: 03/13/2023
"""

#importing libraries
import random


"""
Main input function. This will allow the user to specify the type of password/pin they want generated using the code. For example: If the user wants a 6 digit
pin, they will specify that in this function and that input will be taken into consideration in the password/pin generator function below.
"""
def password_characteristics():
    #defining all of the necessary variables. This is necessary as otherwise if one option between password or pin is selected and no value is assigned to the other variables for the other options, the code will throw an error while returning values.
    type_of_password = ''
    length_of_pin = 0
    length_of_password = 0
    special_characters = ''
    numeric_values = ''
    capital_letters = ''
    
    #input method to understand if the user wants a password or a pin
    type_of_password = input('Would you like a password to be generated or a pin? Please type \'pw\' for password or \'p\' for pin. ')

    #if else statement to obtain more details pertaining to what should be the size of the password/pin
    if type_of_password == 'p':
        length_of_pin = input('What should be the length of the pin? Note: It can only be 4 digits or 6 digits. ')
        print('Understood. A pin of {} digits shall be generated.'.format(length_of_pin))
    elif type_of_password == 'pw':
        length_of_password = input('What should be the length of the password? Note: It can only be 8 characters or 16 characters. ')
        print('Understood. A password of {} characters shall be generated.'.format(length_of_password))
        print()
        #another input to understand whether the password can contain numeric values, special characters or capital letter
        special_characters = input('Should the password contain any one of the following special characters? Ex - @,*,&,#,\\. Note: Please type \'Y\' for Yes, \'N\' for No. ')    
        print()
        numeric_values = input('Should the password contain any numeric values such as 1, 2, 3, etc? Note: Please type \'Y\' for Yes, \'N\' for No. ')
        print()
        capital_letters = input('Should the password contain at least one capital letter? Note: Please type \'Y\' for Yes, \'N\' for No. ')
        #another if else statement to confirm the user of the characteristics of the password
        if special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'Y':
            print('Understood. The password will contain special characters, numeric values and at least one capital letter.')
        elif special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'Y':
            print('Understood. The password will only contain special characters and at least one capital letter, however it will not contain numeric values.')
        elif special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'Y':
            print('Understood. The password will only contain numeric values and at least one capital letter, but no special characters.')
        elif special_characters == 'N' and numeric_values == 'N' and capital_letters == 'Y':
            print('Understood. The password will only contain at least one capital letter but will not contain any special characters or numeric values.')
        elif special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'N':
            print('Understood. The password will contain special characters and numeric values but no capital letter.')
        elif special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'N':
            print('Understood. The password will only contain special characters, however it will not contain numeric values or capital letters.')
        elif special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'N':
            print('Understood. The password will only contain numeric values, but no special characters or capital letters.')
        elif special_characters == 'N' and numeric_values == 'N' and capital_letters == 'N':
            print('Understood. The password will not contain any special characters, numeric values or capital letters')
        else:
            #countermeasure for any wrong inputs provided by the user
            print('Please thoroughly re-check the input provided.')
            password_characteristics()
    else:
        print('Incorrect input.')
        password_characteristics()
            
    #return all of the input parameters as specified by the user
    return type_of_password, length_of_pin, length_of_password, special_characters, numeric_values, capital_letters


"""
Main password/pin generator function. This will allow the program to actually generate the password or pin as per the user.
"""

def password_generator():
    #calling the password_characteristics function to get the input provided by the user.
    type_of_password, length_of_pin, length_of_password, special_characters, numeric_values, capital_letters = password_characteristics()
    
    #defining the digits and characters which can be used to generate the pin or password depending on the user's selection
    digits = '0123456789'
    characters = 'abcdefghijklmnopqrstuvwxyz'
    capital_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    specials = '@*&#\\'

    #using if else statements to generate the password based on the user's input    
    if type_of_password == 'p':
        if length_of_pin == '4':
            #using the random method to generate a pin with the specified number of digits which is 4 in this case
            pin = ''.join(random.sample(digits, k = int(length_of_pin)))
        elif length_of_pin == '6':
            #using the random method to generate a pin with the specified number of digits which is 6 in this case
            pin = ''.join(random.sample(digits, k = int(length_of_pin)))
        #printing the generated pin
        print('Here is your {0} digit pin - {1}.'.format(length_of_pin, pin))
    elif type_of_password == 'pw':
        if length_of_password == '8':
            #if the password length is of 8 characters then depending on whether the user wants special characters, capital letters or numerical values
            #we'll have to come up with a password for all the possible scenarios keeping in mind that the password can only be 8 characters in length.
            if special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'Y':
                #for loop to obtain either 1 or 2 capital letter(s)
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    #depending on the number of capital letters either 3 or 2 normal characters will be considered at random
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 3))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 2))
                #only 1 special character will be selected at random
                special_character_in_password = ''.join(random.choice(specials))
                numeric_values_in_password = ''.join(random.sample(digits, k = 3))

                #joining all the values to generate the password for this particular sequence where the user wants capital letters, special character and
                #numeric values. using the string concatenation and the random function on a list to generate the password with all the values in random order.
                password = capital_letter_in_password + normal_letter_in_password + special_character_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 6))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 5))
                special_character_in_password = ''.join(random.choice(specials))
                
                password = capital_letter_in_password + normal_letter_in_password + special_character_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 4))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 3))
                numeric_values_in_password = ''.join(random.sample(digits, k = 3))

                password = capital_letter_in_password + normal_letter_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'N' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 7))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 6))
                
                password = capital_letter_in_password + normal_letter_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 4))
                special_character_in_password = ''.join(random.choice(specials))
                numeric_values_in_password = ''.join(random.sample(digits, k = 3))

                password = normal_letter_in_password + special_character_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 7))
                special_character_in_password = ''.join(random.choice(specials))
                
                password = normal_letter_in_password + special_character_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 5))
                numeric_values_in_password = ''.join(random.sample(digits, k = 3))

                password = normal_letter_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'N' and capital_letters == 'N':
                password = ''.join(random.sample(characters, k = 8))
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))
                
        elif length_of_password == '16':
            if special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'Y':
                #for loop to obtain either 1 or 2 capital letter(s)
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    #depending on the number of capital letters either 9 or 8 normal characters will be considered at random
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 9))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 8))
                #only 2 special character will be selected at random
                special_character_in_password = ''.join(random.sample(specials, k = 2))
                numeric_values_in_password = ''.join(random.sample(digits, k = 4))

                #joining all the values to generate the password for this particular sequence where the user wants capital letters, special character and
                #numeric values. using string concatenation and the random function on a list to generate the password with all the values in random order.
                password = capital_letter_in_password + normal_letter_in_password + special_character_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 13))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 12))
                special_character_in_password = ''.join(random.sample(specials, k = 2))
                
                password = capital_letter_in_password + normal_letter_in_password + special_character_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 11))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 10))
                numeric_values_in_password = ''.join(random.sample(digits, k = 4))

                password = capital_letter_in_password + normal_letter_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'N' and capital_letters == 'Y':
                for i in range(1,3):
                    capital_letter_in_password = ''.join(random.sample(capital_characters, k = i))
                    if i == 1:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 15))
                    else:
                        normal_letter_in_password = ''.join(random.sample(characters, k = 14))
                
                password = capital_letter_in_password + normal_letter_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'Y' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 10))
                special_character_in_password = ''.join(random.sample(specials, k = 2))
                numeric_values_in_password = ''.join(random.sample(digits, k = 4))

                password = normal_letter_in_password + special_character_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'Y' and numeric_values == 'N' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 14))
                special_character_in_password = ''.join(random.sample(specials, k = 2))
                
                password = normal_letter_in_password + special_character_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'Y' and capital_letters == 'N':
                normal_letter_in_password = ''.join(random.sample(characters, k = 12))
                numeric_values_in_password = ''.join(random.sample(digits, k = 4))

                password = normal_letter_in_password + numeric_values_in_password
                password_list = list(password)
                random.shuffle(password_list)
                password = ''.join(password_list)
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            if special_characters == 'N' and numeric_values == 'N' and capital_letters == 'N':
                password = ''.join(random.sample(characters, k = 16))
                print()
                print('Here is your {0} character password - {1}.'.format(length_of_password, password))

            

password_generator()

print()

restart = input('Would you like another password to be generated? Note: Please type \'Y\' for Yes, \'N\' for No. ')
while restart == 'Y':
    password_generator()
    
        
        
            
    

