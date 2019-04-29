import os


# 先取得該檔案夾內所有的檔案名稱
def get_list():
    all_name = os.listdir()
    return all_name

# 對所有的檔案名稱做 for 迴圈，訂定你的命名規則
for i in get_list():
    if "Black_Tea" in i:
        path = i.replace("Black_Tea", "Drink_Box_1")
    if "Coffee_Milk" in i:
        path = i.replace("Coffee_Milk", "Drink_Box_2")
    if "Green_Milk_Tea" in i:
        path = i.replace("Green_Milk_Tea", "Drink_Box_3")
    if "Lemon_Tea" in i:
        path = i.replace("Lemon_Tea", "Drink_Box_4")
    if "LS_Soymilk" in i[0:10]:
        path = i.replace("LS_Soymilk", "Drink_Box_5")
    if "Ocean_Spray" in i:
        path = i.replace("Ocean_Spray", "Drink_Box_6")
    if "Oolong_Milk_Tea" in i:
        path = i.replace("Oolong_Milk_Tea", "Drink_Box_7")
    if "Purple" in i:
        path = i.replace("Purple", "Drink_Box_8")
    if "Soymilk" in i[0:7]:
        path = i.replace("Soymilk", "Drink_Box_9")
    if "Cheers" in i:
        path = i.replace("Cheers", "Drink_Bottle_1")
    if "Family_Water" in i:
        path = i.replace("Family_Water", "Drink_Bottle_2")
    if "LP33" in i:
        path = i.replace("LP33", "Drink_Bottle_3")
    if "Oats_Drink" in i:
        path = i.replace("Oats_Drink", "Drink_Bottle_4")
    if "Soy_Oats" in i:
        path = i.replace("Soy_Oats", "Drink_Bottle_5")
    if "With_Kernel" in i:
        path = i.replace("With_Kernel", "Drink_Bottle_6")
    if "Crunchoco" in i:
        path = i.replace("Crunchoco", "Snack_Box_1")
    if "Puff" in i:
        path = i.replace("Puff", "Snack_Box_2")
    if "Oreo" in i:
        path = i.replace("Oreo", "Snack_Box_3")
    if "Lotte" in i:
        path = i.replace("Lotte", "Snack_Box_4")
    if "Lays" in i:
        path = i.replace("Lays", "Snack_Box_5")

    # 如果你的檔案夾裡面不只有照片，也有其他類型的檔案，用 if 把照片挑出來
    if '.xml' in i:
        # 前面放舊名字，後面放新名字
        os.rename(i, path)
