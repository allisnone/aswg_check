# -*- coding: utf-8 -*-
#from source_ulrs import *
from source_urls import EXE_URLS, MALICIOUS_WEBSITES, PHISHING_ATTACK,\
    SESSION_HIJACKING, BOTNET_CALLBACK, CROSS_SITE_SCRIPTING,\
    OLDER_KNOWN_VIRUSES, VIRUS_HIDDEN_IN_ZIP,\
    COMMON_VIRUS_FROM_KNOWN_MALICIOUS_SITE, ANONYMIZING_WEBSITES,\
    VOILENCE_WEAPON, ADULT_WEBSITES, CREDIT_CARD, SOCIAL_SECURITY_NUMBER,\
    SOURCE_CODE,INTERAL_URL,INTERAL_POST_URL,CROSS_POST_URL

VIRUS_BLOCK_INFO = "访问的URL中含有安全风险"
URL_BLOCK_INFO = '本次访问违反了公司的网络安全策略'
DLP_BLOCK_INFO = '本次访问违反了公司的数据防泄漏策略'
#PROXIES = {'http': 'http://172.18.200.240:8080'}
PROXIES = {'http': 'http://49.4.84.41:8066'}
IMAGE_STATUS = {'pass':'../static/images/pass.png','fail':'../static/images/fail.png'}

SECURITY_CONFIG = {
    'Security Assessment': {
        'Threat Prevention': [
            #'Block an executable (.exe) download': 
                {
                'name':'可执行文件下载',
                'urls':EXE_URLS,
                'detail':'测试是否可以直接下载可执行文件，exe文件是病毒最常见载体之一',
                'description':'This test tries to download an executable file from a website with a good reputation that uses a Content Distribution Network (CDN) like Akamai or AWS. It tests whether your security infrastructure can block the executable, limiting the possible introduction of malware and other threats.',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'1',
                
                },
                              
            #'Block threats in known malicious websites': 
                {
                'name':'恶意木马网站访问',
                'urls':MALICIOUS_WEBSITES,
                'detail':'测试是否阻止访问恶意木马网站，测试不会直接下载木马软件',
                'description':'This test checks to see if a benign object hosted on a known malicious site is blocked by your security solution. It uses a \
                compromised site from a list published by Google. The test does not attempt to download actual malware.',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'2',
                },
                              
            #'Detect a phishing attack': 
                {
                'name':'钓鱼网站访问',
                'urls': PHISHING_ATTACK,
                'detail':'测试是否识别并阻止访问钓鱼网站，来源于 Phishtank.com权威识别的最新钓鱼站点 ',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'3',
                },
            #'Block a virus hidden in a zip file': 
                {
                'name':'压缩文件病毒',
                'urls':VIRUS_HIDDEN_IN_ZIP,
                'detail':' 测试是否可以识别压缩文件中的病毒',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'4',
                },
                              
            #'Prevent a common virus from a known malicious site': 
                {
                'name':'普通病毒',
                'urls': OLDER_KNOWN_VIRUSES,
                'detail':' 测试是否识别已知病毒，来源权威病毒网站-卡饭',
                'description':'待描述',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'5',
                }
            ],
        'Access Control':[
            #'Block websites in embargoed countrie': 
                {
                'name':'暴力武器网站访问',
                'urls': VOILENCE_WEAPON,
                'detail':'测试是否可以识别并阻止访问宣扬暴力的网站',
                'description':'This test tries to connect to websites in countries under embargo by the Unites States and European Union, such as North Korea. Most companies want to prevent users from connecting to websites in countries that are under embargo in order to comply with trade laws. Additionally, compromised websites are often hosted in countries that are hostile to the United States and the European Union, and they place a low priority on Internet security. ',
                'method': 'get',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'21',
                },
                          
            #'Block access to adult websites': 
                {
                'name':'成人网站访问',
                'urls': ADULT_WEBSITES,
                'method': 'get',
                'detail':'测试是否识别并阻止访问涉黄成人网站',
                'description':'待定',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {},
                'id':'22',
                },
            
            ]
        },
    'Data Protection Assessment': {
        'Data Protection': [
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'验证是否可以识别并保护个人隐私信息外泄',
                'description':'个人隐私信息包括信用卡号，手机号、中国护照号',
                'icon': '../static/images/icon1.bmp',
                'cross': '2',
                'type': 'html',
                'para': {'content':'','file':'static/sample/cn_id_info.doc'},
                'id':'31',
                },
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'测试识别并防止包含隐私信息的图片外发',
                'description':'隐私信息图片外发',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {'content':'','file':'static/sample/business_card.jpg'},
                'id':'32',
                },
            #'Block credit card exfiltration': 
                {
                'name':'个人隐私信息保护',
                'urls': CROSS_POST_URL,#CREDIT_CARD,
                'method': 'POST',
                'detail':'测试包含隐私信息Word,Excel等文档外发',
                'description':'隐私信息Word,Excel外发',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'html',
                'para': {'content':'','file':'static/sample/employee.xls'},
                'id':'33',
                },
                            
                            
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试是否识别并阻止包含企业标准合同，财务报表等敏感信息外泄',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': {'content':'','file':'static/sample/contract.pdf'},
                'id':'34',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试识别并保护源代码外泄',
                'description':'企业核心源代码保护，Java，Python，C/C++等源代码保护',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': {'content':'','file':'static/sample/finance_report.pdf'},
                'id':'35',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试识别并保护企业薪酬福利信息外泄',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': {'content':'','file':'static/sample/salary.doc'},
                'id':'36',
                },
            #'Block Social Security number exfiltration': 
                {
                'name':'企业机密保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'网络拓扑图，Password/Shadow文件上传',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'json',
                'para': {'content':'','file':'static/sample/passwd'},
                'id':'37',
                },
        
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试言论是否包含淫秽文字',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/sex_photo.jpg'},
                'id':'38',
                },
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'暴力武器 ',
                'description':'涉及暴力言论，武器出售转让等言论',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/weapons_violence.txt'},
                'id':'39',
                },
            #'Block source code exfiltration': 
                {
                'name':'不正当言论',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试识别并阻止反党反政府等言论传播 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/anti_party.txt'},
                'id':'40',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'测试识别病人住院信息、病患病症等外泄',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/hospital.pdf'},
                'id':'41',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'健康病症，体检报告 ',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/hospital.pdf'},
                'id':'42',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'保险理赔',
                'description':'待完善',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/insurance.pdf'},
                'id':'43',
                },
            #'Block source code exfiltration': 
                {
                'name':'行业特点信息保护',
                'urls': CROSS_POST_URL,
                'method': 'POST',
                'detail':'AutoCAD图纸 ',
                'description':'工程设计图纸',
                'icon': '../static/images/fail.png',
                'cross': '2',
                'type': 'text',
                'para': {'content':'','file':'static/sample/design_drawing.pdf'},
                'id':'44',
                }
            ]
        }
    }

def reverse_str(a='abc def'):
    b = list(a)
    b.reverse()
    return ''.join(b)

def get_url_mapping():
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
    
    replace_key = {}
    summary_key = '_SUMMARY'
    sub_summary_key = '_RESULT'
    section_key = ' Result'
    for L1 in SECURITY_CONFIG.keys():
        if L1 not in replace_key.keys():
            replace_key[L1] = reverse_str(L1).upper().replace(' ','_') + summary_key + '999'
        for L2 in SECURITY_CONFIG[L1].keys():
            if L2 not in replace_key.keys():
                replace_key[L2] = reverse_str(L2).upper().replace(' ','_') + summary_key + '888'
                replace_key[L2 + section_key] = L2.upper().replace(' ','_') + sub_summary_key + '888'
    return result,replace_key

URL_MAPPING,REPLACE_KEYS = get_url_mapping()
REPLACE_KEYS['Summary Title'] = 'ALL_SUMMARY_TITLE999'
REPLACE_KEYS['All Summary Result'] = 'SUMMARY_ALL_RESULT999'
#print(SECURITY_CONFIG)
#print('REPLACE_KEYS=',REPLACE_KEYS)
"""
REPLACE_KEYS= {
    'Summary Title': 'ALL_SUMMARY_TITLE999',
    'Security Assessment': 'TNEMSSESSA_YTIRUCES_SUMMARY999', 
    'Data Protection': 'NOITCETORP_ATAD_SUMMARY999', 
    'Access Control': 'LORTNOC_SSECCA_SUMMARY999', 
    'Data Protection Assessment': 'TNEMSSESSA_NOITCETORP_ATAD_SUMMARY999', 
    'Threat Prevention': 'NOITNEVERP_TAERHT_SUMMARY999',
    'Data Protection Result': 'DATA_PROTECTION_RESULT999',
    'Threat Prevention Result': 'THREAT_PREVENTION_RESULT999', 
    'Access Control Result': 'ACCESS_CONTROL_RESULT999'
    }
"""
