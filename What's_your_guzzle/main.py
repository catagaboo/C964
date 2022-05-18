# Gabriel Cata
# Student ID: 001104955

import csv
import pandas as pd
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt

df = pd.read_csv('cocktails2.csv')

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)

class Main:

    # This is the Start Menu to the program
    # User must select an option to see data
    # To quit program user must select '4'
    while True:
        print('\n************************************************************')
        print("\t\t\t\t\tWhat's Your Guzzle? \n")
        print('\t\t\t\t\tSTART MENU OPTIONS')
        print('************************************************************')

        print('\n\n (1) - All Drinks \n')
        print(' (2) - Liquor selection\n')
        print(' (3) - Shot selection\n')
        print(' (4) - Let Me Pick a Drink for you!\n')
        print(' (5) - Exit System\n')
        input1 = input('Please Select a Menu Option: ')

        # If user selects 'Start Program'
        if input1 == '1':
            
            # This prints the Header for all Cocktails
            print('____________________________________________________________')
            pd.set_option('display.max_columns', None)
           # print(df.head(111))
           
           # Prints a list of all drinks to select from
            for index, row in df.iterrows():
                print(index, row ['Name'])
           
            print("\nAll Cocktails and Shots Loaded Successfully!\n")
            
            # This allows user to enter a cocktail name from list to see ingredients
            cocktail_name = input('Enter the Name of the Cocktail you want -or- Press ENTER to go back to MAIN menu: ')
            
            with open('cocktails2.csv') as csv_file:
                cocktails2_csv = csv.DictReader(csv_file)
                not_found = True
                for row in cocktails2_csv:
                    if cocktail_name == row['Name']:
                        not_found = False
                        print('\n{0:<10} \n{1:<10} \n{2:<10} \n{3:<10} \n{4:<10} \n{5:<10}'.format(row['Name'], row['Glass'], row['Main Alcohol'], row['Other Alcohols'], row['Mixes'], row['Garnish'] ))
                    
            if not_found:
                print('This does not exist')

        # This displays cocktails based on their main alcohol
        elif input1 == '2':
            df = pd.read_csv('cocktails2.csv', usecols= ['Name', 'Glass', 'Main Alcohol', 'Other Alcohols' ] )
            # This prints the Header for all Shots
            print('____________________________________________________________')
            #Drinks with vodka
            liquor_selection = df[(df['Main Alcohol'] == '1oz Vodka')]
            print(liquor_selection.head(19))
            
            print('____________________________________________________________')
            #Drinks with vodka
            liquor_selection = df[(df['Main Alcohol'] == '1/2oz Vodka')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with gin
            liquor_selection = df[(df['Main Alcohol'] == '1oz Gin')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with gin
            liquor_selection = df[(df['Main Alcohol'] == '2oz Gin/Vodka')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with tequila
            liquor_selection = df[(df['Main Alcohol'] == '1oz Tequila')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with rum
            liquor_selection = df[(df['Main Alcohol'] == '1oz Light Rum')]
            print(liquor_selection.head(20))
            
            print('____________________________________________________________')
            #Drinks with whiskey
            liquor_selection = df[(df['Main Alcohol'] == '1oz Whiskey')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with bourbon
            liquor_selection = df[(df['Main Alcohol'] == '1oz Bourbon')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with bourbon
            liquor_selection = df[(df['Main Alcohol'] == '2oz Bourbon')]
            print(liquor_selection.head(10))
            
            print('____________________________________________________________')
            #Drinks with bourbon
            liquor_selection = df[(df['Main Alcohol'] == '2oz Scotch')]
            print(liquor_selection.head(10))

            print("\nAll Cocktails Loaded Successfully!\n")

        # This displays all the shots with ingredients
        elif input1 == '3':
            df = pd.read_csv('cocktails2.csv', usecols= ['Name', 'Glass', 'Main Alcohol', 'Other Alcohols'] )
            # Prints shots status
            print('____________________________________________________________')
            print(df.tail(23))
            
            print("\nAll Shots Loaded Successfully!\n")
            
            
        # if user selects 'Exit'
        elif input1 == '4':
            print('\nI am going to ask a few questions, and with your answers\n')
            print('I will select a perfect drink for you! \n')
            print('\nLets get started!\n')
            print("""Would you like a...?
        1. Smooth drink
        2. Strong drink
            """)
            ans = input('Please Select an Option: (1 or 2): ')
            if ans == '1':
                  print('\nSmooth it is...\n')
                  print("""Now, what type of drink would you like...?
        1. Fruity Drink
        2. Sour Drink
        3. Bitter Drink
        4. Boozy Drink
             """)
                  ans2 = input('Please select an Option: (1, 2, 3, or 4): ')

                  if ans2 == '1':
                    print('Yum! ... Now, I will select a drink for your pleasure!\n')
                    #reads and loads the data
                    df = pd.read_csv('fruity_drink_type.csv')

                    # Uses KMode to predict a drink based on user selections
                    cluster = []
                    K = range(1,2)
                    for num_clusters in list(K):
                        kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                        clusters = kmode.fit_predict(df)
                        cluster.append(kmode.cost_)
                 
                    print('\nI predict you will enjoy this tasty cocktail!')
                    #prints cluster centroids
                    print('\n', kmode.cluster_centroids_, '\n')
                    
                  elif ans2 == '2':
                    print('Alrighty! ... Now, I will select a drink for your pleasure!\n')
                    #reads and loads the data
                    df = pd.read_csv('sour_drink_type.csv')

                    # Uses KMode to predict a drink based on user selections
                    cluster = []
                    K = range(1,2)
                    for num_clusters in list(K):
                        kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                        clusters = kmode.fit_predict(df)
                        cluster.append(kmode.cost_)
                 
                    print('\nI predict you will enjoy this tasty cocktail!')
                    #prints cluster centroids
                    print('\n', kmode.cluster_centroids_, '\n')
                    
                  elif ans2 == '3':
                    print('Ok then! ... Now, I will select a drink for your pleasure!\n')
                    #reads and loads the data
                    df = pd.read_csv('bitter_drink_type.csv')

                    # Uses KMode to predict a drink based on user selections
                    cluster = []
                    K = range(1,2)
                    for num_clusters in list(K):
                        kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                        clusters = kmode.fit_predict(df)
                        cluster.append(kmode.cost_)
                 
                    print('\nI predict you will enjoy this tasty cocktail!')
                    #prints cluster centroids
                    print('\n', kmode.cluster_centroids_, '\n')

                  elif ans2 == '4':
                    print('Must have been a long day! ... Now, I will select a drink for your pleasure!\n')
                    #reads and loads the data
                    df = pd.read_csv('boozy_drink_type.csv')

                    # Uses KMode to predict a drink based on user selections
                    cluster = []
                    K = range(1,2)
                    for num_clusters in list(K):
                        kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                        clusters = kmode.fit_predict(df)
                        cluster.append(kmode.cost_)
                 
                    print('\nI predict you will enjoy this tasty cocktail!')
                    #prints cluster centroids
                    print('\n', kmode.cluster_centroids_, '\n')
                    
                  else:
                    print('\n Not a Valid Choice Try again')
                    

            elif ans == '2':
                  print('\nStrong it is...\n')
                  print("""Now, what type of drink would you like...?
        1. Boozy Drink
        2. Sour Drink
        3. Bitter Drink
             """)
                  ans2 = input('Please select an Option: (1, 2, or 3): ')
                  
                  if ans2 == '1':
                      print('Yum! ... Now, I will select a drink for your pleasure!\n')
                      #reads and loads the data
                      df = pd.read_csv('boozy_drink_type_not.csv')

                      # Uses KMode to predict a drink based on user selections
                      cluster = []
                      K = range(1,2)
                      for num_clusters in list(K):
                          kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                          clusters = kmode.fit_predict(df)
                          cluster.append(kmode.cost_)
                   
                      print('\nI predict you will enjoy this tasty cocktail!')
                      #prints cluster centroids
                      print('\n', kmode.cluster_centroids_, '\n')
                    
                  elif ans2 == '2':
                      print('Alrighty! ... Now, I will select a drink for your pleasure!\n')
                      #reads and loads the data
                      df = pd.read_csv('sour_drink_type_not.csv')

                      # Uses KMode to predict a drink based on user selections
                      cluster = []
                      K = range(1,2)
                      for num_clusters in list(K):
                          kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                          clusters = kmode.fit_predict(df)
                          cluster.append(kmode.cost_)
                   
                      print('\nI predict you will enjoy this tasty cocktail!')
                      #prints cluster centroids
                      print('\n', kmode.cluster_centroids_, '\n')
                      
                  elif ans2 == '3':
                      print('Ok then! ... Now, I will select a drink for your pleasure!\n')
                      #reads and loads the data
                      df = pd.read_csv('bitter_drink_type_not.csv')

                      # Uses KMode to predict a drink based on user selections
                      cluster = []
                      K = range(1,2)
                      for num_clusters in list(K):
                          kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
                          clusters = kmode.fit_predict(df)
                          cluster.append(kmode.cost_)
                   
                      print('\nI predict you will enjoy this tasty cocktail!')
                      #prints cluster centroids
                      print('\n', kmode.cluster_centroids_, '\n')
                      
                  else:
                    print('\n Not a Valid Choice Try again')
                    
            else:
                  print('\n Not a Valid Choice Try again')
            break

        # if user selects 'Exit'
        elif input1 == '5':
            print('\nThank You, Have a Nice Day!\n')
            break
         
        # if user input does not match menu options
        else:
            print('\nPlease Select a Valid Menu Option...\n')
            
   