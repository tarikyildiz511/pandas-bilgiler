import pandas as pd
from numpy.random import randn
#Data Frame nedir sql veya excel tablosu gibi bir tablodur
df = pd.DataFrame(randn(3,3),["A","B","C"],columns = ["Column1","Column2","Column3"])
#data frame'yi result'a gönder
result = df
#data frame'den kolon 1'i ekrana yazdır
result = df["Column1"]
#typeni öğrenmek
result = type(df["Column1"])
result = df[["Column1","Column2"]]
result = df.loc["A"]

print(result)


