product=[['laptop',56000],
         ['phone',76000],
         ['charger',2000],
         ['mouse',700],
         ['buds',3500]
         ]

def view_product():
    print('product Name' .ljust(15,' '),'price')
    for i in product:
        print(i[0].ljust(15,' '),i[1])
view_product()        


        
                                   
