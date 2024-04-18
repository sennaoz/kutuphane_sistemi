<<<<<<< HEAD:import csv.py
import csv


class Node:
    def __init__(self, book_name, author, publisher):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        self.next = None



class BookLinkedList:
    def __init__(self):
        self.head = None



    def add_book(self, book_name, author, publisher):
        new_book = Node(book_name, author, publisher)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book

    def display_books(self):
        current = self.head
        while current:
            print(f"Book Name: {current.book_name}, Author: {current.author}, Publisher: {current.publisher}")
            current = current.next

    def delete_book(self, book_name):
        current = self.head
        if current is not None and current.book_name == book_name:
            self.head = current.next
            current = None
            return
        
        while current is not None:
            if current.book_name == book_name:
                break
            prev = current
            current = current.next
        if current == None:
            print(f"Book '{book_name}' not found in the library.")
            return
        prev.next = current.next
        current = None

    def export_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book Name", "Author", "Publisher"])
            current = self.head
            while current:
                writer.writerow([current.book_name, current.author, current.publisher])
                current = current.next

# Example usage:
book_list = BookLinkedList()
book_list.add_book("Python Programming", "John Doe", "Tech Publishing")
book_list.add_book("Data Structures and Algorithms", "Jane Smith", "Coding Books Inc.")
book_list.add_book("Machine Learning Basics", "Alice Johnson", "AI Press")
book_list.display_books()
book_list.delete_book(book_name="Python Programming")
book_list.display_books()
# Export to CSV file
book_list.export_to_csv("books.csv")
print("Books exported to 'books.csv' successfully.")
=======
import csv

class Node:
    def __init__(self, book_name, author, publisher, ispn, year, quantity):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        self.ispn = ispn
        self.year = year
        self.quantity = quantity
        self.next = None

class BookLinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, book_name, author, publisher, ispn, year, quantity):
        new_book = Node(book_name, author, publisher, ispn, year, quantity)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book

    def display_books(self):
        current = self.head
        while current:
            print(f"Book Name: {current.book_name}, Author: {current.author}, Publisher: {current.publisher}, ISPN: {current.ispn}, Year: {current.year}, Quantity: {current.quantity}")
            current = current.next

    def delete_book(self, book_name):
        current = self.head
        if current is not None and (current.book_name == book_name):
            self.head = current.next
            current = None
            return
        while current is not None:
            if current.book_name == book_name:
                break
            prev = current
            current = current.next
        if current == None:
            print(f"Book '{book_name}' not found in the library.")
            return
        prev.next = current.next
        current = None

    def export_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book Name", "Author", "Publisher", "ISPN", "Year", "Quantity"])
            current = self.head
            while current:
                writer.writerow([current.book_name, current.author, current.publisher, current.ispn, current.year, current.quantity])
                current = current.next


book_list = BookLinkedList()
print(type(book_list))
"""
book_list.add_book("Python Programming", "John Doe", "Tech Publishing", "AB67345", "1998", "12")
book_list.add_book("Data Structures and Algorithms", "Jane Smith", "Coding Books Inc.", "ZM87456", "2001", "5")
book_list.add_book("Machine Learning Basics", "Alice Johnson", "AI Press", "WG29345", "2011", "3")
book_list.add_book("Python Programming", "John Doe", "Tech Publishing", "AB67345", "1998", "12")
book_list.add_book("Data Structures and Algorithms", "Jane Smith", "Coding Books Inc.", "ZM87456", "2001", "5")
"""
#book_list.display_books()
#book_list.delete_book(book_name="Python Programming")
#book_list.display_books()

book_list.export_to_csv("books.csv")
print("Books exported to 'books.csv' successfully.")
>>>>>>> 709e393 (ilk):KutuphaneSistemi.py
