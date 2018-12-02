# -*- coding: utf-8 -*-
import re
import os
import csv
import json
import string
import requests
from urllib.parse import quote
from config import VIRUS_BLOCK_INFO,URL_BLOCK_INFO,DLP_BLOCK_INFO,PROXIES,SECURITY_CONFIG,REPLACE_KEYS,reverse_str
import random,sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
import html_create as html
#pip install requests_toolbelt
#from aswg.config import SECURITY_CONFIG
import datetime
#import pdf
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def encodeURL(url):
    """
    处理包含中文字符串/空格的URL编码问题
    :param url:
    :return:
    """
    return quote(url, safe=string.printable).replace(' ', '%20')

def get_block_info(response_text):
    if VIRUS_BLOCK_INFO in response_text:
        return 'VIRUS_BLK'
    elif URL_BLOCK_INFO in response_text:
        return 'URL_BLK'
    elif DLP_BLOCK_INFO in response_text:
        return 'DLP_BLK'
    else:
        return 'OTHER_BLK'

def http_request(url,uri='',params={},type='get',headers={},proxy=PROXIES):
    """
    下载文件，分析是否被SWG阻断
    :param url:
    :return: callback
    """
    try:
        r = None
        if uri:
            url = ''.join([url,uri])
        if type.lower()=='get':
            print('get_url=',url)
            r = requests.get(encodeURL(url), params=params, proxies=proxy, verify=False)
        elif type.lower()=='post':
            print(encodeURL(url))
            print('params=',params)
            print('headers=',headers)
            
            r = requests.post(encodeURL(url),data=params,headers=headers,proxies=proxy,verify=False)
            #sogaoqing_post(post_data,post_url='http://www.sogaoqing.com/post.php',proxies=PROXIES,
        else:
            return []
        r.encoding = 'utf-8'
        #print(url, r.text)
        if r.status_code == 403:
            block_info = get_block_info(r.text)
            return [url, url.split('/')[-1], r.status_code, block_info]
        else:
            return [url, url.split('/')[-1], r.status_code, 'pass']
    except Exception as e:
        print('ERROR=',e)
        return [url, url.split('/')[-1], 0, e]
    
def get_request(url,params={},proxy=PROXIES):
    return http_request(url,type='get',proxy=PROXIES)

def post_request(url,uri='',params={},headers={},proxy=PROXIES):
    return http_request(url,uri=uri,params=params,type='post',headers=headers,proxy=PROXIES)

def is_proxy_workable(proxy=PROXIES):
    url='http://www.sogaoqing.com'
    try:
        r = requests.get(encodeURL(url), proxies=proxy, verify=False)
        return True
    except Exception as e:
        print('ERROR=',e)
        return False
    

def write2csv(data):
    try:
        with open('aswg_result.csv', 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    except Exception as e:
        print(e)
        
def get_url_mapping(SECURITY_CONFIG):
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    result= {}
    for li in data_threat:
        result[li['id']]=li
        
    for li in data_access:
        result[li['id']]=li
    
    for li in data_protection:
        result[li['id']]=li    
    return result
        
def get_all_http_result(proxy=PROXIES,config={}):
    data_threat = config['Security Assessment']['Threat Prevention']
    print('您的公网IP是： %s' % get_my_public_ip())
    for data in data_threat:
        pass
    return    

def get_my_public_ip():#from ip138
    #从ip138获取本机的公网IP
    url = 'http://%s.ip138.com/ic.asp' % datetime.datetime.now().year
    r = requests.get(encodeURL(url),verify=False)
    r.encoding = 'gb2312'
    pattern = re.compile(r'(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')
    #str = re.findall(pattern, r.text)
    return pattern.search(r.text).group()
#get_all_http_result()
#print(get_my_public_ip())
#print(get_url_mapping())    

#print(len(get_url_mapping()))  
#print("您的公网IP地址是： ",get_my_public_ip())

def form_sogaoqing_data(content='',file_name=''):
    """
    生成sogaoqing post的payload
    :param content: str, post的内容
    :param file_name: str，post的文件名，绝对路径
    :return: dict, 返回字典
    """
    return {'content': content,'file':file_name}

def sogaoqing_post(post_data,url='http://www.sogaoqing.com/post.php',proxies=PROXIES,enconding='utf-8'):
    """
    通过 post的方法向sogaoqing提交 内容，或者文件
    :param post_data: dict type, post的数据， 来源 form_sogaoqing_data()
    :param url: str type, post 方法的模板url，默认指向sogaoqing
    :param proxies: dict type, ASWG 代理, 默认是华为ASWG代理
    :param enconding: str type, HTTP reponse的编码格式，默认是utf-8
    :return: str，返回HTTP的response
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0', 
        'Referer': url }
    #print(os.path.basename(post_data['file']))
    multipart_encoder = MultipartEncoder(
        fields={
            #'username': argv_dict['username'],
            #'pwd': argv_dict['pwd'],
            #'type': 'txt',
            #'friendfield': argv_dict['friendfield'],
            #'friend': argv_dict['friend'],
            'content': post_data['content'],
            'file': (os.path.basename(post_data['file']), open(post_data['file'], 'rb'), 'application/octet-stream') 
                                                      #file为路径 
                },
        boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))
        )
    headers['Content-Type'] = multipart_encoder.content_type 
    #请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data;#boundary=${bound} 
    r = requests.post(url, data=multipart_encoder, headers=headers,proxies=proxies) 
    r.encoding = enconding
    #print(r.text)
    return r

def sogaoqing_http_request(url,uri='',params={},type='get',headers={},proxy=PROXIES):
    """
    下载文件，分析是否被SWG阻断
    :param url:
    :return: callback
    """
    try:
        r = None
        if uri:
            url = ''.join([url,uri])
        if type.lower()=='get':
            #print('get_url=',url)
            r = requests.get(encodeURL(url), params=params, proxies=proxy, verify=False)
            r.encoding = 'utf-8'
        elif type.lower()=='post':
            #r = requests.post(encodeURL(url),data=params,headers=headers,proxies=proxy,verify=False)
            #print(encodeURL(url))
            r = sogaoqing_post(params,url=encodeURL(url),proxies=proxy)
        else:
            return []
        
        #print(url, r.text)
        if r.status_code == 403:
            block_info = get_block_info(r.text)
            return [url, url.split('/')[-1], r.status_code, block_info,params]
        elif r.status_code == 200:
            return [url, url.split('/')[-1], r.status_code, 'FAIL_BLK',params]
        else:
            return [url, url.split('/')[-1], r.status_code, 'OTHER',params]
    except Exception as e:
        print('ERROR=',e)
        return [url, url.split('/')[-1], 0, e,params]

def initial_summary(total_num,status=[]):
    
    block_403 = {}
    for block in status:
        if block not in block_403.keys():
            block_403[block] = 0
    block_403.update({'403_TOTAL':0,'403_OTHER':0})
    sumary = {
        'total':total_num,
        '200_ok':0,
        '403_block':block_403,
        'other':0,
        }
    return sumary

def combile_L2_summary(summary_list):
    if not summary_list:
        return {}
    elif len(summary_list)==1:
        return summary_list[0]
    else:
        all_summary = summary_list.pop(0)
        for sub in summary_list:
            for key in sub.keys():
                if key!='403_block':
                    all_summary[key] = all_summary[key] + sub[key]
                else:
                    block_403 = sub['403_block']
                    for sub_403 in block_403.keys():
                        all_summary[key][sub_403] = all_summary[key][sub_403] + block_403[sub_403]
        return all_summary

def get_aswg_category_result(datas,proxy=PROXIES):
    #data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    ASWG_BLOCK_STATUS = ['DLP_BLK','VIRUS_BLK','URL_BLK']
    all_results = []
    total_num =len(datas)
    sumary = initial_summary(total_num, ASWG_BLOCK_STATUS)
    sub_section_html = html.form_head_element()
    for item in datas:
        url = item['urls']
        if not url:
            continue
        para_data = item['para']
        request_type = item['method']
        test_id = item['id']
        sub_result = sogaoqing_http_request(url,params=para_data,type=request_type,proxy=proxy)
        if sub_result:
            #print('test_id=%s :'% test_id,sub_result)
            http_status = sub_result[2]
            if http_status==200:
                sumary['200_ok'] = sumary['200_ok'] + 1
            elif http_status==403:
                sumary['403_block']['403_TOTAL'] = sumary['403_block']['403_TOTAL'] + 1
                aswg_status = sub_result[3]
                if aswg_status in ASWG_BLOCK_STATUS:
                    sumary['403_block'][aswg_status] = sumary['403_block'][aswg_status] + 1
                else:
                    sumary['403_block']['403_OTHER'] = sumary['403_block']['403_OTHER'] + 1
            else:
                sumary['other'] = sumary['other'] + 1
            sub_result.insert(0,test_id)
            """
            form html here
            """
            row_html = html.get_item_html(sub_result,proxies=proxy)
            sub_section_html = sub_section_html + row_html
            
            all_results.append(sub_result)
        else:
            print('No result')
    sumary['other'] = total_num-sumary['403_block']['403_TOTAL'] -  sumary['200_ok']
    return all_results,sumary,sub_section_html

def form_html_block(item_result=[]):
     
    
    return

def read_base_html(htlm='./static/template/base.html',encoding='utf-8'):
    f = open(htlm,'r', encoding=encoding)
    result = f.read()
    f.close()
    return result

def write_final_html(html_content,file_name='./result/result.html',encoding='utf-8'):
    with open(file_name,'w',encoding=encoding) as f:
        f.write(html_content) 
    f.close()
    return

def replace_base_html_block(base_html,replace_key,replace_content):
    return base_html.replace(replace_key,replace_content)

def get_aswg_result(conf=SECURITY_CONFIG,proxy=PROXIES):
    """
    REPLACE_KEYS= {
    'Summary Title': 'ALL_SUMMARY_TITLE999',
    'Security Assessment': 'SECURITY_ASSESSMENT_SUMMARY999', 
    'Data Protection': 'DATA_PROTECTION_SUMMARY999', 
    'Access Control': 'ACCESS_CONTROL_SUMMARY999', 
    'Data Protection Assessment': 'DATA_PROTECTION_ASSESSMENT_SUMMARY999', 
    'Threat Prevention': 'THREAT_PREVENTION_SUMMARY999',
    'Data Protection Result': 'DATA_PROTECTION_RESULT999',
    'Threat Prevention Result': 'THREAT_PREVENTION_RESULT999', 
    'Access Control Result': 'ACCESS_CONTROL_RESULT999'
    }
    """
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    #print('data_threat',data_threat)
    now_time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    now_time = datetime.datetime.now().strftime('%A %Y-%m-%d %H:%M:%S %p')
    base_html = read_base_html()
    proxy_str = 'None'
    if proxy:
        proxy_str = proxy['http']
    else:
        pass
    summary_html = html.get_summary_title_html(h3_content='综合评估',proxy=proxy_str,now_time=now_time)
    base_html = base_html.replace(REPLACE_KEYS['Summary Title'],summary_html)
    all_summary_list = []
    all_summary = {}
    for L1 in conf.keys():
        if conf[L1]:
            pass
        else:
            continue
        L1_summary_list = []
        for L2 in conf[L1].keys():
            if conf[L1][L2]:
                pass
            else:
                continue
            
            l2_h3_content = '数据防泄漏'
            l2_h4_content = '数据保护'
            l2_section = 'dataProtection'
            if L2=='Access Control':
                l2_section = 'accessControl'
                l2_h3_content = ''
                l2_h4_content = '访问控制'
            elif L2=='Threat Prevention':
                l2_section = 'threatPrevention'
                l2_h3_content = '安全防护'
                l2_h4_content = '威胁防护'
            else:
                pass
            sub_result,L2_sumary,sub_section_html = get_aswg_category_result(conf[L1][L2],proxy=proxy)
            l2_pass_count = L2_sumary['total'] - L2_sumary['200_ok']
            sub_summary_html = html.get_sub_summary_html(h3_content=l2_h3_content,h4_content=l2_h4_content,
                         fail_count=L2_sumary['200_ok'],pass_count=l2_pass_count,section=l2_section)
            print(L2,' L2 detail: ',sub_result)
            print(L2,' L2 summary: ',L2_sumary)
            l2_result_key = L2 + ' Result'
            #替换子项的总结
            base_html = base_html.replace(REPLACE_KEYS[L2],sub_summary_html)
            #替换子项的具体行
            base_html = base_html.replace(REPLACE_KEYS[l2_result_key], sub_section_html)
            L1_summary_list.append(L2_sumary)
        #汇总L1的summary
        L1_summary = combile_L2_summary(L1_summary_list)
        all_summary[L1] = L1_summary
        #替换base HTML的分项总结：Security Assessment 和 Data Protection Assessment
        l1_h4_content='安全评估'
        if L1== 'Data Protection Assessment':
            l1_h4_content = '数据评估'
        l1_fail_count = L1_summary['200_ok']
        l1_pass_count = L1_summary['total'] - L1_summary['200_ok']
        L1_summary_html = html.get_L1_summary_html(l1_h4_content,loader_img='../static/images/loader.png',
                                                   fail_count=l1_fail_count,pass_count=l1_pass_count)
        base_html = base_html.replace(REPLACE_KEYS[L1],L1_summary_html)
        L1_summary_html = ''
        all_summary_list.append(L1_summary)
    #汇总全部summary
    all_summary['all'] = combile_L2_summary(all_summary_list) 
    all_fail_count = all_summary['all']['200_ok']
    all_pass_count = all_summary['all']['total'] - all_summary['all']['200_ok']
    all_summary_html = html.get_L1_summary_html(h4_content='综合评估',loader_img='../static/images/loader.png',
                                                fail_count=all_fail_count,pass_count=all_pass_count)
    base_html = base_html.replace(REPLACE_KEYS['All Summary Result'],all_summary_html)
    #替换生成最终综合结论的HTML
    #write_final_html(base_html,file_name='./result/result_%s.html'%now_time_str)
    #print('Write the result as HTML: %s'% file_name)
    return  all_summary,base_html,now_time_str
"""            
if __name__ == '__main__':
    #print("您的公网IP地址是： ",get_my_public_ip())
    print('PROXIES=',PROXIES)
    #PROXIES={}
    all_summary = get_aswg_result(proxy=PROXIES)
    print('all_summary=',all_summary)
"""