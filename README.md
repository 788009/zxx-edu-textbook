# zxx-edu-textbook

[国家中小学智慧教育平台](https://basic.smartedu.cn/)电子课本整理；免登录下载 PDF

![](https://github.com/788009/zxx-edu-textbook/blob/main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-28%20220136.png?raw=true)

## 获取 token

**初次使用需要设置 token**

说是免登录，其实依然需要登录，只是将 token 保存，之后无需登录。

### [方法一](https://github.com/happycola233/tchMaterial-parser?tab=readme-ov-file#2-%E8%AE%BE%E7%BD%AE-access-token)（推荐）

### 方法二

在课本查看页抓包（F12 → Network/网络 → 刷新），`ctrl` + `F` 搜索 `id`，点击第一个结果的 `x-nd-auth` 行：

![](https://github.com/788009/zxx-edu-textbook/blob/main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-28%20212723.png?raw=true)

复制 `id` 值，即 token：

![](https://github.com/788009/zxx-edu-textbook/blob/main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-03-28%20213058.png?raw=true)

## 使用方法

Release 中提供了 exe 和网页两个版本。

### exe

- 下载 `zxx-exe.zip`。
- 解压后，在 `token.txt` 中填入 token。
- 打开 `main.exe` 即可使用。
- 请确保 `main.exe`、`tree.json` 和 `token.txt` 在同一目录下。

### 网页

- 下载 `zxx-htmlGenerator.exe`。
- 运行，输入 token，回车（这一步实际上是将 token 填入网页代码中）。
- 用浏览器打开生成的 `single.html` 即可使用。

## 其他

- 目前未知 token 有效期，似乎可以使用很久，若访问电子课本出现 `401 Authorization Required`，则表示 token 失效，更新 token 即可。

## 声明

下载的电子课本仅供交流学习，资源归国家中小学智慧教育平台所有。