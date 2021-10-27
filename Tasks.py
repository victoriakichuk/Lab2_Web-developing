def palindrome():
    num = int(input("Enter a number: "))
    temp = num
    is_palindrome = True
    is_not_palindrome = False
    rev_num = 0
    while (num > 0):
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10
    if (temp == rev_num):
        print(is_palindrome)
        return
    print(is_not_palindrome)


def division235():
    list = []
    two = []
    three = []
    five = []
    for e in input("Enter the numbers").split():
        list.append(int(e))
    for i in list:
        if i % 2 == 0:
            two.append(i)
        if i % 3 == 0:
            three.append(i)
        if i % 5 == 0:
            five.append(i)
    print("List of numbers that divide by 2:", two)
    print("List of numbers that divide by 3: ", three)
    print("List of numbers that divide by 5: ", five)


def flip():
    n1 = int(input("Enter a number:'/; "))
    n2 = 0
    while n1 > 0:
        d = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + d
    print('The opposite number:', n2)


def sqrt():
    A = float(input("Number: "))
    n = int(input("Power "))
    x = A / 2
    for i in range(1000):
        x = 1 / n * ((n - 1) * x + A / x ** (n - 1))
    return x


def tenthousand(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = n ** (1 / 2)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
        return True


def ob(y):
    if y == '1':
        f = palindrome()
        print(f)
    elif y == '2':
        f = division235()
    elif y == '3':
        f = flip()
    elif y == '4':
        print(sqrt())
    elif y == '5':
        print(tenthousand(int(input("Number you picked: "))))


print("Pick a task")
y = input()
ob(y)


