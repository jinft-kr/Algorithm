'''

'''
N = input()

tmp = len(N) // 2
left = list(N[:tmp])
right = list(N[tmp:])
sum = 0
for i in left:
    sum += int(i)
for i in right:
    sum -= int(i)

if sum == 0:
    print("LUCKY")
else:
    print("READY")
