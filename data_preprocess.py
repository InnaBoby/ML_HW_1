
#приведем столбцы к числовому типу

def data_preproc(df):

 '''
 Функция преобразующая столбцы со строковой информацией в числовые
 '''

 df['mileage'] = df['mileage'].transform(lambda x: float(str(x).split()[0]))

 df['engine'] = df['engine'].transform(lambda x: float(str(x).split()[0]))

 #в столбце 'max_power' была одна строка, где наименование стояло перед цифрой
 df['max_power'] = df['max_power'].transform(lambda x: float(str(x).split()[0]) if str(x).split()[0].isalpha() == False else 0)

 df['torque_Nm'] = df['torque'].transform(lambda x: str(x).split()[0]).astype('str')
 df['torque_Nm'] = df['torque_Nm'].apply(lambda x: re.findall(r'\d+\.?\d+?', x)).apply(lambda x: float(''.join(x)) if ''.join(x) != '' else 0)


 df['torque_rpm'] = df['torque'].transform(lambda x: str(x).replace(str(x).split()[0], '')).astype('str')
 df['torque_rpm'] = df['torque_rpm'].apply(lambda x: re.findall(r'\d+\.?\d+?', x))
 #т.к. по некоторым автомобилям есть 2 значения, то сделаем 2 столбца с минимальным и максимальным значением

 def choose_min(lst):
     if len(lst) > 1:
       if lst[0] < lst[1]:
         return lst[0]
       else:
         return lst[1]
     elif len(lst) == 1:
       return lst[0]
     else:
       return 0

 df['torque_rpm_min'] = df['torque_rpm'].apply(choose_min).astype('float')

 def choose_max(lst):
     if len(lst) > 1:
       if lst[0] > lst[1]:
         return lst[0]
       else:
         return lst[1]
     elif len(lst) == 1:
       return lst[0]
     else:
       return 0

 df['torque_rpm_max'] = df['torque_rpm'].apply(choose_max).astype('float')

 df.drop(columns=['torque', 'torque_rpm'], inplace = True)

 return df
