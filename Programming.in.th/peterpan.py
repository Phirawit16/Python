word = list(input())


def l1():
    count = 1
    for i in word:
        if count % 3 != 0:
            print('..#.', end='')
            count += 1
        else:
            print('..*.', end='')
            count = 1
    print('.')


def l2():
    count = 1
    for i in word:
        if count % 3 != 0:
            print('.#.#', end='')
            count += 1
        else:
            print('.*.*', end='')
            count = 1
    print('.')


def l3():
    print('#', end='')
    workdone = 0
    count = 1
    alert = True
    for i in word:
        if count % 3 != 0:
            print('.{}.'.format(i), end='')
            workdone += 1
            if workdone == len(word):
                print('#', end='')
                break
            count += 1
        else:
            print('.{}.*'.format(i), end='')
            workdone += 1
            alert = False

        if count % 3 != 0 and alert is True:
            print('#'.format(i), end='')
        elif count % 3 == 0 and alert is True:
            print('*'.format(i), end='')
        else:
            count = 1
            alert = True
    print('')


l1()
l2()
l3()
l2()
l1()
