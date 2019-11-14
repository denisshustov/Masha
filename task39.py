def isInt(p2):
    try:
        r = int(p2)
        return True
    except Exception:
        return False

def checkUserInput(p1):
    if isInt(p1) == True:
        print('int ok')
        return True
    else:
        print('ошибка ведите число')
        return False


k = input()
checkUserInput(k)
