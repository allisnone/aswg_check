# -*- coding: utf-8 -*-
import url_request as req
import pdf
import sys
if __name__ == '__main__':
    print("注意事项和准备：")
    print("1. 您的公网IP地址是： ",req.get_my_public_ip())
    print('2. 默认运行ASWG主程序，不加任何参数时，即为无ASWG代理测试')
    print("3. 如开始ASWG代理测试，请确认你的公网IP地址已经加入ASWG的内网并加入免认证规则; 并在运行时添加ASWG代理IP:端口")
    print("4. 如果你没有ASWG代理，可暂时使用默认代理：华为云ASWG代理，加参数1即可: python aswg.py 1")
    #print('默认代理=',req.PROXIES)
    print('----------------------检查ASWG代理服务器设置--------------')  
    proxies = {}
    aswg_or_not = ''
    if len(sys.argv)>=2:
        if sys.argv[1] and isinstance(sys.argv[1], str):
            proxy = sys.argv[1]  #start date string
            if not proxy:
                aswg_or_not = '无'
                print('测试将不经过任何ASWG！！！')
            elif str(proxy) == '1':
                proxies = req.PROXIES
                print('使用默认代理： ', req.PROXIES)
            elif ':' not in proxy:
                print("你当前输入的代理是:%s ,请输入正确的ASWG IP +端口号" % proxy)
                sys.exit()
            else:
                proxies = {'http': 'http://' + proxy}
                print('当前使用自定义的ASWG代理是： ', proxies)
    else:
        aswg_or_not = '无'
        print('测试将不经过任何ASWG！！！')   
    print('----------------------开始  %sASWG 代理测试--------------'% aswg_or_not)   
    all_summary,base_html,now_time_str = req.get_aswg_result(proxy=proxies)
    if aswg_or_not:
        now_time_str = 'aswg' + now_time_str
    print('----------------------生成PDF测试报告--------------')
    pdf.html2pdf(dest_url='',result_dir='./result/',wkhtmltopdf_dir='',now_time_str=now_time_str)
    print('----------------------完成 %sASWG 代理测试--------------'% aswg_or_not)   
    print('all_summary=',all_summary)