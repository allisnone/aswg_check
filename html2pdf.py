# -*- coding: utf-8 -*-
#https://wkhtmltopdf.org/downloads.myhtml
#https://pypi.org/project/pdfkit/
#https://www.cnblogs.com/my8100/p/7738366.myhtml
import pdfkit
import sys,os

def get_special_file(given_dir='./result/',key_word='result',file_type='.html'):
    """
        获取特定目录的最新扫描文件名
    """
    """
    :param given_dir: str type, given DIR
    :return: str type, all file name in the given DIR
    """
    all_file_names=[]
    #print(given_dir)
    #print(os.walk(given_dir))
    obsolute_dif = given_dir
    if len(given_dir.split('.'))>2:
        print('输入的DIR格式错误，请检查DIR格式')
    elif './' in given_dir:#相对路径：
        current_dir = os.path.split(os.path.realpath(__file__))[0].replace('\\','/')
        obsolute_dir = current_dir + given_dir.split('.')[-1]
    for root,dirs,allfiles in os.walk(given_dir):
        if root==given_dir:
            for file in allfiles:
                if key_word in file and file_type in file:
                    all_file_names.append(obsolute_dir + file)
    all_file_names=sorted(all_file_names,reverse=True)
    return all_file_names

def get_untransfer_html(given_dir='./result/',key_word='result'):
    html_file_list = get_special_file(given_dir, key_word, file_type='.html')
    if not html_file_list:
        return []
    pdf_file_list = get_special_file(given_dir, key_word, file_type='.pdf')
    transferred_before = ',,'.join(pdf_file_list).replace('.pdf', '.html')
    transferred_before = transferred_before.split(',,')
    #print('transferred_before=',transferred_before)
    html_need_to_transfer = list(set(html_file_list).difference(set(transferred_before)))
    #print('html_need_to_transfer=',html_need_to_transfer)
    return html_need_to_transfer

def html2pdf0(dest_url='',result_dir='./result/',key_word='result',wkhtmltopdf_dir='',now_time_str='proxy_20180924'):
    """
    基于HTML report文件（以URL的形式）生成 PDF报告
    :param dest_url: str, 需要转换为PDF报告的目标URL，默认为空，实质指向: ./result/result.myhtml
    :param result_dir: str, PDF文件输出的目录，绝对路径；默认是result目录
    :param wkhtmltopdf_dir: str, 可执行文件wkhtmltopdf.exe的目录，觉得路径；默认为空，实质指向：C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe
    :param now_time_str: str,PDF文件的日期和有无代理标识。
    :return: none，无返回值
    """
    path_wk = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    if not wkhtmltopdf_dir:
        pass
    else:
        path_wk = wkhtmltopdf_dir + '/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    current_path = os.path.split(os.path.realpath(__file__))[0].replace('\\','/')
    if not dest_url:
        dest_url = 'file:///' + current_path + '/result/result.html'
    options = { 
        'page-size':'A4',
        'margin-top':'0.75in', 
        'margin-right':'0.75in',
        'margin-bottom':'0.75in',
        'margin-left':'0.75in',
        'encoding':"UTF-8",
        'no-outline':None
        }
    result_pdf_name = result_dir +  'aswg' + now_time_str + '.pdf'
    pk = pdfkit.from_url(dest_url,result_pdf_name,options=options,configuration=config)
    return

def html2pdf(dest_url='',result_pdf_name='',wkhtmltopdf_dir=''):
    """
    基于HTML report文件（以URL的形式）生成 PDF报告
    :param dest_url: str, 需要转换为PDF报告的目标URL，默认为空，实质指向: ./result/result.myhtml
    :param result_pdf_name: str, PDF文件输出的名字
    :param wkhtmltopdf_dir: str, 可执行文件wkhtmltopdf.exe的目录，觉得路径；默认为空，实质指向：C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe
    :param now_time_str: str,PDF文件的日期和有无代理标识。
    :return: none，无返回值
    """
    if '.html' not in dest_url:#无效url
        return
    if not result_pdf_name:
        current_path = os.path.split(os.path.realpath(__file__))[0].replace('\\','/')
        result_pdf_name = dest_url.split('/')[-1].replace('.html','.pdf')
        result_pdf_name = current_path + '/result/' + result_pdf_name
    path_wk = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    if not wkhtmltopdf_dir:
        pass
    else:
        path_wk = wkhtmltopdf_dir + '/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    options = { 
        'page-size':'A4',
        'margin-top':'0.75in', 
        'margin-right':'0.75in',
        'margin-bottom':'0.75in',
        'margin-left':'0.75in',
        'encoding':"UTF-8",
        'no-outline':None
        }
    print('result_pdf_name=',result_pdf_name)
    pk = pdfkit.from_url(dest_url,result_pdf_name,options=options,configuration=config)
    return

def html2pdfs(htmls=[]):
    """
    批量生成 PDF报告
    :param htmls: list, html文件的url列表
    :return: int，成功转换为PDF文件的数量
    """
    count = 0 
    for html in htmls:
        if ':' in html:
            if 'http://' in html.lower() or 'https://' in html.lower():
                pass
            elif '://' not in html and html[1]==':' and html.count(':')==1:  #本地磁盘html文件，转为可访问的url
                html = 'file:///' + html 
            else:
                print('无法识别的HTML URL路径: %s' % html)
                continue
        else:
            print('无效HTML URL路径：%s' % html)
            continue
        html2pdf(html)
        count = count + 1
    return count

if __name__=='__main__':
    print("----------------------使用说明--------------")
    print("该程序htmToPdf.exe用于把html文件转换为PDF文件！如需转换在线的html文件，请自行研究：wkhtmltopdf.exe")
    print("1. 请确认已经建立result目录和static目录")
    print('2. 默认先运行aswg.exe程序生成html文件，后运行htmlToPDF.exe程序')
    print("3. 默认不加任何参数将把./result/目录下尚未转换为PDF文件的html文件：转换为PDF文件。")
    print("4. 你也可指定目录-必须是绝对路径")
    print("----------------------End 使用说明--------------")
    #print('默认代理=',req.PROXIES)
    proxies = {}
    aswg_or_not = ''
    if len(sys.argv)>=2:
        if sys.argv[1] and isinstance(sys.argv[1], str):
            proxy = sys.argv[1]  #start date string
            if not proxy:
                aswg_or_not = '无'
                print('测试将不经过任何ASWG！！！')
    elif len(sys.argv)>3:
        print('输入过多参数，无效！！！退出')
        sys.exit()
    else:
        print('使用系统默认参数')
    print('----------------------生成PDF测试报告--------------')
    aswg_or_not = 'None'
    html_need_to_transfer = get_untransfer_html(given_dir='./result/',key_word='result')
    pdf_nums = 0
    if  html_need_to_transfer:
        pdf_nums = html2pdfs(html_need_to_transfer)
    else:
        print('无HTML文件需要转换为PDF文件')
    #pdf.html2pdf(dest_url='',result_dir='./result/',wkhtmltopdf_dir='',now_time_str=now_time_str)
    #xhtmlpdf.convertHtmlToPdf(base_html,'test1.pdf')
    print('----------------------完成 HTML转换为PDF报告,包含%s份PDF文件，位于result目录！--------------'% pdf_nums)   
    #print('all_summary=',all_summary)
