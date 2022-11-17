per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Сумма депозита = "))
per_cent_list=list(per_cent.values())
def umnozh (x):
    return x*money/100
deposit=map(umnozh,per_cent_list)
deposit=list(map(int,deposit))
print("deposit = ",deposit,"\nМаксимальная сумма, которую вы можете заработать —",max(deposit))
