# -*- coding: utf-8 -*-
import url_request as req
#import pdf
import sys
if __name__ == '__main__':
    print("----------------------注意事项和准备----------------------")
    try:
        req.get_my_public_ip()
        print("1. 您的公网IP地址是：%s;必要时需加入ASWG免认证。" % req.get_my_public_ip())
    except:
        print("1. 无法确定您的公网IP地址！请自行从ip138.com检查，必要时需加入ASWG免认证。")
    print("注意事项和准备：")
    print('2. 默认运行ASWG主程序，不加任何参数时，即为无ASWG代理测试')
    print("3. 如开始ASWG代理测试，请确认你的公网IP地址已经加入ASWG的内网并加入免认证规则; 并在运行时添加ASWG代理IP:端口")
    print("4. 如果你没有ASWG代理，可暂时使用默认代理：华为云ASWG代理，加参数1即可: python aswg.py 1")
    #print('默认代理=',req.PROXIES)
    print('----------------------检查ASWG代理服务器设置--------------')  
    proxies = {}
    aswg_or_not = 'no_aswg_'
    proxy = None
    if len(sys.argv)>=2:
        if sys.argv[1] and isinstance(sys.argv[1], str):
            proxy = sys.argv[1]  #start date string
            if not proxy:
                #aswg_or_not = '无'
                print('测试将不经过任何ASWG！！！')
            elif str(proxy) == '1':
                proxies = req.PROXIES
                aswg_or_not = '_default_aswg_'
                print('当前使用默认代理： ', req.PROXIES['http'])
            elif ':' not in proxy:
                print("你当前输入的代理是:%s ,请输入正确的ASWG IP +端口号" % proxy)
                sys.exit()
            else:
                aswg_or_not = proxy.replace('.','_').replace(':','_') + '_aswg_'
                proxies = {'http': 'http://' + proxy}
                print('当前使用自定义的ASWG代理是： ', proxies)
    else:
        #aswg_or_not = '无'
        print('测试将不经过任何ASWG！！！')   
    if proxies:
        if not req.is_proxy_workable(proxies):
            print('代理服务异常，请检查代理服务器或网络连通性！')
            sys.exit()
        else:
            print('代理正常,代理服务器可达！')
    print('----------------------开始 %s ASWG 代理测试--------------'% proxy)   
    all_summary,base_html,now_time_str = req.get_aswg_result(proxy=proxies)
    #if aswg_or_not:
    additional_name = aswg_or_not + now_time_str
    html_file_name='./result/result_%s.html' % additional_name
    print('----------------------生成HTML测试报告--------------')
    req.write_final_html(base_html,file_name= html_file_name)
    print('Write the result as HTML: %s'% html_file_name)
    #pdf.html2pdf(dest_url='',result_dir='./result/',wkhtmltopdf_dir='',now_time_str=now_time_str)
    print('----------------------完成 %sASWG 代理测试--------------'% proxy)   
    print('all_summary=',all_summary)