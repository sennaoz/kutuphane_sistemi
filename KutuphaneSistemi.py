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

    def modify_book(self, book_name, new_author, new_publisher, new_ispn, new_year, new_quantity):
        current = self.head
        while current:
            if current.book_name == book_name:
                current.author = new_author
                current.publisher = new_publisher
                current.ispn = new_ispn
                current.year = new_year
                current.quantity = new_quantity
                print(f"Kitap '{book_name}' bilgileri basariyle guncellendi.")
                return
            current = current.next
        print(f"Kitap '{book_name}' bulunmadi.")

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

admin_info = {"rabiaduygu": "1231", "senaozen" : "1232", "emirhanoguz" : "1233", "emirkara" : "1234"}
user_info = {"ali": "1111", "ayse": "2222"}
print(admin_info)
admin_info.update
print(admin_info)

hold = int(input("Admin icin 1, Kullanici icin 2 Girin:"))
#print(type(hold))
while hold!=1 and hold!=2:
    print("Hatali Giris")
    hold = int(input("Admin icin 1, Kullanici icin 2 Girin:"))
else:
    if hold==1:
        username = input("Lutfen admin adinizi girin:")
        #userpw = input("Lutfen sifrenizi girin:")
        while username!="rabiaduygu" and username!="senaozen" and username!="emirhanoguz" and username!="emirkara":
            print("Bu adda bir admin bulunamadi.")
            username = input("Lutfen farkli bir admin adi girin:")
        else:
            userpw = input("Lutfen sifrenizi girin:")
            while admin_info[username] != userpw:
                userpw = input("Sifre yanlis!! Lutfen yeniden sifre girin:")
            else:
                choice = int(input("Kitap eklemek icin 1, Silmek icin 2, Bilgileri güncellemek için 3, Admin ekleme-silme-guncelleme için 4, Kullanici ekleme-silme-guncelleme için 5 Girin:"))
                while choice != 1 and choice != 2 and choice != 3 and choice!= 4:
                    choice = int(input("Hatali Giris!! Kitap eklemek icin 1, Silmek icin 2, Bilgileri güncellemek için 3 girin:"))
                else: 
                    
                    if choice == 1:
                        book_name = input("Kitabin Adini Girin:")
                        author = input("Kitabin Yazar Adini Girin:")
                        publisher = input("Kitabin Yayim Evini Girin:")
                        ispn = input("Kitap ISPN Girin:")
                        year = input("Kitabin Yayim Yilini Girin:")
                        quantity = input("Kitabin Miktarini Girin:")
                        
                        book_list.add_book(book_name,author,publisher,ispn,year,quantity)
                    elif choice==2:
                        book_name = input("Silmek Istediğiniz Kitabin Adini Girin:")
                        book_list.delete_book(book_name)
                    elif choice==3:
                        book_name = input("Bilgilerini guncellemek istediginiz kitap ismi girin:")
                        new_author = input("Yeni Yazar Girin:")
                        new_publisher = input("Yeni Yayim Evi Girin ya da 'Same' Girin:")
                        new_ispn = input("Yeni ISPN Girin ya da 'Same' Girin:")
                        new_year = input("Yeni ISPN Girin ya da 'Same' Girin:")
                        new_quantity = input("Yeni ISPN Girin ya da 'Same' Girin:")
                        
                        book_list.modify_book(book_name, new_author, new_publisher, new_ispn, new_year, new_quantity)
                    elif choice==4:
                        #Dictioanry üszerinde tutulunca data güncllenemiyor. Bağlı liste olarak tutulmalı.
                        """
                        hold = int(input("Admin Eklemek icin 1, Silmek icin 2, Guncellemek icin 3 Girin:"))
                        if hold==1:
                            new_admin_key = input("Yeni Admin Kullanici Adi Girin: ")
                            new_admin_pw = input("Yeni Admin Sifre Girin: ")
                            admin_info[new_admin_key] = new_admin_pw
                        elif hold==2:
                            admin_key = input("Silmek Istediğiniz Admin Adi Girin: ")
                            del admin_info[admin_key]
                        elif hold==3:
                            admin_key = input("Sifresini Guncellemek Istediginiz Admin Adi Girin:")
                            if admin_key in admin_info:
                                admin_info[admin_key] = input("Lutfen Yeni Sifre Girin:")
                        """
                    elif choice==5:
                        """
                        hold = int(input("Kullanici Eklemek icin 1, Silmek icin 2, Guncellemek icin 3 Girin:"))
                        if hold==1:
                            new_user_key = input("Yeni Kullanici Kullanici Adi Girin: ")
                            new_user_pw = input("Yeni Kullanici Sifre Girin: ")
                            admin_info[new_user_key] = new_user_pw
                        elif hold==2:
                            user_key = input("Silmek Istediğiniz Kullanici Adi Girin: ")
                            del user_info[user_key]
                        elif hold==3:
                            user_key = input("Sifresini Guncellemek Istediginiz Kullanici Adi Girin:")
                            if user_key in admin_info:
                                user_info[user_key] = input("Lutfen Yeni Sifre Girin:")
                        """
                    else:
                        print("ERROR!")

    else:
        #Kullanici Islemleri
        pass

"""
book_list.add_book("Python Programming", "John Doe", "Tech Publishing", "AB67345", "1998", "12")
book_list.add_book("Data Structures and Algorithms", "Jane Smith", "Coding Books Inc.", "ZM87456", "2001", "5")
book_list.add_book("Machine Learning Basics", "Alice Johnson", "AI Press", "WG29345", "2011", "3")
book_list.add_book("Python Programming", "John Doe", "Tech Publishing", "AB67345", "1998", "12")
book_list.add_book("Data Structures and Algorithms", "Jane Smith", "Coding Books Inc.", "ZM87456", "2001", "5")
"""
book_list.export_to_csv("books.csv")
print("Books exported to 'books.csv' successfully.")