# # -----------------------------DICTIONARY----------------------------

# # ------create dictionary----------

# D1={}
# print(D1)
# print(type(D1))
# print('\n')
# print('-------------------------------------------------------')

# # ------create dictionaries in four different ways----------

# #------1 way------
# print('create dictionary in 1st way')
# D2={'Name':'Sahil','Age':'40'}
# print(D2)
# print(type(D2))
# print('\n')
# print('-------------------------------------------------------')

# #------2 way------
# print('create dictionary in 2nd way')
# D3={}
# D3['Name']='SahilRaj'
# D3['Age']=43
# print(D3)
# print(type(D3))
# print('\n')
# print('-------------------------------------------------------')

# #------3 way------
# print('create dictionary in 3rd way')
# D4=dict(Name='SahilJi',Age=45)
# print(D4)
# print(type(D4))
# print('\n')
# print('-------------------------------------------------------')

# # #------4 way------
# # dict([('Name','Sahil'),('Age',40)])
# # print('-------------------------------------------------------')

# # ---------Adding values in dictionary-------------
# D5={'Raja':'1234567890','Adity':'0987654321'}
# print(D5)
# print('Adding values in dictionary')
# D5['Sahil']='916578967879'
# D5['Amit']='916789676767'
# print(D5)
# print('\n')

# print('-------------------------------------------------------')


# # --------Replacing values in dictionary----------
# D6={'Sahil':'916576879456','Amit':'919978687878'}
# print(D6)
# print('Replacing values in dictionary')
# D6['Sahil']='916578967879'
# D6['Amit']='916789676767'
# print(D6)
# print('\n')
# print('-------------------------------------------------------')


# # -------------Retrieving Values in dictionary--------------------

# print('Retrieving values in dictionary')
# D7={'Sahil':'916576879456','Amit':'919978687878'}
# print(D7['Sahil'])
# print('\n')
# print('-------------------------------------------------------')


# # ------------------formatting dictionaries--------------------------
# D={}
# D['laptop']='Macbook Pro'
# D['Count']=10
# print('formatting dictionaries')
# print('I want %(Count)d %(laptop)s'%D)
# print('\n') 
# print('-------------------------------------------------------')


# #----------------------Deleting item in dictionary--------------------------
# D8={'Sahil':'916576879456','Amit':'919978687878'}
# print(D8)
# print('Deletingitem in  dictionary')
# del D8['Sahil']
# print(D8)


# # ------------------------Method dictionary class--------------------------------
# # ----keys method-----
# print('Keys Method --->return all key')
# ASCII_CODE1={"A":11,"B":12,'C':13,'D':14,'E':15}
# print(ASCII_CODE1)
# print(ASCII_CODE1.keys())
# print('\n') 
# print('-------------------------------------------------------')

# # ---values method-----
# print('Values Method ----->return all values')
# ASCII_CODE2={"A":11,"B":12,'C':13,'D':14,'E':15}
# print(ASCII_CODE2)
# print(ASCII_CODE2.values())
# print('\n') 
# print('-------------------------------------------------------')



# # ---items method-------
# print('Items Method ----->return all items')
# ASCII_CODE3={"A":11,"B":12,'C':13,'D':14,'E':15}
# print(ASCII_CODE3)
# print(ASCII_CODE3.items())
# print('\n') 
# print('-------------------------------------------------------')


# # ------clear method---------
# print('Clear Method ----->deleting all entries')
# ASCII_CODE3={"A":11,"B":12,'C':13,'D':14,'E':15}
# print(ASCII_CODE3)
# print(ASCII_CODE3.clear())
# print('\n') 
# print('-------------------------------------------------------')

# # --------get Method--------
# print('Get method-->return the value for a key')
# D9={'Mumbai':45,"Bihar":65,"Dehli":76}
# print(D9.get('Bihar'))
# print('\n') 
# print('-------------------------------------------------------')


# # --------Pop Method--------
# print('Pop method-->remove a key and return the vlue if the key exist')
# D10={'Mumbai':45,"Bihar":65,"Dehli":76}
# D10.pop('Bihar')
# print(D10)
# print('\n') 
# print('-------------------------------------------------------')