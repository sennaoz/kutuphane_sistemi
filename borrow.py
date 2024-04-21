from datetime import datetime
space = " "

def findline(word):
    with open("isim-kitap-tarih.txt", "r") as file:
        for line in file:
            if word in line:
                return line.split(" ")
def borrow(name,book):
    date = datetime.now()

    with open("isim-kitap-tarih.txt","a",encoding="UTF-8") as file:
        file.write(name + space + book + space + date.strftime("%Y %m %d") + space + "\n")
def iade(book):
    returndate = datetime.now()
    returndate = returndate.strftime("%Y %m %d").split(" ")
    date = findline(book)[2:5]

    days = (int(returndate[0])*365 + int(returndate[1])*30 + int(returndate[2])) - (int(date[0])*365 + int(date[1])*30 + int(date[2]))

    if days > 30:
       print("30 gunluk sureyi asmissiniz! Isleminiz gerceklesemedi.")

def main():
    borrow("emirhanoguz","BatanGunes")
    iade("BatanGunes")

main()