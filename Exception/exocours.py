if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except ValueError:
        print("Please enter a float")
    except ZeroDivisionError:
        print("b should not be 0")
    else:
        print(res)