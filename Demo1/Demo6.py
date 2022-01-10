import unicodedata


def Is_Number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False


print("lalalala是否为数字： ",Is_Number('lalalala'))
print("1345是否为数字： ",Is_Number('1345'))
print("lalalala1345是否为数字： ",Is_Number('lalalala1345'))