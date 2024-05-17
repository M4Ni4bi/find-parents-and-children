'''
python1402-project 1
main file
'''
from funcs import *  # import all functions

while True:
    try:
        file_name = input('\nPlease enter your xlsx file name or address:\nto exit program, enter number 0.\nYour ' #get file name from user
                          'choice: ')

        if file_name == '0':    #close program if the user type 0
            break
        else:
            father_of_dict = father_of(file_name) #get dictionaries from functions
            son_of_dict = son_of(file_name)
            while True:     
                user_input = input('To receive fathers children,enter number 1.\nTo receive childrens fathers, '    #ask users what they want 
                                   'enter number 2.\n''To calculate the required amount of parts, enter number 3.\n'
                                   'To Change file enter number 0.\n'
                                   'your choice: ')

                if user_input == '1':
                    while True:
                        try:
                            user_choice = input('enter a father name (to get all enter 0): ')   
                            if user_choice == '0':  #get all fathers and children then  show to user 
                                for i in father_of_dict:
                                    if not father_of_dict[i]:
                                        print(f'{i} has no child')
                                    else:
                                        temp_str = f'{i} is father of ' #a temporary string
                                        for j in father_of_dict[i]:
                                            temp_str = temp_str + f'{j} and '
                                        print(temp_str[:-4]) #print them but remove the final and
                                break
                            else:
                                temp_str = f'{user_choice} is father of '   #find the father in dictionary and give children
                                for i in father_of_dict[user_choice]:
                                    temp_str = temp_str + f'{i} and '
                                print(temp_str[:-4])
                                break
                        except:
                            print('ERROR!!\nPlease check that the father name is correct.\n'
                                  'Also check upper case and lower case characters.')
                elif user_input == '2':
                    while True:
                        try:
                            user_choice = input('enter a child name (to get all enter 0): ')
                            if user_choice == '0':  #give all children and their fathers
                                for i in son_of_dict:
                                    temp_str = f'{i} is son of '
                                    for j in son_of_dict[i]:
                                        temp_str = temp_str + f'{j} and'
                                    print(temp_str[:-4])
                                break
                            else:   #give fathers of the user choice child name
                                temp_str = f'{user_choice} is son of '
                                for i in son_of_dict[user_choice]:
                                    temp_str = temp_str + f'{i} and'
                                print(temp_str[:-4])
                                break
                        except:
                            print('ERROR!!\nPlease check that the father name is correct.\n'
                                  'Also check upper case and lower case characters.')
                elif user_input == '3':
                    while True:
                        try:
                            user_numb = int(input('Enter the number of final product: '))
                            total_numb_dict = total_numb(file_name,user_numb)  #use the function 3 and get needed_parts dictionary
                            for i_index,i in enumerate(total_numb_dict):
                                if i_index == 0:
                                    print(f'for {total_numb_dict[i]} of {i} you need:')
                                else:
                                    print(f'{total_numb_dict[i]} {i}')
                            break
                        except:
                            print('ERROR!!\nPlease check your choice.')
                elif user_input == '0': #change file name
                    break
                else:
                    print('ERROR!! invalid number')
    except:
        print('ERROR!!\nplease check your file name. ALSO enter .xlsx format.')
