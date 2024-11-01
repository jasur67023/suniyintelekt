import pandas as pd
data = {
    'ism': ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim', 'Jahongir','Abdulaziz','Nusratbek','Jasurbek','Jonibek' ],
    'yoshi': [25, 30, 22, 45, 50, 60, 33, 23, 26, 80],
    'shahar': ['Toshkent', 'Fargona', 'Namangan', 'Andijon', 'Toshkent', 'Fargona', 'Fargona', 'Fargona', 'Namangan', 'Andijon'],
}
mb = pd.DataFrame(data)
print(mb)
yosh_odamlar =mb[mb['yoshi'] > 30]
print("30 yoshdan kichiklar:\n",yosh_odamlar)
mb['yoshi'] += 1
print("Yangillangan DataFrame:\n", mb)
shahar_fergana = mb[mb['shahar'] == 'Fargona']
print("Farg'ona shaharidagi odamlar:\n", shahar_fergana)

import numpy as np

phone_1d = np.array([1,2,3,4,5,6])
phone_2d = np.array([[1,2,3,4],[5,6,7,8]])

sum_phone = np.sum(phone_1d)
mean_phone = np.mean(phone_1d)
product_phone = np.prod(phone_1d)

print("1D Massiv: ", phone_1d)
print("2D Massiv:\n", phone_2d)
print("Massivlar yig'indis: ", sum_phone)
print("O'rtacha: ", mean_phone)
print("Ko'paytma: ", product_phone)