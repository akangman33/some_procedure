import os


# 先取得該檔案夾內所有的檔案名稱
def get_list():
    all_name = os.listdir()
    return all_name

# 對所有的檔案名稱做 for 迴圈，訂定你的命名規則
for i in get_list():
    path = i.replace(" ", "_")
    # 如果你的檔案夾裡面不只有照片，也有其他類型的檔案，用 if 把照片挑出來
    if '.xml' in i:
        # 前面放舊名字，後面放新名字
        os.rename(i, path)
