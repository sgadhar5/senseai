# Project 1 -Linked List

This project involves developing a Java-based system for managing a product catalog using a custom singly linked list data structure. The objective is to allow an e-commerce company to efficiently manage their product details with operations to add, remove, search, and display products, ensuring that each product can be uniquely identified and accessed quickly. Here’s a more detailed breakdown of the components and functionalities:


**IDedObject Interface:**

An interface that defines two methods: getID(), which returns the unique identifier of any object implementing this interface, and printID(), which 
prints the details associated with the ID. This ensures that all objects in the list can be uniquely identified and manipulated based on their IDs.

**Product Class:**

A class representing the products in the e-commerce catalog. It implements the IDedObject interface, containing attributes such as productID, productName, and supplierName. Methods include getters and a method to print the product details, ensuring encapsulation and data integrity.

**MyLinkedList Class:**

A generic singly linked list class that stores objects of type AnyType, where AnyType extends IDedObject. This class includes methods to add a product at the front, remove the front product, find a product by ID, delete a specific product by ID, and print all products. This allows for efficient manipulation of the product list without relying on external libraries.

**Main Class:**

Contains the main method and manages user interactions. It uses a command-line interface to allow users to perform operations like adding a product, finding a product by ID, deleting a product, and printing all product records.

**Development Environment**


This project was developed using IntelliJ IDEA. No other IDEs were used to develop this project as per the constraints given in the assignment.

# Sample Run:

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 3
Enter Product ID: 100
Enter Product Name: Bananas
Enter Supplier Name: Dole
Product added.

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 2
Enter Product ID to find: 100
100
Bananas
Dole

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 3
Enter Product ID: 101
Enter Product Name: Apple
Enter Supplier Name: Honeyscrisp
Product added.

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 6
101
Apple
Honeyscrisp
100
Bananas
Dole

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 2
Enter Product ID to find: 101
101
Apple
Honeyscrisp

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 4
101
Apple
Honeyscrisp
First item deleted.

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 6
100
Bananas
Dole

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 1
List has been made empty.

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 6
List is empty

Operations on List:
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 7
Done.


