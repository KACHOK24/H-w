class Order:
    def __init__(self):
        self.taomlar = []

    def taom_qoshish(self, nomi, narx,promokod, soni=1):
        self.taomlar.append({"nomi": nomi, "narx": narx, "soni": soni,"promokod":promokod})

    def jami_summa(self):
        summa = 0
        for taom in self.taomlar:
            summa += taom["narx"] * taom["soni"]
        return summa

    def yetkazish_narxi(self):
        if self.jami_summa() > 100000:
            return 0
        else:
         return 15000

    def toliq_tolov(self):
        return self.jami_summa() + self.yetkazish_narxi()
 
buyurtma = Order()
buyurtma.taom_qoshish("Choy", 111000, 3)
buyurtma.taom_qoshish("Osh", 75000, 2)
buyurtma.taom_qoshish("Choy", 5000, 1)

print("Taomlar summasi:", buyurtma.jami_summa())
print("Yetkazib berish:", buyurtma.yetkazish_narxi())
print("Jami to'lov:", buyurtma.toliq_tolov())