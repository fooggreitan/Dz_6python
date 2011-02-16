# 45. Найти сумму чисел списка стоящих на нечетной

seanson = list(map(float, input().split(",")))
res = [vax for i, vax in enumerate(seanson) if i%2 == 1]
print(sum(res))

