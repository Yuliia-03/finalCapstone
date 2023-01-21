# finalCapstone

##### Let us assume that you work for a Nike warehouse. As store 
##### manager you are responsible for managing the warehouse, and 
##### more importantly, performing stock taking. To optimise your 
##### delivery time and for improved organisation, you have decided 
##### to use your Python knowledge to get an overview of what each 
##### stock-taking session entailed.
#
##### Nike warehouses store the following information for each stock-taking list:
##### ● Country
##### ● Code
##### ● Product
##### ● Cost
##### ● Quantity
##### ● Value
#
##### Other store managers (in other regions) would like to be able to 
##### use your program to do the following:
##### ● Search products by code.
##### ● Determine the product with the lowest quantity and restock it.
##### ● Determine the product with the highest quantity.
##### ● Calculate the total value of each stock item. The total value is 
##### calculated by multiplying the cost by the quantity for each item 
##### entered into the system.
#
#### This program allows the user to read data about shoes in
#### the warehouse and perform the following operations:
#
##### ● read_shoes_data - This function will open the file
##### inventory.txt and read the data from this file, then create a
##### shoes object with this data and append this object into the
##### shoes list. One line in this file represents data to create one
##### object of shoes. 
#
##### ● capture_shoes - This function will allow a user to capture
##### data about a shoe and use this data to create a shoe object
##### and append this object inside the shoe list.
#
##### ● view_all - This function will iterate over the shoes list and
##### print the details of the shoes returned from the __str__
##### function.
#
##### ● re_stock - This function will find the shoe object with the
##### lowest quantity, which is the shoes that need to be
##### re-stocked. Ask the user if they want to add this quantity of
##### shoes and then update it. This quantity should be updated
##### on the file for this shoe.
#
##### ● seach_shoe - This function will search for a shoe from the list
##### using the shoe code and return this object so that it will be
##### printed.
#
##### ● value_per_item - This function will calculate the total value
##### for each item.
##### value = cost * quantity. Print this information on the console
##### for all the shoes.
#
##### ● highest_qty - Determine the product with the
##### highest quantity and print this shoe as being for sale.
## Installation

> Repo includes a file named ```requirements.txt``` to automate the 
> installation of the project’s requirements
