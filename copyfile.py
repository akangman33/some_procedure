# -*- coding: UTF-8 -*-
# import os
import sys
import shutil
import numpy as np

count = np.arange(3, 2927, 3).tolist()
# count = np.arange(1, 3300, 3).tolist()
# filename = ['Oats_Drink', 'Soy_Oats', 'With_Kernel']
filename = ['Black_Tea', 'Cheers', 'Coffee_Milk', 'Family_Water', 'Green_Milk_Tea',
            'LP33', 'LS_Soymilk', 'Oolong_Milk_Tea', 'Puff', 'Crunchoco', 'Oreo',
            'Oats_Drink', 'Soy_Oats', 'With_Kernel']
# filename = ['Black_Tea', 'Cheers', 'Coffee_Milk', 'Family_Water', 'Green_Milk_Tea',
#             'Lemon_Tea', 'LP33', 'LS_Soymilk', 'Oats_Drink', 'Ocean_Spray',
#             'Oolong_Milk_Tea', 'Purple', 'Soy_Oats', 'Soymilk', 'With_Kernel',
#             'Puff', 'Lays', 'Crunchoco', 'Oreo', 'Lotte']
source = "D:/image/image_0119/{}_0119_black_background_{}.jpg"
target = "D:/image/temp_horizontal"

try:
    for name in filename:
        for cnt in count:
            print(name, cnt)
            shutil.copy(source.format(name, str(cnt).zfill(4)), target)
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())