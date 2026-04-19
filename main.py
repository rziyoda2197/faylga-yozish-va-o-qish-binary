def matn_baytga_yoz(matn, fayl_ismi):
    with open(fayl_ismi, 'wb') as f:
        f.write(matn.encode('utf-8'))

def baytga_matn_oq(fayl_ismi):
    with open(fayl_ismi, 'rb') as f:
        matn = f.read().decode('utf-8')
    return matn

matn = "Salam, dunyo!"
fayl_ismi = "matn.bin"

matn_baytga_yoz(matn, fayl_ismi)
print(baytga_matn_oq(fayl_ismi))
```

Kodda ikkita funksiya mavjud:

1. `matn_baytga_yoz(matn, fayl_ismi)`: Matnni binary faylga yozadi.
2. `baytga_matn_oq(fayl_ismi)`: Binary fayldan matnni oʻqib chiqadi.
