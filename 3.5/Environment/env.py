dictionary = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789йёцукенгшщзфывапролдячсмитьбюжэхъЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ№"

def StringIsEmpty(string):
    return len(string) == 0

def StringIsEmptyOrWhitespace(string):
    string = string.replace(' ', '')
    return len(string) == 0

def GetKeyFromDictWithValue(dict, value):
    for key, value in dict.items():
        if value == value:
            return key

def AnyStrToInt(obj):
    if type(obj) == list:
        result = []
        for item in obj:
            result.append(int(item))
        return result
    elif type(obj) == str:
        return int(obj)
