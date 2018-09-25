# aswg_check

环境准备和使用步骤：
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
