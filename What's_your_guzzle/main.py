# Gabriel Cata
# Student ID: 001104955

import csv
import cocktails
import pandas as pd

df = pd.read_csv('cocktails2.csv')


pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)


class Main:
  
    # This imports the cocktails2.csv data
    # with open('cocktails2.csv') as csv_file:
    #     cocktails2_csv = csv.reader(csv_file, delimiter=',')
    #     for row in cocktails2_csv:
    #         name = (row[0])
    #         glass = (row[1])
    #         main_alcohol = row[2]
    #         other_alcohol = row[3]
    #         mixes = row[4]
    #         garnishes = row[5]

    #         # This creates cocktail objects from csv file
    #         c = cocktails.Cocktails(name, glass, main_alcohol, other_alcohol, mixes, garnishes)
           

    # This is the Start Menu to the program
    # User must select an option to see data
    # To quit program user must select '4'
    while True:
        print('\n************************************************************')
        print("\t\t\t\t\tWhat's Your Gultch? \n")
        print('\t\t\t\t\tSTART MENU OPTIONS')
        print('************************************************************')

        print('\n\n (1) - All Drinks \n')
        print(' (2) - Liquor selection\n')
        print(' (3) - Shot selection\n')
        print(' (4) - Exit System\n')
        input1 = input('Please Select a Menu Option: ')

        # If user selects 'Start Program'
        if input1 == '1':
            
            # This prints the Header for all Cocktails
            print('____________________________________________________________')
            pd.set_option('display.max_columns', None)
        #    print(df.head(111))
            for index, row in df.iterrows():
                print(index, row ['Name'])
           
            print("\nAll Cocktails and Shots Loaded Successfully!\n")
            
            cocktail_name = input('Enter the Name of the cocktail you want: ')
            
            with open('cocktails2.csv') as csv_file:
                cocktails2_csv = csv.DictReader(csv_file)
                not_found = True
                for row in cocktails2_csv:
                    if cocktail_name == row['Name']:
                        not_found = False
                        print('{0:<10} |{1:<10} |{2:<10} | {3:<10} |{4:<10} |{5:<10}'.format(row['Name'], row['Glass'], row['Main Alcohol'], row['Other Alcohols'], row['Mixes'], row['Garnish'] ))
                    
            if not_found:
                print('This does not exist')

        # if user selects 'All Cocktails'
        elif input1 == '2':
            # This prints the Header for all Shots
            print('____________________________________________________________')
            #Drinks with vodka
            liquor_selection = df[(df['Main Alcohol'] == 'Vodka')]
            print(liquor_selection.head(111))
            
            print('____________________________________________________________')
            #Drinks with tequila
            liquor_selection = df[(df['Main Alcohol'] == 'Tequila')]
            print(liquor_selection.head(111))
            
            print('____________________________________________________________')
            #Drinks with gin
            liquor_selection = df[(df['Main Alcohol'] == 'Gin')]
            print(liquor_selection.head(111))
            
            print('____________________________________________________________')
            #Drinks with rum
            liquor_selection = df[(df['Main Alcohol'] == 'Light Rum')]
            print(liquor_selection.head(111))
            
            print('____________________________________________________________')
            #Drinks with whiskey
            liquor_selection = df[(df['Main Alcohol'] == 'Whiskey')]
            print(liquor_selection.head(111))
            
            print('____________________________________________________________')
            #Drinks with bourbon
            liquor_selection = df[(df['Main Alcohol'] == 'Bourbon')]
            print(liquor_selection.head(111))

            print("\nAll Cocktails Loaded Successfully!\n")

        # if user selects 'Shots' shot selection displayed
        elif input1 == '3':
           
            # Prints shots status
            print('____________________________________________________________')
            print(df.tail(24))
            print("\nAll Shots Loaded Successfully!\n")
            
            
        # if user selects 'Exit'
        elif input1 == '4':
            print('\nThank You, Have a Nice Day!\n')
            break

        # if user input does not match menu options
        else:
            print('\nPlease Select a Valid Menu Option...\n')
