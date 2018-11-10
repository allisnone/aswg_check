# -*- coding: utf-8 -*-
from config import URL_MAPPING,IMAGE_STATUS

def get_summary_title_html(h3_content='综合评估',proxy='None',now_time='2018-09-24'):
    summary_title = '''
        <div style="width:100%;font-size: 18px; color: #2A2C30; font-weight:500;">
            <div class="test-result-div col-xs-6 col-sm-6">
                <h3 style="text-align:left;">{0}</h3>  
            </div>
            <div class="test-result-div col-xs-6 col-sm-6">
                <h4 style="text-align:right;"> 代理服务器：<p class="text-success">{1}</p> </h4>
                <h5 style="text-align:right;">{2}</h5>
            </div>
        </div>'''.format( h3_content,proxy,now_time)
    return summary_title

def get_L1_summary_html(h4_content='安全评估',loader_img='../static/images/loader.png',fail_img=IMAGE_STATUS['fail'],fail_count=0,
                        pass_img=IMAGE_STATUS['pass'],pass_count=0):
    pass_rate = 0
    result_class = 'text_primary'
    
    if (fail_count + pass_count)>0:
        pass_rate = round(round(pass_count,2)/(fail_count + pass_count),2)*100
        if pass_rate<50:
            result_class = 'text-danger' #text-wairning
        elif pass_rate<80:
            result_class = 'text-wairning' #text-wairning
        else:
            result_class = 'text-success' #text-wairning
    #<img src="{failimg}" style="height:16px; width:16px; margin: 26px 6px 8px 0px;">      
    pass_result = "{0}%".format(str(pass_rate).split('.')[0])
    percentage_result = '<span class="{0}" style="display:block;font-size:20px">{1}</span>'.format(result_class,pass_result)
    #col-xs-12 col-sm-12 col-md-4 col-lg-4
    l1_summary_html = ''' <div class="test-result-div col-xs-4 col-sm-4" style="background-color:#ffffff;">
        <div class="horizontal-align" style="width:255px;">
            <div style="width:100%; text-align:center;">
                <span style="font-size:16px; color: #2A2C30; font-weight:400;">
                    <h4>{head}</h4>
                </span>
                <div style="margin: 1px 1px 1px 1px;">
                    <div style="display:inline;width:100%">
                        <div class="col-xs-4 col-sm-4" style="margin: 0 0 0 0%;">
                            <img src="{failimg}" style="height:16px; width:16px; margin: 26px 6px 8px 0px;">
                            <p id="FailCountData" style="color:#D82D24; font-size:20px; display:inline; top:13px; position:relative;">{failcount}</p>
                            <span style="display:block; color: #4C4F54; word-wrap: break-word;">失败</span>
                        </div>
                        <div class="col-xs-4 col-sm-4" style="margin: 0 0 0 0%;">
                            <img src="{passimg}" style="height:16px; width:16px; margin: 26px 6px 8px 0px;">
                            <p id="PassCountData" style="color:#399C1D; font-size:20px; display:inline; top:13px; position:relative;">{passcount}</p>
                            <span style="display:block; color: #4C4F54;">成功</span>
                        </div>
                        <div class="col-xs-4 col-sm-4" style="margin: 0 0 0 0%;">
                            <p id="PassCountData" style="color:#399C1D; height:16px; width:16px; margin: 26px 6px 8px 0px; font-size:20px;text-align:left;">{percentage_result}</p>
                            <span style="display:block; color: #4C4F54;">成功率</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>\n'''.format(head=h4_content,percentage_result=percentage_result,ptgimg=pass_img,failimg=fail_img,failcount=fail_count,passimg=pass_img,passcount=pass_count)
        #%(h4_content,loader_img,fail_img,fail_count,pass_img,pass_count)
    
    return l1_summary_html

#get_L1_summary_html(fail_count=5,pass_count=12)
def get_sub_summary_html(h3_content='数据防泄漏',h4_content='数据保护',fail_img=IMAGE_STATUS['fail'],
                         fail_count=0,pass_img=IMAGE_STATUS['pass'],pass_count=0,section='dataProtection'):
    h3_html = '<h3>%s</h3> ' % h3_content
    h4_html = '<h4>%s</h4></div>' % h4_content
    fail_img_html = '    <img src="%s" style="width:15px; height:15px; margin:1px;">' % fail_img
    fail_count_html = '      <span id="dataProtectionFailCount" style="color:#D82D24;margin:5px;">%s</span> 失败' % fail_count
    pass_img_html = '    <img src="%s" style="width:15px; height:15px; margin:5px;">' % pass_img
    pass_count_html = '      <span id="dataProtectionPassCount" style="color:#399C1D;margin:5px;">%s</span> 成功' % pass_count
    sub_summary_html = ' <div id="dataProtection" class="container" style="display:block;padding:0;"> \
        <div style="font-size: 21px; font-weight:500; margin-bottom:10px;width:100%;"> ' + h3_html + '</div> <div style="display:inline;width:100%"> \
        <div id="dataProtectionClick"  class="col-xs-4 col-sm-4" style="display:flex; color:#009CDA;"> \
        <div id="dataProtectionGlyphicon" class="fa fa-chevron-down" style="padding:4px; padding-right: 8px;"></div> \
        <div style="font-size: 17px; font-weight:500;"> ' + h4_html + '</div> \
        <div id="dataProtectionResult" class="col-xs-8 col-sm-8" style="display:inline;"> \
        <div style="display:inline;margin-left:5%;">' + fail_img_html + '    <p style="color:#2A2C30;display:inline;"> ' + fail_count_html + '    </p> \
        </div> \
        <div style="display:flex; margin-left:3%;">' + pass_img_html + '    <p style="color:#2A2C30;display:inline;">' + pass_count_html + '    </p> \
        </div> \
        </div> \
        </div> \
        </div>'
    return sub_summary_html.replace('dataProtection',section)

def get_item_html(request_result,url_mapping=URL_MAPPING,image_status=IMAGE_STATUS,proxies={}):
    if not request_result or not url_mapping:
        return ''
    config_id = request_result[0]
    http_status = request_result[3]
    aswg_status = request_result[4]
    #aswg_status_html = '<img src="' + aswg_status + '" style="width:15px; height:15px; margin:5px;">'
    status_img = IMAGE_STATUS['pass']
    text_class = 'text-primary'
    if http_status==200:
        status_img = IMAGE_STATUS['fail']
        text_class = 'text-danger' #text-wairning
    test_name = URL_MAPPING[config_id]['name']
    test_detail = URL_MAPPING[config_id]['detail']
    #test_description = URL_MAPPING[config_id]['description']
    row_html = '''<div class="row {text_class}" style="display:flex;width:100%;background-color:#ffffff;"> 
        <div class="col-xs-1 col-sm-1" style="display:inline;"> 
        <div> <img src="{status_img} "style="width:15px; height:15px; margin:5px;"> </div>
        </div> 
        <div class="col-xs-3 col-sm-3" style="display:inline;"> <p> {test_name}</p></div> 
        <div class="col-xs-2 col-sm-2" style="display:inline;"> 
        <div> <p> {aswg_status} </p></div>
        </div> 
        <div class="col-xs-6 col-sm-6" style="display:inline;text-align:left;"> 
        <p>{test_detail}</p>
        </div> 
        </div>'''.format(text_class=text_class,status_img=status_img,test_name=test_name,aswg_status=aswg_status,test_detail=test_detail)
    return row_html;

def form_head_element():
    head_html =  '<div class="row" style="width:100%;"> \
        <div class="col-xs-1 col-sm-1" style="display:inline;"> <p> 状态 </p></div>  \
        <div class="col-xs-3 col-sm-3" style="display:inline;"> <p> 测试分类 </p></div> \
        <div class="col-xs-2 col-sm-2" style="display:inline;"> <p> 阻断 </p></div> \
        <div class="col-xs-6 col-sm-6" style="display:inline;text-align:center;"> <p> 测试描述 </p></div> \
        </div>'
    return  head_html

"""
def get_sub_section_html(requesection='accessControl'):
    
    return 

print(get_sub_summary_html(section='accessControl'))

request_result = ['31', 'http://www.sogaoqing.com/post.php', 'post.php', 403, 'DLP_BLOCK', {'content': '', 'file': 'static/sample/cn_id_info.doc'}]
row_html = get_item_html(request_result,url_mapping=URL_MAPPING,image_status=IMAGE_STATUS,proxies={})
print('row_html=',row_html)
"""