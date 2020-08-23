print('     ', end='')
for i in range(10):
    print(f'{i:^5d}', end='')
print()
print('-------------------------------------------------------')
for i in range(0,10):
    print(f'{i}:   ', end='')
    producto = 0
    for j in range(10):
        print(f'{producto:^5d}', end='')
        producto += i
    print('')