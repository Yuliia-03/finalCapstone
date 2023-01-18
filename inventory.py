from tabulate import tabulate
import sys

#========The beginning of the class==========
class Shoe:

    def __init__(self, country: str, code: str, product: str, cost: int, quantity: int):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f'Country {"-":>2} {self.country} \nCode {"-":>5} {self.code} \nProduct {"-":>2} {self.product} \nCost {"-":>5} {self.cost} \nQuantity - {self.quantity}\n'

    def get_data(self):
        return self.country, self.code, self.product, self.cost, self.quantity

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
headers1=['Country', 'Code', 'Product', 'Cost', 'Quantity']

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open('./T32/inventory.txt', 'r') as f: 
            for line in f.readlines()[1:]:
                new_element = line.split(',')
                new_element[-1].replace("\n", "")
                shoe_list.append(Shoe(new_element[0], new_element[1], new_element[2], new_element[3], new_element[4].replace("\n", "")))
    except FileNotFoundError as error:
            print("The file that you are trying to open does not exist")
            print(error)

def capture_shoes(country: str, code: str, product: str, cost: int, quantity: int):
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    shoe_list.append(Shoe(country, code, product, cost, quantity))

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    print(tabulate([list(shoe.get_data()) for shoe in shoe_list], headers=headers1))

def re_stock():

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    
    min_quantity = int(shoe_list[0].quantity)
    min_index = 0
    for i in range(1, len(shoe_list)):
        curr_el = int(shoe_list[i].quantity)
        if min_quantity > curr_el:
            min_quantity = curr_el
            
            # (+1 because the first line in file witn name of columns)
            min_index = i+1

    print(shoe_list[min_index])

    to_re_stock = input("Do you want to re-stock that shoes? Y/N: ")
    while to_re_stock != 'Y' and to_re_stock != 'N':
        to_re_stock = input("Sorry, we can't understand your answer. Do you want to re-stock that shoes? Y/N")
    
    if to_re_stock == 'Y':
        new_quantity = int(input("How many of the shoes would you like to add: "))
        new_quantity+= min_quantity

        lines = open('./T32/inventory.txt', 'r').readlines()
        lines[min_index] = lines[min_index][:-1*len(str(min_quantity))-1] + str(new_quantity) + "\n"
        out = open('./T32/inventory.txt', 'w')
        out.writelines(lines)
        out.close()
        
def seach_shoe(code: str):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    headers1.append('Total value')
    print(tabulate([list( (*shoe.get_data(), int(shoe.cost)*int(shoe.quantity)) ) for shoe in shoe_list], headers=headers1))

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    high_qty_index = Shoe('-', '-', '-', 0, 0)

    for i in shoe_list:
        if int(i.quantity) > int(high_qty_index.quantity):
            high_qty_index = i
    print("Shoe for sale:")
    print(high_qty_index)


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:

    menu_message = '''\nSelect one of the following Options below:
r  - Read data from file 'inventory.txt' and add to the list as a Shoe object
с  - Сreate a shoe object and append this object inside the shoe list
va - View all data
rs - Find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked
s  - Search for a shoe from the list using the shoe code
tv - Calculate the total value for each item
hq - determine the product with the highest quantity and print this shoe as being for sale
e  - Exit
: '''

    menu = input(f"{menu_message}").lower()


    if menu == 'r':
        
        read_shoes_data()
    
    elif menu == 'c':

        country = input('Enter shoe details: \nCountry: ')
        code = input('Code: ')
        product = input('Product: ')
        cost = int(input('Cost: '))
        quantity = int(input('Quantity: '))

        capture_shoes(country, code, product, cost, quantity)

    elif menu == 'va':
        
        view_all()

    elif menu == 'rs':

        re_stock()

    elif menu == 's':

        code = input('Enter the code: ')
        seach_shoe(code)

    elif menu == 'tv':

        value_per_item()
    
    elif menu == 'hq':

        highest_qty()

    elif menu == 'e':
        print('Goodbye!')
        sys.exit()
