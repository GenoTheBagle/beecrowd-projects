menu = {
    "1":4.0,
    "2":4.5,
    "3":5.0,
    "4":2.0,
    "5":1.5
}

x, y = input().split()

total = menu[x]*int(y)

print(f"Total: R$ {total}0")
