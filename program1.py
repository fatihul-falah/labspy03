modal = 100000000
laba = 0
untung = 0

for bulan in range(1, 9):
    if(bulan < 3):
        laba = 0
        untung = untung + laba
    elif(bulan < 5):
        laba = modal*1/100
        untung = untung + laba
    elif(bulan < 8):
        laba = modal*5/100
        untung = untung + laba
    else:
        laba = modal*2/100
        untung = untung + laba
    print("Laba bulan ke", bulan, "Sebesar:", laba)
print("Total laba adalah:", untung)
