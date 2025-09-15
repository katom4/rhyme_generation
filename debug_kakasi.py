from pykakasi import kakasi

kks = kakasi()

text = "ラーメン"
result = kks.convert(text)
print('"ラーメン"')
for item in result:
    print(item)

text = "かんたん"
result = kks.convert(text)
print('"かんたん"')
for item in result:
    print(item)