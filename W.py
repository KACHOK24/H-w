# FILENAME = "vazifa.txt"

# while True:
#     print("\n1. Vazifa qo'shish")
#     print("2. Vazifalarni ko'rish")
#     print("3. Vazifani o'chirish")
#     print("4. Chiqish")

#     choice = input("Tanlang: ")

#     if choice == "1":
#         task = input("Vazifani kiriting: ")
#         f = open(FILENAME, "a")
#         f.write(task + "\n")
#         f.close()
#         print("Vazifa qo'shildi!")

#     elif choice == "2":
#         f = open(FILENAME, "r")
#         print("Vazifalar ro'yxati:")
#         print(f.read())
#         f.close()

#     elif choice == "3":
#         f = open(FILENAME, "r")
#         tasks = f.readlines()
#         f.close()

#         print("Vazifalar ro'yxati:")
#         for i, t in enumerate(tasks, 1):
#             print(f"{i}. {t.strip()}")

#         num = input("O'chirish uchun raqamni kiriting: ")

#         try:
#             index = int(num) - 1
#             if 0 <= index < len(tasks):
#                 removed = tasks.pop(index)

#                 f = open(FILENAME, "w")
#                 f.writelines(tasks)
#                 f.close()

#                 print(f"O'chirildi: {removed.strip()}")
#             else:
#                 print("Bunday raqamli vazifa yo'q.")
#         except ValueError:
#             print("Bu raqam emas, xato!")

#     elif choice == "4":
#         print("Dasturdan chiqildi.")
#         break

#     else:
#         print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")
      