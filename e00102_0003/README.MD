# 编译运行发布步骤
本地安装Python路径参考如下：
D:\Python\Python36
或
D:\Python\Python313
在环境变量中设置有效果的路径为上面的某一个，哪个路径在上面就哪个有效
D:\Python\Python313\Scripts\
D:\Python\Python313\
D:\Python\Python36\Scripts\
D:\Python\Python36\
上面的设置为313版本有效
同时可以把安装目录下的
D:\Python\Python313\python.exe
文件多复制几份，改为不同的名称，如下：
D:\Python\Python313\python313.exe
D:\Python\Python313\python3.13.exe
D:\Python\Python313\python3.exe

生成虚拟环境
python -m venv .venv
执行程序
python main.py
安装打包依赖
pip install pyinstaller
打包程序
pyinstaller --onefile main.py

打包后会生成dist文件夹，里面有打包后的可执行文件。
同时把data文件夹拷贝到dist文件夹下，这样可执行文件才能找到data文件

# 注意事项
1. 请确保安装的 Python 版本为 3.6 或以上版本。
2. 请确保安装的 PyInstaller 版本为 3.6 或以上版本。
3. 请确保安装的依赖包均已安装。
4. 请确保 main.py 与 requirements.txt 位于同一目录下。
5. 请确保 main.py 与 pyinstaller 位于同一目录下。


# python程序示例，打包
## 生成虚拟环境
```shell
python -m venv .venv
```
.开头一般是隐藏文件，所以需要用ls -a才能看到
## 生成依赖文件
```shell
pip freeze > requirements.txt
```
## 安装依赖
```shell
pip install -r requirements.txt
```
## 运行程序
```shell
python main.py
```
## 打包程序
```shell
pyinstaller --onefile main.py
```

```shell
clear
pyinstaller -F main.py -n 程序名称
```


# pyinstaller 使用方法
```shell
pyinstaller --help
```
options:
  -h, --help            show this help message and exit
  -v, --version         Show program version info and exit.
What to generate:
  -D, --onedir          Create a one-folder bundle containing an executable (default)
  -F, --onefile         Create a one-file bundled executable.
  --specpath DIR        Folder to store the generated spec file (default: current directory)
  -n, --name NAME       Name to assign to the bundled app and spec file (default: first script's basename)

# Python路径变更修改

1.配置 VSCode 的 Python 解释器
选择解释器：
打开 VSCode。
按 Ctrl+Shift+P（Windows/Linux）或 Cmd+Shift+P（Mac），输入 Python: Select Interpreter 并选择它。
在弹出的列表中选择 Enter interpreter path，然后手动输入或浏览到 D:\Python\python.exe。
2. 检查 VSCode 设置
settings.json：打开 VSCode 的设置文件（File > Preferences > Settings 或按 Ctrl+,），搜索 python.pythonPath 或 python.defaultInterpreterPath，确保它们指向正确的路径。


# 设置命令行代理
在控制台输入
set https_proxy=http://127.0.0.1:33210
set http_proxy=http://127.0.0.1:33210

查看
echo %http_proxy% # Windows
echo $http_proxy     #linux

取消
set http_proxy=      # Windows
unset http_proxy      #linux

set https_proxy=
set http_proxy=

# github 上传代码方法
## 2021年8月13日github已经不支持密码认证方法
Logon failed, use ctrl+c to cancel basic credential prompt.
remote: Support for password authentication was removed on August 13, 2021.

## 采用ssh密钥认证
1. 生成ssh密钥对
```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f id_rsa_github_xxxx
```
2. 复制ssh公钥到github
```shell
clip < ~/.ssh/id_rsa.pub
```
3. 登录github，点击左上角头像，选择Settings，选择SSH and GPG keys，New SSH key，Title随便填，Key直接粘贴复制的公钥，点击Add SSH key。
4. 克隆代码到本地
```shell
git clone git@github.com:your_username/your_repository.git
```
5. 推送代码到远程仓库
```shell
git push origin master
```
## 本地有多个仓库的配置方法
通过 右键 git bash here 打开git bash，输入
```shell
cd ~
pwd
```
返回
/c/Users/Administrator
即进入当前用户的ssh目录
C:\Users\Administrator\.ssh
在config文件中添加如下内容
```shell
# CJXT github all
Host cjxt.github.com
    HostName github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa_github_chengjingxuetang
```
其中cjxt.github.com为自定义的域名，HostName为github.com，PreferredAuthentications publickey为公钥认证，IdentityFile为密钥文件路径。

拉取代码采用如下命令
```shell
git clone git@cjxt.github.com:chengjinxt/pythonExamples.git
```


