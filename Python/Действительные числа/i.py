p = int(input())
x = int(input())
y = int(input())
k = int(input())
money_before = 100 * x + y
for i in range(1,k+1):
    money_after = int(money_before * (100 + p) / 100) 
    money_before = money_after
print(money_after // 100, money_after % 100)