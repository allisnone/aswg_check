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

二、Exe 使用步骤：

程序运行的是有前提的，当前客户端已配置好，只需两个条件：aswg 策略，安装wkhtmltopdf.exe（用户生成pdf文件）应用程序并配置好环境变量。--后续补充这部分
当前客户端演示即可：
1、程序copy整个aswg目录至windows c盘某个目录即可
2、在cmd命令下进入aswg目录
3、运行 aswg.exe  (无需参数)生成无代理时的结果， 输出html格式，位于result目录。
4、运行aswg.exe 172.18.230.23:8080,   172.18.230.23:8080 是代理的地址，生成有代理的检测结果。
5、运行html2pdf.exe, 把result 目录的html文件转换为pdf文件。即可把pdf提交给用户做前后有无对比。
6、可登陆ucss https://172.16.230.23:8447  查看事件;用户密码：admin/Firewall1!  -本机firefox可以直接登录。

