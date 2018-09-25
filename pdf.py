# -*- coding: utf-8 -*-
#https://wkhtmltopdf.org/downloads.html
#https://pypi.org/project/pdfkit/
#https://www.cnblogs.com/my8100/p/7738366.html
import pdfkit
import os

def html2pdf(dest_url='',result_dir='./result/',wkhtmltopdf_dir='',now_time_str='proxy_20180924'):
    """
    基于HTML report文件（以URL的形式）生成 PDF报告
    :param dest_url: str, 需要转换为PDF报告的目标URL，默认为空，实质指向: ./result/result.html
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
        'page-size':'letter',
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
