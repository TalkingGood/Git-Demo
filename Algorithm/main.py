# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

list = [ int(s) for s in input("請輸入： ").split()]
for i in range(len(list) -1, -1):
    print(i)
    print(list[i])


