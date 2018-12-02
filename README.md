# -*- coding: utf-8 -*-
# aswg_check

一、Pure Python 环境准备和使用步骤：
1. 安装python3 环境： 
		Windows, Mac 去下载相应的安装包： https://www.python.org/downloads/
		Linux 系统默认安装2python2.7， 可以使用 直接安装新版本，然后设置python3的环境变量。 或者安装python 多版本控制工具 pyenv
		之前我有安装配置过pyenv，后面会更新共享tips。

2. 安装python 依赖库：
pip install requests
pip install requests_toolbelt
pip install pdfkit

3. 安装HTML转换未PDF工具 wkhtmltopdf，并设置用户环境变量：
	wkhtmltopdf下载地址： https://wkhtmltopdf.org/downloads.html
	
4. 使用方法：
不使用代理：
python aswg.py 
使用默认代理：
python aswg.py 1

使用自定义代理： 172.16.0.21:8080
python aswg.py  172.16.0.21:8080

5. 如果使用自定义代理，需对ASWG做相关网络、认证和策略配置
5.1 查看你的公网IP，把你的公网IP 加入ASWG内网.
5.2 如果你没有有ASWG集成的认证账号，添加免认证。
5.3 配置相应的ASWG 安全设置、默认策略允许“安全分析“和”内容分析”、配置ASWG DLP策略：包括个人身份信息、源代码保护、社保信息等相关策略。

二、生成windows 单一可执行EXE文件步骤：
1、安装pyinstaller
easy_install PyInstaller

2、运行pyinstaller 将python代码生成两个exe文件：aswg.exe, htmp2pdf.exe，结果位于dist
pyinstaller -F -i ./static/images/aswg.ico aswg.py
pyinstaller -F -i ./static/images/aswg.ico html2pdf.py

3、将result、static、doc目录复制到dist目录：aswg.exe和htmp2pdf.exe 依赖这两个目录输出结果和做dlp相关配置。
4、将dist目录copy并重命名即可发布使用。

三、EXE 文件使用步骤 
程序运行的是有前提的，当前客户端已配置好，只需两个条件：
aswg 策略，安装wkhtmltopdf.exe（用于将HTML结果转换为PDF文件）应用程序并配置好环境变量。
更详细的说明请阅读： aswg/doc/ASWG安全预检查指导说明.docx
1、验证aswg IP是否可达： ping 172.18.230.23  或者 telnet 172.18.230.23 8080
2、验证已配置好wkhtmltopdf.exe的环境变量： wkhtmltopdf.exe -V
3、发布的aswg目录至windows c盘某个目录即可
4、以管理员运行cmd命令并进入aswg目录
5、运行 aswg.exe  (无需参数)生成无代理时的结果， 输出html格式，位于result目录。
 生成无代理时的报告-无参数运行：aswg.exe
 生成有aswg代理的报告：
	使用自定义aswg代理时的报告：aswg.exe 172.18.230.23:8080,   其中172.18.230.23:8080 是代理的地址，生成有代理的检测结果。
	 使用云端ASWG（华为云）生成报告： aswg.exe cloud
6、生成PDF报告：运行html2pdf.exe, 程序将result 目录的html文件转换为pdf文件。提交PDF文件给用户做前后有无对比。
7、可登陆ucss https://172.16.230.23:8447  查看事件;用户密码：admin/Firewall1!  -本机firefox可以直接登录。


四、Python多版本使用技巧
多版本python环境时，把多版本加入环境变量后，需区分python版本，重命名python主程序和pyinstaller:
C:\Python3.6\python36.exe
C:\Python3.6\Scripts\pyinstaller36.exe
C:\Python3.6\Scripts\pyinstaller36-script.py

多版本使用方法：
python36 -m pip install requests
python36 -m pip install requests_toolbelt
python36 -m pip install pdfkit
python36 -m pip install PyQt5
pyinstaller36 -F -i ./static/images/aswg.ico aswg.py
pyinstaller36 -F -i ./static/images/aswg.ico html2pdf.py
