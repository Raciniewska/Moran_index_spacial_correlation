import matplotlib.pyplot as plt

import csv
import numpy as np
import pandas as pd
# TO DO TRZEBA USUNAC NAGLOWEK ZACHOWAC GO JAKO SLOWNIK I ZAMiENIC NAGLOWEK NUMERAMI
w = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\macierz_odległości.csv',sep=';')

w = w.iloc[: , 1:]
numery_obszarow = w.columns
numery_w_macierzach = []
obszary_slownik ={}
for number in range(0,len(numery_obszarow)):
    numery_w_macierzach.append(str(number))
    obszary_slownik[int(float(numery_obszarow[number]))]=number
w=w.set_axis(numery_w_macierzach, axis=1, inplace=False)
print(w)
w.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\macierz_odległości.csv',sep=';',index = False, header=False)

#MACIERZ SASIEDZTWA
nb = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\macierz_sasiedztwa.csv',sep=';')

nb = nb.iloc[: , 1:]
numery_obszarow = nb.columns
numery_w_macierzach = []
obszary_slownik ={}
for number in range(0,len(numery_obszarow)):
    numery_w_macierzach.append(str(number))
    obszary_slownik[int(float(numery_obszarow[number]))]=number
nb=nb.set_axis(numery_w_macierzach, axis=1, inplace=False)
print(nb)
nb.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\macierz_sasiedztwa.csv',sep=';',index = False, header=False)

#PRZYPADKI
inf =pd.read_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\przypadki.csv',  sep=';')
inf=inf.drop(['date','id','x','y','time','sex' ,'age',  'exp_id','2020-10-01 00:00:00', 'x92','y92'], axis = 1)
inf = inf[inf.event == 'exposed']
inf=inf.drop(['event'], axis = 1)
inf['i']=1
inf=inf.groupby('reg_id').sum()
inf_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in inf.iterrows():
    inf_vec.at[obszary_slownik[index],0]=row[0]
inf_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\przypadki.csv',sep=';',index = False, header=False)

#MUZEA-BIBLIO
muzea_biblio = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\muzea_biblio_data.csv',sep=';')
muzea_biblio['summed_area'] = muzea_biblio['LICZBAKOND'] *muzea_biblio['summed_area']
muzea_biblio=muzea_biblio.drop(['id', 'left','POJEMNOSC','area','top','right','bottom' ,'ID_2',  'LICZBAKOND'], axis = 1)
muzea_biblio=muzea_biblio.groupby("fid").sum()
muzea_biblio_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in muzea_biblio.iterrows():
    muzea_biblio_vec.at[obszary_slownik[index],0]=row[0]
muzea_biblio_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\muzea_biblioteki.csv',sep=';',index = False, header=False)
#BUDYNKI
budynki= pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\data_budynki1000.csv',sep=',')
budynki=budynki.drop(['ID_2','id','LICZBAKOND','area'], axis = 1)
budynki=budynki.groupby("fid").sum()
budynki_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in budynki.iterrows():
    budynki_vec.at[obszary_slownik[index],0]=row[0]
budynki_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\budynki.csv',sep=';')
#handel
handel = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_handel_data.csv',sep=';')
handel =handel.drop(['id', 'ID_2','POJEMNOSC','area'], axis = 1)
handel=handel.groupby("fid").sum()
handel_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in handel.iterrows():
    handel_vec.at[obszary_slownik[index],0]=row[0]
handel_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\handel.csv',sep=';',index = False, header=False)

#hotele
hotele = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_hotele_data.csv',sep=';')
hotele['summed_area'] = hotele['LICZBAKOND'] *hotele['summed_area']
hotele =hotele.drop(['id', 'ID_2','POJEMNOSC','area', 'LICZBAKOND'], axis = 1)
hotele=hotele.groupby("fid").sum()
hotele_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in hotele.iterrows():
    hotele_vec.at[obszary_slownik[index],0]=row[0]
hotele_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\hotele.csv',sep=';',index = False, header=False)

#koscioly
koscioly = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_koscioly_data.csv',sep=';')
koscioly['summed_area'] = koscioly['LICZBAKOND'] *koscioly['summed_area']
koscioly =koscioly.drop(['id', 'ID_2','POJEMNOSC','area', 'LICZBAKOND'], axis = 1)
koscioly=koscioly.groupby("fid").sum()
koscioly_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in koscioly.iterrows():
    koscioly_vec.at[obszary_slownik[index],0]=row[0]
koscioly_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\koscioly.csv',sep=';',index = False, header=False)

#miejsca_pracy
miejsca_pracy = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_miejsca_pracy_data.csv',sep=';')
miejsca_pracy =miejsca_pracy.drop(['id', 'ID_2','POJEMNOSC','area' ], axis = 1)
miejsca_pracy=miejsca_pracy.groupby("fid").sum()
miejsca_pracy_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in miejsca_pracy.iterrows():
    miejsca_pracy_vec.at[obszary_slownik[index],0]=row[0]
miejsca_pracy_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\miejsca_pracy.csv',sep=';',index = False, header=False)

#parki_lasy
parki_lasy = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_parki_lasy_data.csv',sep=';')
parki_lasy =parki_lasy.drop(['id', 'ID_2','area','TYP' ], axis = 1)
parki_lasy=parki_lasy.groupby("fid").sum()
parki_lasy_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in parki_lasy.iterrows():
    parki_lasy_vec.at[obszary_slownik[index],0]=row[0]
parki_lasy_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\parki_lasy.csv',sep=';',index = False, header=False)

#szkola_przedszkola
szkola_przedszkola = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_szkola_przedszkola_data.csv',sep=';')
szkola_przedszkola =szkola_przedszkola.drop(['id', 'ID_2','area','RODZAJ' ], axis = 1)
szkola_przedszkola=szkola_przedszkola.groupby("fid").sum()
szkola_przedszkola_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in szkola_przedszkola.iterrows():
    szkola_przedszkola_vec.at[obszary_slownik[index],0]=row[0]
szkola_przedszkola_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\szkola_przedszkola.csv',sep=';',index = False, header=False)

#zdrowie
zdrowie = pd.read_csv ('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\raw_data\\siatka_zdrowie_data.csv',sep=';')
zdrowie =zdrowie.drop(['id', 'ID_2','area','RODZAJ' ], axis = 1)
zdrowie=zdrowie.groupby("fid").sum()
zdrowie_vec = pd.DataFrame(np.zeros((len(w.columns), 1)))
for index, row in zdrowie.iterrows():
    zdrowie_vec.at[obszary_slownik[index],0]=row[0]
zdrowie_vec.to_csv('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\1000x1000\\zdrowie.csv',sep=';',index = False, header=False)

#zapisanie numerów obszarów
with open('C:\\Users\\braciniewska\\OneDrive - Lenovo\\Documents\\Studia\\pbad\\transformed_data\\obszary_slownik.csv', 'w' ,newline="")  as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['f_id','index'])
    for data in obszary_slownik.items():
        writer.writerow(data)