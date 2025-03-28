from modules import *
import pyperclip as pc

def setToken():
    print('未设置 token，请参考 github.com/788009/zxx-edu-textbook#获取-token')
    input()
    exit()

try:
    token = readS('token.txt')
except:
    setToken()

if token == '':
    setToken()

def copyWithToken(url):
    pc.copy(f'{url}?accessToken={token}')

def choose(tree, end):
    if tree.get(end):
        [print(f'{key}: {value}') for key, value in tree.items()]
        if tree['url']:
            copy = input('带 token 复制到剪贴板？y/n: ')
            if copy in ['y', 'Y']:
                copyWithToken(tree['url'])
                print('已复制')
        input('按回车键退出')
        return True
    keys = list(tree.keys())
    [print(i+1, keys[i]) for i in range(len(keys))]
    while True:
        try:
            choice = int(input('输入数字选择，0 表示返回上一级：'))
            if choice > len(keys):
                continue
            break
        except:
            print('输入错误，请重新输入')
            pass
    if choice == 0:
        return False
    res = choose(tree[keys[choice-1]], end)
    if res == 0:
        return choose(tree, end)
    return True

data = readL('tree.json')
choose(data, 'url')
