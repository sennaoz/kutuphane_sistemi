from KutuphaneSistemi import BookLinkedList

admin_info = {"rabiaduygu": "1231", "senaozen" : "1232", "emirhanoguz" : "1233", "emirkara" : "1234"}

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
                choice = int(input("Kitap eklemek icin 1, Silmek icin 2 girin:"))
                while choice != 1 and choice != 2:
                    choice = int(input("Hatali Giris!! Kitap eklemek icin 1, Silmek icin 2 girin:"))
                else: 
                    book_list = BookLinkedList()
                    if choice == 1:
                        book_name = input("Kitabin Adini Girin:")
                        author = input("Kitabin Yazar Adini Girin:")
                        publisher = input("Kitabin Yayim Evini Girin:")
                        ispn = input("Kitap ISPN Girin:")
                        year = input("Kitabin Yayim Yilini Girin:")
                        quantity = input("Kitabin Miktarini Girin:")
                        
                        book_list.add_book(book_name,author,publisher,ispn,year,quantity)
                    else:
                        book_name = input("Silmek Istediğiniz Kitabin Adini Girin:")
                        book_list.delete_book(book_name)
    else:
        #Kullanici Islemleri
        pass
                        

            