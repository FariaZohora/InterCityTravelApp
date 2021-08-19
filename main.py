### Intercity Travelling App ###
import citylist


citylist.services()

nationality = input("Please enter your nationality: Bangladeshi or foreign").lower()
passID = None
if nationality=='bangladeshi':
    pass
elif nationality=='foreign':
    passID = input("Please enter your Passport number: ")

operation = input("Enter operation:")

while True:
    if operation=='1':
        passengers = input('Please enter the number of passengers:')
        location = input('Type your location:').upper()
        to = input('Type your destination:').upper()
        if citylist.cities().__contains__(to):
            print('Flights available for city',to)
        else:
            print('There are no trips available for this city.')
        print('You want to travel from',location,'to',to,'with',passengers,'number of passenger/s')
        citylist.get_info()
        break

    elif operation=='2':
        citylist.get_info()
        location = input('Where are you working from?')
        to = input('Where do you want to offer rides to?')
        cartype = input('What is your car type?')
        passengers = input('How many passengers can you take?')
        citylist.get_info()
        print('You can carry upto',passengers, 'passenger/s','in your',cartype,'from',location, 'to',to)
        break

    elif operation=='3':
        string = 'Information about application'\
                 '\nCreated in 2011, a travelling app that helps you find rides and offer rides to people'
        print(string)
        break

    elif operation==Q or operation==q:
        break