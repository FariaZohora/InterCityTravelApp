def cities():
    city_list = ["DHAKA","CHITTAGONG","RAJSHAHI","KHULNA","SYLHET","RONGPUR","COXS BAZAAR"]
    return city_list

def get_info():
    firstname = input('Write your firstname:')
    lastname = input('Write your last name:')
    email = input('Write your email address:')
    phone = input('Write your phone number:')
    req = input('Enter your requirements, Smoking YES/NO, Luggage YES/NO, Meal YES/NO, Pets YES/NO')
    print('Name:',firstname,lastname,'\nYour travelling requirements are:',req,)


def services():
    print("1. Find ride\n"
          "2. Offer ride\n"
          "3. How it works\n"
          "Q. Quit Application")
