
# Phase-3-Group-Project, 12/12/2023

## SNEAKER SHOP MANAGEMENT SYSTEM

## Authors

By:
- Pat Aloo
- Mark Mwangi
- Brian Cherus

## Table of Contents
- [Project Description](#project-description)
- [Key Features/MVP](#key-featuresmvp)
- [Setup/Installation Requirements](#setup/installation-requirements)
- [Known Bugs](#known-bugs)
- [Technologies Used](#technologies-used)
- [Support and contact details](#support-and-contact-details)
- [License](#license)

## Project Description

For this project, we are going to collaborate on building a Sneaker Shop Management System that runs from the Command Line.The system will be built using Python and ulitises class attributes and methods in addition to Object-relational mapping with SQLALchemy.

The system leverages SQLAlchemy ORM to interact with a well-structured database. It comprises of three interconnected tables:
1. Sneakers: Store details of sneakers, including brand, size, color, price, and availability.
2. Customers: Maintain customer information, such as names, contact details, and IDs.
3. Reviews: Associate reviews with specific customers and sneakers.

### Overview
The Sneaker Shop Management System provides a comprehensive solution for managing various aspects of a sneaker shop, including:
- Inventory Management: Easily add, update, and remove sneakers from the inventory.
- Customer Management: Maintain a database of customer information for seamless transactions.
- Review Tracking: Keep track of customer reviews associated with specific sneakers.

It provides the necessary features for the users to interact with the sneaker inventory and perform various actions.

## Key Features/MVP

### A user can:

#### Create: 
1. Create a new customer
2. Create a new sneaker
3. Create a new review associated with a particular customer and sneaker

#### Read: 
1. Retrieve details about a sneaker using its ID
2. Retrieve details about a customer using their ID
3. Fetch all the reviews associated with a particular customer/sneaker
4. Fetch all the unavailable sneakers for re-stock

#### Update: 
1. Modify a sneaker's price using its ID
2. Update a customer's information using their ID
3. Update the availability of a sneaker

#### Delete: 
1. Remove a sneaker by providing its ID
2. Delete a customer by providing their ID


## Setup/Installation Requirements

- Fork and clone the repository to your desired local folder.
- Open the folder with vs code.
- Navigate into the `alchemy` folder using the command `cd alchemy`
- Run `pipenv install` in your terminal to install all necessary   dependencies.
- Run `pipenv shell` in your terminal to enter into your virtual environment.
- Run the `test.py` file in your terminal by using the `lib/test.py` command.

- Congragulations! The application is  now up and successfully running.
       
## Known Bugs

- The application runs smoothly. No detected bugs.

## Technologies used

- Python
- SQLAlchemy
- Faker
- DateTime
- Terminal

## Support and contact details

1. Pat Aloo
- email :: aloemo77@gmail.com
- phone :: +254791488881

2. Mark Mwangi
- email :: mark.mwangi1@student.moringaschool.com
- phone :: +254770614345

3. Brian Cherus
- email :: brian.cherus@student.moringaschool.com
- phone :: +254720560979


## License

MIT License

Copyright (c) 2023 PAT L. ALOO, MARK MWANGI, BRIAN CHERUS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.```

