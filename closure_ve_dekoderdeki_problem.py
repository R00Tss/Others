def selam():
    print('Selam fonksiyonu çalıştı')
    def merhaba():
        print('merhaba fonksiyonu çalıştı')
    return merhaba    

#Bir numaralı durum
selam()

# İki numaralı durum
test = selam()
test()
