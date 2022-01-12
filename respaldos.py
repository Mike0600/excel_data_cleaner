# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:15:43 2022

@author: mike0
"""

import pandas as pd



def search_colums(col1, col2):
    equal_columns : list = []
    zero_columns : list = []
    for i in range(2,len(col1)):
        if col1[i] != '0':
            if col1[i] == col2[i]:
                equal_columns.append(i)
        elif col1[i] == '0':
            if col1[i] == col2[i]:
                zero_columns.append(i)
    
    return equal_columns, zero_columns


def fill_data(row_list):
    data : list = []
    for elem in row_list:
        data.append(df.iloc[elem:elem+1, 1:13].values.tolist())
    return data



def list_to_df(col_list):
    list_to_clean : list = []
    for item in col_list:
        list_to_clean.append(item[0])
    for item in list_to_clean:
        item.pop(4)
        item.pop(4)
        item.pop(7)
        item.pop(6)
    new_data = pd.DataFrame (list_to_clean, columns = ['Nombre',
                                                       'Usuario',
                                                       'Usuario',
                                                       'Nombre del equipo',
                                                       'Proyecto',
                                                       'Correo',
                                                       '1/3/2022',
                                                       '1/10/2022'])
    return new_data





df = pd.read_csv('r.csv')
equal_columns, zero_columns =  search_colums(df['Unnamed: 11'], df['Unnamed: 12'])

data_equal_colums = fill_data(equal_columns)
data_zero_colums = fill_data(zero_columns)


data_equal_colums_df = list_to_df(data_equal_colums)  
data_zero_colums_df = list_to_df(data_zero_colums)
    


data_equal_colums_df.to_csv('Personas_sin_avance.csv', index = True)
data_zero_colums_df.to_csv('Personas_sin_respaldo.csv', index = True)