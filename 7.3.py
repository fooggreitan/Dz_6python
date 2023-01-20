# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

seanson = list(map(float, input().split(",")))
print(seanson)
res = [seanson[i] * seanson[len(seanson) - 1 - i] for i in range((len(seanson) + 1)//2)]
print(res)

