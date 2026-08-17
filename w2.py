class ATM:
    def __init__(self, parol, balans):
        self.parol = parol
        self.balans = balans

    def kirish(self):
        try:
            kiritilgan_parol = input("Parolni kiriting: ")
            if kiritilgan_parol == self.parol:
                print("Prol togri")
                self.menu()
            else:
                raise ValueError("Parol notog'ri")
        except ValueError as xato:
            print(f"Xatolik: {xato}")

    def menu(self):
        while True:
            print("\n1 - Balansni korish")
            print("2 - Balansga pul qoshish")
            print("3 - Chiqish")
            tanlov = input("Tanlovingiz: ")

            if tanlov == "1":
                print(f"Sizning balansingiz: {self.balans} so'm")
            elif tanlov == "2":
                try:
                    summa = float(input("Qoshmoqchi bolgan summa: "))
                    if summa <= 0:
                        raise ValueError("Summa musbat bo'lishi kerak")
                    self.balans += summa
                    print(f"Qo'shildi Yangi balans: {self.balans} so'm")
                except ValueError as xato:
                    print(f"Xatolik: {xato}")
            elif tanlov == "3":
                print("Xayr")
                break
            else:
                print("Noto'g'ri tanlov")


if __name__ == "__main__":
    atm = ATM(parol="1234", balans=1000)
    atm.kirish()