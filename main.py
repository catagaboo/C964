# Gabriel Cata
# Student ID: 001104955

import csv
import HashMap
import package
import GraphDistance
import truck
import re


# Greedy Algorithm Method takes a list of packages, a graph, and a delivery truck - (O^N2)
# The algorithm increments time, distance, and visited nodes with each node that is visited,
# finding the shortest path to deliver the packages on the trucks
def deliver_shortest_route(packages, graph, delivery_truck):
    # This will repeat until all packages have been delivered
    while packages:
        # First package is preselected for comparison
        package_to_deliver = packages[0]
        for p in packages:
            # This checks all packages on the truck and finds the shortest path between the current
            # location and the package destination.
            if graph.get_distance(delivery_truck.node_index, p.node_index) < \
                    graph.get_distance(delivery_truck.node_index, package_to_deliver.node_index):
                package_to_deliver = p
        # This is the distance traveled between current location and closest node
        distance_traveled = float(graph.get_distance(delivery_truck.node_index, package_to_deliver.node_index))
        # This adds the distance traveled to the total miles the truck traveled
        delivery_truck.miles += distance_traveled
        # This updates the location of the truck to the nearest node
        delivery_truck.node_index = package_to_deliver.node_index
        # This updates the trucks time based on the 18mph speed of the truck and the distance traveled
        delivery_truck.time += distance_traveled / delivery_truck.speed
        # This updates the delivery time of the package with the current time
        package_to_deliver.delivery_time = delivery_truck.time
        # This updates the status of the package
        package_to_deliver.status = 'Package Delivered'
        # This removes the delivered package from truck
        packages.remove(package_to_deliver)


# Method returns the truck to the hub while updating the total miles the truck drove - O(1)
def return_to_hub(delivery_truck, graph):
    hub = '4001 South 700 East'
    distance_traveled = float(graph.get_distance(delivery_truck.node_index, 1))
    delivery_truck.miles += distance_traveled
    delivery_truck.time += distance_traveled / delivery_truck.speed


# Method takes a time in minutes and returns a time formatted "HH:MM AM/PM" - O(1)
def format_minutes(t):
    time_hours = int(t / 60)
    time_minutes = t % 60
    if t < 720:
        am_pm = "AM"
        formatted_time = "%d:%02d" % (time_hours, time_minutes)
    else:
        am_pm = "PM"
        formatted_time = "%d:%02d" % (time_hours - 12, time_minutes)
    return formatted_time + ' ' + am_pm


# Method takes a time in the format of "HH:MM AM/PM" and returns that time in minutes - O(1)
def time_to_minutes(t):
    parsed = t.split(':')
    hours = parsed[0]
    parsed2 = parsed[1].split(' ')
    minutes = parsed2[0]
    am_pm = parsed2[1]

    time_in_minutes = float(hours) * 60 + float(minutes)
    if am_pm.upper() == 'AM':
        return time_in_minutes
    elif am_pm.upper() == 'PM':
        return time_in_minutes + 720


# Method returns package information and status when user selects a time of day - O(1)
def lookup_package(selected_package, selected_time):
    statement = '| ' + "{:<4}".format(str(selected_package.id)) + '| ' + "{:<40}".format(str(selected_package.address)) \
                + '| ' + "{:<17}".format(str(selected_package.city)) + '| ' + "{:^6}".format(str(selected_package.zip)) \
                + '| ' + "{:^9}".format(str(format_minutes(selected_package.delivery_deadline))) + \
                '| ' + "{:<5}".format(str(selected_package.weight)) + '| '

    if selected_package is not None:
        # If package at the Hub
        if selected_time < selected_package.departure_time:
            statement1 = statement + 'At Hub'

            return statement1

        # If package is En Route
        elif selected_package.delivery_time > selected_time > selected_package.departure_time:
            statement2 = statement + 'En Route'

            return statement2

        # If package is Delivered
        elif selected_time >= selected_package.delivery_time:
            statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)

            return statement3


# Method returns initial package information when user selects to start program - O(1)
def add_packages(selected_package):
    statement = '| ' + "{:<4}".format(str(selected_package.id)) + '| ' + \
                "{:<40}".format(str(selected_package.address)) + '| ' + \
                "{:<17}".format(str(selected_package.city)) + '| ' + \
                "{:^8}".format(str(selected_package.zip)) + '| ' + \
                "{:^10}".format(str(format_minutes(selected_package.delivery_deadline)))

    return statement


class Main:
    # This creates the hashmap for packages
    hm = HashMap.HashMap()
    g = GraphDistance.Graph()

    # This imports the WGUPS_package.csv data - O(N)
    with open('WGUPS_packages.csv') as csv_file:
        packages_csv = csv.reader(csv_file, delimiter=',')
        for row in packages_csv:
            id = int(row[0])
            node_index = int(row[1])
            address = row[2]
            city = row[3]
            state = row[4]
            zip = row[5]
            dl = int(row[6])
            weight = int(row[7])
            status = 'At The Hub'

            # This creates package objects from csv file
            p = package.Package(id, node_index, address, city, state, zip, dl, weight, status)
            # This adds package objects to HashMap
            hm.add(p.id, p)

    # This adds all vertices to the adjacency matrix with the data from the csv file - O(N)
    with open('WGUPS_distance_table.csv') as csv_file:
        distance_csv = csv.reader(csv_file, delimiter=',')
        for row in distance_csv:
            id = int(row[0])
            name = row[1]
            address = row[2]
            city = row[3]
            state = row[4]
            zip = row[5]

            # This parses the csv to create vertex objects
            v = GraphDistance.Vertex(id, name, address, city, state, zip)
            # This adds vertex objects to the adjacency matrix
            g.add_vertex(v)

    # This adds all the edges and weights to adjacency matrix - O(N^2)
    with open('WGUPS_distance_table.csv') as csv_file:
        distance_csv = csv.reader(csv_file, delimiter=',')
        for row in distance_csv:
            vertex1_id = int(row[0])
            for i in range(6, 32):
                vertex2_id = i - 5
                edge_weight = row[i]
                g.add_edge(vertex1_id, vertex2_id, edge_weight)

    # This is the Start Menu to the program - O(N)
    # User must select an option to see data
    # To quit program user must select '4'
    while True:
        print('\n************************************************************')
        print('\t\t\tWELCOME TO THE WGUPS ROUTING PROGRAM \n')
        print('\t\t\t\t\tSTART MENU OPTIONS')
        print('************************************************************')

        print('\n\n (1) - Start Program and Load All packages for the day \n')
        print(' (2) - Individual Package Lookup \n')
        print(' (3) - Print Package Status at 3 different times \n')
        print(' (4) - Exit System\n')
        input1 = input('Please Select a Menu Option: ')

        # If user selects 'Start Program'
        if input1 == '1':
            # This creates the trucks
            truck1 = truck.Truck()
            truck2 = truck.Truck()

            truck1_departure_time = 480
            truck2_departure_time = 545

            # This manually groups the packages - O(N)
            packages1 = [
                hm.get(1), hm.get(2), hm.get(7), hm.get(8), hm.get(13), hm.get(14), hm.get(15), hm.get(16),
                hm.get(19), hm.get(20), hm.get(21), hm.get(29), hm.get(30), hm.get(33), hm.get(34), hm.get(39)
            ]

            packages2 = [
                hm.get(3), hm.get(4), hm.get(6), hm.get(10), hm.get(11), hm.get(12), hm.get(17), hm.get(18),
                hm.get(25), hm.get(26), hm.get(31), hm.get(32), hm.get(36), hm.get(37), hm.get(38), hm.get(40)
            ]

            packages3 = [
                hm.get(5), hm.get(9), hm.get(22), hm.get(23), hm.get(24), hm.get(27), hm.get(28), hm.get(35)
            ]

            # truck1 loads the packages
            truck1.packages = packages1
            for p in truck1.packages:
                p.delivery_time = truck1_departure_time
                p.departure_time = truck1_departure_time
                p.status = 'En Route'
            # truck1 delivers the packages
            truck1.time = truck1_departure_time
            deliver_shortest_route(truck1.packages, g, truck1)

            # truck2 loads the packages
            truck2.packages = packages2
            for p in truck2.packages:
                p.delivery_time = truck2_departure_time
                p.departure_time = truck2_departure_time
                p.status = 'En Route'
            # truck2 delivers the packages starting at 9:05AM
            truck2.time = truck2_departure_time
            deliver_shortest_route(truck2.packages, g, truck2)
            # truck1 returns to the hub
            return_to_hub(truck1, g)
            # truck1 loads the remaining packages
            # truck1 cannot leave until package #9 address is updated at 10:20AM
            truck1.time = 620
            truck1.packages = packages3
            for p in truck1.packages:
                p.time = truck1.time
                p.departure_time = truck1.time
                p.status = 'En Route'
            # truck1 delivers the remaining packages
            deliver_shortest_route(truck1.packages, g, truck1)
            # This prints the Header for all packages when packages are loaded into trucks
            print('________________________________________________________________________________________________')
            print('| ' + "{:<4}".format('ID') + '|' + "{:<39}".format(' ADDRESS') + '  | ' + "{:<16}".format('CITY') +
                  ' |  ' + "{:<7}".format('ZIP') + '| ' + "{:<9}".format('DELIVERY DEADLINE'))
            print('________________________________________________________________________________________________')
            for i in range(1, 41):
                print(add_packages(hm.get(i)))
            print('________________________________________________________________________________________________')
            print("\nAll Packages Loaded Successfully!\n")

        # if user selects 'Individual Package Lookup'
        elif input1 == '2':
            while True:
                # User asked to enter package ID to lookup
                package_id = int(input("\nPlease Enter the package ID# (1-40)  "
                                       "or Enter '0' to Exit: \n"))
                selected_package = hm.get(int(package_id))

                # if user enters '0' exit 'Individual Package Lookup'
                if package_id == 0:
                    print("\nExiting Individual Package Lookup!\n")
                    break

                # User is asked to enter the Time to check the status of the package
                elif selected_package is not None:
                    while True:
                        status_time = input("Please Enter the Time of the STATUS you want to check: "
                                            "(Example: 10:30 AM or 05:45 AM) \n")
                        format_check = re.match("[0-9][0-9]:[0-9][0-9] [A-Z][A-Z]", status_time)
                        # if format is entered correctly, print package info and status
                        if bool(format_check):
                            status_time = time_to_minutes(status_time)
                            print(
                                '________________________________________________________________________________________________________')
                            print('| ' + "{:<4}".format('ID') + '|' + "{:<39}".format(
                                ' ADDRESS') + '  | ' + "{:<16}".format('CITY') +
                                  ' | ' + "{:<6}".format('ZIP') + '|' + ' DEADLINE ' + '|WEIGHT' + '| STATUS')
                            print(
                                '________________________________________________________________________________________________________')
                            print(lookup_package(selected_package, status_time))
                            break
                        # else ask user to re-enter time correctly
                        else:
                            print("Please Enter Time In Correct Format (HH:MM AM -or- HH:MM PM)")
                # else ask user to enter a valid package ID (1-40)
                else:
                    print('Please select a valid package ID...\n')

        # if user selects 'Print All Packages Status at' at three different times
        elif input1 == '3':
            # This creates the trucks
            truck1 = truck.Truck()
            truck2 = truck.Truck()

            truck1_departure_time = 480
            truck2_departure_time = 545

            # This manually groups the packages - O(N)
            packages1 = [
                hm.get(1), hm.get(2), hm.get(7), hm.get(8), hm.get(13), hm.get(14), hm.get(15), hm.get(16),
                hm.get(19), hm.get(20), hm.get(21), hm.get(29), hm.get(30), hm.get(33), hm.get(34), hm.get(39)
            ]

            packages2 = [
                hm.get(3), hm.get(4), hm.get(6), hm.get(10), hm.get(11), hm.get(12), hm.get(17), hm.get(18),
                hm.get(25), hm.get(26), hm.get(31), hm.get(32), hm.get(36), hm.get(37), hm.get(38), hm.get(40)
            ]

            packages3 = [
                hm.get(5), hm.get(9), hm.get(22), hm.get(23), hm.get(24), hm.get(27), hm.get(28), hm.get(35)
            ]

            # truck1 loads the packages
            truck1.packages = packages1
            for p in truck1.packages:
                p.delivery_time = truck1_departure_time
                p.departure_time = truck1_departure_time
                p.status = 'En Route'
            # truck1 delivers the packages
            truck1.time = truck1_departure_time
            deliver_shortest_route(truck1.packages, g, truck1)

            # truck2 loads the packages
            truck2.packages = packages2
            for p in truck2.packages:
                p.delivery_time = truck2_departure_time
                p.departure_time = truck2_departure_time
                p.status = 'En Route'
            # truck2 delivers the packages starting at 9:05AM
            truck2.time = truck2_departure_time
            deliver_shortest_route(truck2.packages, g, truck2)
            # truck1 returns to the hub
            return_to_hub(truck1, g)
            # truck1 loads the remaining packages
            # truck1 cannot leave until package #9 address is updated at 10:20AM
            truck1.time = 620
            truck1.packages = packages3
            for p in truck1.packages:
                p.time = truck1.time
                p.departure_time = truck1.time
                p.status = 'En Route'
            # truck1 delivers the remaining packages
            deliver_shortest_route(truck1.packages, g, truck1)
            # Three different package status times
            status1 = 540
            status2 = 600
            status3 = 780
            # Prints the first package status data
            print(
                '\n********************************************************************************************************\n')
            print('All Package Status at ' + format_minutes(status1))
            print(
                '________________________________________________________________________________________________________')
            print('| ' + "{:<4}".format('ID') + '|' + "{:<39}".format(' ADDRESS') + '  | ' + "{:<16}".format('CITY') +
                  ' | ' + "{:<6}".format('ZIP') + '|' + ' DEADLINE ' + '|WEIGHT' + '| STATUS')
            print(
                '________________________________________________________________________________________________________')
            for i in range(1, 41):
                print(lookup_package(hm.get(i), status1))
            # Prints the second package status data
            print(
                '\n********************************************************************************************************\n')
            print('All Package Status at ' + format_minutes(status2))
            print(
                '________________________________________________________________________________________________________')
            print('| ' + "{:<4}".format('ID') + '|' + "{:<39}".format(' ADDRESS') + '  | ' + "{:<16}".format('CITY') +
                  ' | ' + "{:<6}".format('ZIP') + '|' + ' DEADLINE ' + '|WEIGHT' + '| STATUS')
            print(
                '________________________________________________________________________________________________________')
            for i in range(1, 41):
                print(lookup_package(hm.get(i), status2))
            # Prints the third package status data
            print(
                '\n********************************************************************************************************\n')
            print('All Package Status at ' + format_minutes(status3))
            print(
                '________________________________________________________________________________________________________')
            print('| ' + "{:<4}".format('ID') + '|' + "{:<39}".format(' ADDRESS') + '  | ' + "{:<16}".format('CITY') +
                  ' | ' + "{:<6}".format('ZIP') + '|' + ' DEADLINE ' + '|WEIGHT' + '| STATUS')
            print(
                '________________________________________________________________________________________________________')
            for i in range(1, 41):
                print(lookup_package(hm.get(i), status3))
            # This lets user know all packages have been delivered after the last status check
            print(
                '\n********************************************************************************************************\n')
            print("\nAll Packages Delivered Successfully!\n")
            # This prints the total miles driven by all trucks
            print('Total Miles: ' + str(truck1.miles + truck2.miles))

        # if user selects 'Exit'
        elif input1 == '4':
            print('\nThank You, Have a Nice Day!\n')
            break

        # if user input does not match menu options
        else:
            print('\nPlease Select a Valid Menu Option...\n')
