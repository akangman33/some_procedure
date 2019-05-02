# -*- coding: UTF-8 -*-
import os

def batch_rename(dir_path):
    count = 1
    for fname in os.listdir(dir_path):
        new_fname = "member_" + str(count).zfill(4) + ".jpg"
        print(new_fname)
        os.rename(os.path.join(dir_path, fname), os.path.join(dir_path, new_fname))
        count = count + 1

dir_path = "./temp2/"
batch_rename(dir_path)