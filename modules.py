from json import loads, dumps

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

def readS(fileName):
    with open(fileName, encoding='utf-8') as f:
        res = f.read()
        return res

def readE(fileName): # Eval
    with open(fileName, encoding='utf-8') as f:
        res = f.read()
        if not res[0] in ['{', '[']:
            res = res[1:]
        return eval(res)

def readL(fileName): # Loads
    with open(fileName, encoding='utf-8') as f:
        res = f.read()
        if not res[0] in ['{', '[']:
            res = res[1:]
        return loads(res)

def writeR(fileName, text): # Replace
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(text)

def writeA(fileName, text): # Append
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(text)

def writeD(fileName, data, indent=4, ensure_ascii=False): # Dumps
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(dumps(data, indent=indent, ensure_ascii=ensure_ascii))
