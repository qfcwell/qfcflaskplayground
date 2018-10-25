# -*- coding:utf-8 -*-
from pyh import *
import pandas as pd
import datetime
import numpy as np

class CapolHtml_TablePage():
    def __init__(self):
        self.page=PyH('CAPOL_WEB_UI')
        self.head=self.page.head
        self.body=self.page.body
        self.body.attributes['style']='min-width:1600px;'
        self.css=[]
        self.js=[]
        self.page_css=''
        self.page_js=''
        self.top=div(div(cl="navigate"),cl='top_banner')
        self.top.div.addObj(div(img(onclick="Com_openHomePageFunc();",alt="",src="http://cip.capol.cn/capol/homepage/resource/img/logo.png"),cl="logo",style="cursor:pointer;"))
        self.top.div.addObj(div(ul(li(span('个人空间',cl="personalspace c_nav_info")),li(span('工作空间',cl="workspace c_nav_info active")),li(span('知识中心',cl="knowledge")),li(span('企业文化',cl="cultur"))),cl="c_nav"))
        self.top.div.addObj(div(input(id="fullSearch_input",type="text",placeholder="请输入关键字搜索全系统"),span(span(cl="glyphicon glyphicon-search"),cl="search-btn"),cl="search"))
        self.breadcrumb=ul(cl="breadcrumb",role="tablist")
        self.tab1_left=div(ul(cl="nav nav-tabs",role="tablist"))
        self.tab1_right=div(ul(cl="nav nav-tabs",role="tablist"))
        self.nav_tree=div(ul(),cl="nav nav-tree",style="width:240px;position: absolute;margin-left:20px;margin-top:10px;")
        self.main_frame=div(style="padding-left:280px;padding-right: 20px;")
        self.tab2=div(ul(cl="nav nav-tabs",role="tablist"),style="height:33px;margin-top:10px;")
        self.no_selection=select(option('不限',value=''),id="filter-company",cl="combobox",style="width:80px;")
        self.comp_selection=select(option('不限',value=''),option('集团公司',value=''),option('深圳公司',value=''),option('广州公司',value=''),option('上海公司',value=''),option('长沙公司',value=''),id="filter-company",cl="combobox",style="width:80px;")
        self.dept_selection=select(option('不限',value=''),id="filter-dept",cl="combobox",style="width:80px;")
        self.stage_selection=select(option('初步设计',value=''),option('施工图',value=''),id="filter-dept",cl="combobox",style="width:80px;")
        self.selection=div(style="height:48px;")
        self.select_year=div(span('年份',style='font-weight:bold;'),select(option('不限',value=''),option('2018',value=''),option('2017',value=''),option('2016',value=''),option('2015及以前',value=''),id="filter-module",cl="combobox",style="width:60px;"),cl="select-item")
        self.select_company=div(span('所属公司',style='font-weight:bold;'),self.comp_selection,cl="select-item")
        self.select_dept=div(span('所属部门',style='font-weight:bold;'),self.dept_selection,cl="select-item",style="padding-right: 40px;")
        self.select_dept1=div(span('一级部门',style='font-weight:bold;'),self.dept_selection,cl="select-item")
        self.select_dept2=div(span('二级部门',style='font-weight:bold;'),self.dept_selection,cl="select-item")
        self.select_keywords=div(span('关键字',cl="float",style='font-weight:bold;margin-top:8px;'),div('<input class="form-control input-sm" type="text" placeholder="名称、内容、负责人……" style="width:200px;border-right:0px;"><span class="input-group-search-btn"> 搜索</span>',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;margin-left:100px;")
        self.select_prjno=div(span('工程编号',cl="float",style='font-weight:bold;margin-top:8px;'),div('<input class="form-control select" type="text" style="width:80px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px; ")
        self.select_prjname=div(span('工程名称',cl="float",style='font-weight:bold;margin-top:8px;'),div('<input class="form-control select" type="text" style="width:200px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;")
        self.dgn_manager=div(span('方案负责人',cl="float",style='font-weight:bold;margin-top:8px;'),div('<input class="form-control select" type="text" style="width:80px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;")
        self.prj_manager=div(span('项目负责人',cl="float",style='font-weight:bold;margin-top:8px;'),div('<input class="form-control select" type="text" style="width:80px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;")
        self.select_prjcomp=div(span('项目所属公司',style='font-weight:bold;'),self.comp_selection,cl="select-item")
        self.select_prjdept=div(span('项目所属部门',style='font-weight:bold;'),self.dept_selection,cl="select-item")
        self.select_prjstage=div(span('工程阶段',style='font-weight:bold;'),self.stage_selection,cl="select-item")
        self.select_subentry=div(span('子项',style='font-weight:bold;'),self.no_selection,cl="select-item")
        self.selection_br=div(style='clear:both;')
        self.prj_status_checkbox=''
        self.prj_stage_checkbox=''
        self.major_checkbox=''
        self.opinion_type_checkbox=''
        self.hr_status=self.generate_checkbox('人员状态',lst=['全部','在职','离职'],checked=[1])
        self.tabletitle=div(cl="table-title clearFix")
        self.tabletools=''
        self.table=table(cl="table table-bordered")
        self.form_window=''
        
        

    def generate_checkbox(self,objname,lst=[],checked=[]):
        if lst:
            obj=div(div(objname,"：&nbsp;&nbsp;",style='height:24px;float:left;font-weight: bold;'),cl="checkbox",style="margin-left: 5px; padding-right:100px;float: left;margin-top:10px;margin-bottom:10px;")
            for item in lst:
                if item in checked:
                    obj.addObj(label(input(type="checkbox",checked='true'),item+'&nbsp;'))
                else:
                    obj.addObj(label(input(type="checkbox"),item+'&nbsp;'))
            return obj
        else:
            return ''   

    def set_status_checkbox(self,lst=[],checked=[]):
        if lst==[]:
            lst=['全选','投标','规划','方案','初步设计','施工图','施工服务','待启动','暂停','合同履约完成','竣工','终止']
            checked=['投标','规划','方案','初步设计','施工图','施工服务','待启动','暂停']
        self.prj_status_checkbox=self.generate_checkbox('工程状态',lst=lst,checked=checked)

    def set_major_checkbox(self,lst=[],checked=[]):
        if lst==[]:
            lst=['全部','建筑','结构','给排水','电气','暖通','其他']
            checked=range(7)
        self.major_checkbox=self.generate_checkbox('专业',lst=lst,checked=checked)

    def set_stage_checkbox(self,lst=[],checked=[]):
        if lst==[]:
            lst=['全部','投标','规划','方案','初设','施工图','施工服务']
            checked=range(7)
        self.prj_stage_checkbox=self.generate_checkbox('工程阶段',lst=lst,checked=checked)

    def set_opinion_type_checkbox(self,lst=[],checked=[]):
        self.opinion_type_checkbox=self.generate_checkbox('意见类型',lst=lst,checked=checked)

    def set_selection(self,type=0,selection=[],checkbox=[],underline=True):
        if type==1:
            if underline:
                self.selection=div(style="width:100%;border-bottom: 1px solid #ccc;")
            else:
                self.selection=div(style="width:100%")
            if selection:
                self.selection.addObj(div(div(style="height:48px;width:100%;"),style="width:100%;float: left;"))
            else:
                self.selection.addObj(div(div(style="height:10px;width:100%;"),style="width:100%;float: left;"))
            for item in selection:
                self.selection_dict={
                '所属公司':self.select_company,'所属部门':self.select_dept,'项目所属公司':self.select_prjcomp,'项目所属部门':self.select_prjdept,
                '一级部门':self.select_dept1,'二级部门':self.select_dept2,
                '年份':self.select_year,'工程阶段':self.select_prjstage,'工程编号':self.select_prjno,'工程名称':self.select_prjname,'方案负责人':self.dgn_manager,'项目负责人':self.prj_manager,
                '子项':self.select_subentry,'关键字':self.select_keywords,'br':self.selection_br}
                self.selection.div[0].addObj(self.selection_dict[item])
            for item in checkbox:
                self.checkbox_dict={'专业':self.major_checkbox,'工程阶段':self.prj_stage_checkbox,'工程状态':self.prj_status_checkbox,'人员状态':self.hr_status,'意见类型':self.opinion_type_checkbox}
                self.selection.div.addObj(self.checkbox_dict[item])
            self.selection.addObj(div(style='clear:both;'))
        else:
            self.selection.addObj(self.select_year)
            self.selection.addObj(self.select_company)
            self.selection.addObj(self.select_dept)
            self.selection.addObj(self.select_keywords)

    def set_breadcrumb(self,lst=[]):
        self.breadcrumb.addObj(li(a(span(cl="glyphicon glyphicon-home",aria_hidden="true"),'首页',href="#")))
        for (name,href) in lst:
            if href:
                self.breadcrumb.addObj(li(a(name,href=href)))
            else:
                self.breadcrumb.addObj(li(name))
    
    def set_tab1_left(self,lst=[],active=0,width='50%'):
        if width:
            self.tab1_left.attributes['style']="height:42px;width:"+width+";display: inline-block;"
        else:
            self.tab1_left.attributes['style']="height:42px;display: inline-block;"
        if lst:
            for (name,href) in lst:
                self.tab1_left.ul.addObj(li(a(name,href=href,cl="disabled"),role="presentation"))
            if active:
                self.tab1_left.ul[active-1].attributes['cl']='active'
                self.tab1_left.ul[active-1].a.attributes['cl']=''
        else:
            self.tab1_left=''

    def set_tab1_right(self,lst=[],active=0,width='50%'):
        if width:
            self.tab1_right.attributes['style']="height:42px;width:"+width+";display: inline-block;float: right;"
        else:
            self.tab1_right.attributes['style']="height:42px;display: inline-block;float: right;"
        if lst:
            for (name,href) in lst:
                self.tab1_right.ul.addObj(li(a(name,href=href,cl="bordered"),role="presentation",cl="right"))
            if active:
                self.tab1_right.ul[active-1].attributes['cl']='active'
        else:
            self.tab1_right=''

    def set_nav_lst1(self,lst=[],active=0):
        for (name,href) in lst:
            self.nav_tree.ul.addObj(li(a(name,span(cl="glyphicon glyphicon-triangle-bottom triangle-bottom"),href=href,cl='lv1')))

    def set_nav_lst2(self,index=0,lst=[],active=0):
        self.nav_tree.ul[index-1].addObj(ul(style="display: block;"))
        for (name,href) in lst:
            self.nav_tree.ul[index-1].ul.addObj(li(a(name,href=href)))
        if active:
            self.nav_tree.ul[index-1].ul[active-1].a.attributes['cl']='active'


    def set_tab2(self,lst=[],active=0):
        if lst:
            for (name,href) in lst:
                self.tab2.ul.addObj(li(a(name,cl="sm",href=href),role="presentation"))
            if active:
                self.tab2.ul[active-1].attributes['cl']="active"
        else:
            self.tab2=''

    def set_tabletitle(self,lst=[],type=0):
        if type==1:
            self.tabletitle=div(style="text-align: center;font-size: 18px; margin-top:20px; font-weight: bold;")
            for item in lst:
                self.tabletitle.addObj(item)  
        else:
            for i in lst:
                self.tabletitle.addObj(i)

    def set_tabletools(self,*lst,date=0):
        icons={'导出Excel':span(cl="icon icon-file-excel"),
        '导出PDF':span(cl="icon icon-file-pdf"),
        '打印':span(cl="glyphicon glyphicon-print")}
        if lst:
            self.tabletools=div(div(cl="btn-group",role="group",style="float: left;"),style="height:30px;padding:5px 0px;")
            for item in lst:
                if icons[item]:
                    self.tabletools.div.addObj(button(icons[item],item,type="button",cl="btn btn-default btn-xs"))
                else:
                    self.tabletools.div.addObj(button(item,type="button",cl="btn btn-default btn-xs"))
            if date:
                self.tabletools.addObj(span('日期：',datetime.datetime.now().strftime('%Y-%m-%d'),style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
        else:
            self.tabletools=''

    def set_form_window(self,name):
        self.form_window=div(div(h4(span(name,cl="title"),span(id="close",cl="glyphicon glyphicon-remove close-button")),cl="form-window-title"),cl="form-window",id="window",style="display: none;")

    def generate(self):
        for css in self.css:
            self.page.addCSS(css)
        self.head<<style(self.page_css,type='text/css')
        for js in self.js:
            self.page.addJS(js)
        #self.head<< script(self.page_js,type='text/javascript')
        self.body<<self.top
        self.body<<div(self.breadcrumb,self.tab1_left,self.tab1_right,self.nav_tree,self.main_frame,self.form_window)
        self.main_frame.addObj(self.tab2)
        self.main_frame.addObj(self.selection)
        self.main_frame.addObj(self.tabletitle)
        self.main_frame.addObj(self.tabletools)
        self.main_frame.addObj(self.table)
   
class table(Tag):
    tagname='table'
    def __init__(self, *arg, **kw):
        Tag.__init__(self, *arg, **kw)
        self<<thead(tr())
        self<<tbody()


    def add_col(self,col_name):
        self.thead.tr<<th(col_name)

    def add_cols(self,col_name_lst):
        for col_name in col_name_lst:
            self.add_col(col_name)

    def add_row(self,row):
        r=tr()
        for d in row:
            r<<td(d)
        self.tbody<<r

    def add_rows(self,rows):
        for row in rows:
            self.add_row(row)

    def set_col_attr(self,i,**attr):
        for row in self.tbody:
            row[i].attributes=attr

    def set_cell_attr(self,r,c,**attr):
        self.tbody[r][c].attributes=attr

    def read_excel(self,excel,**kw):
        self.excel=pd.read_excel(excel,**kw)
        self.excel=self.excel.fillna('')
        if isinstance(self.excel.columns,pd.MultiIndex):
            lines=zip(*self.excel.columns)
            for line in lines: 
                row=tr()
                for item in line:
                    row.addObj(th(item))
                self.thead.addObj(row)
        else:
            self.add_cols(self.excel.columns)
        self.add_rows(self.excel.values)

    def get_value(self,r,c):
        return self.tbody[r][c]

    def set_value(self,r,c,*val):
        for i in self.tbody[r][c]:
            self.tbody[r][c].pop()
        for i in val:
            self.tbody[r][c].append(i)

    def datetime_str_split_line(self,*cols):
        for col in cols:
            for r in range(len(self.tbody)):
                if isinstance(self.tbody[r][col][0],str):
                    self.tbody[r][col][0]=self.tbody[r][col][0].replace(' ','</br>')

    def datetime_str_to_date_str(self,*cols):
        for col in cols:
            for r in range(len(self.tbody)):
                if isinstance(self.tbody[r][col][0],str):
                    self.tbody[r][col][0]=self.tbody[r][col][0].split(" ")[0]

    def str_length_control(self,length,*cols):
        for col in cols:
            for r in range(len(self.tbody)):
                if isinstance(self.tbody[r][col][0],str):
                    val=self.tbody[r][col][0]
                    if (len(val.encode('utf-8'))+len(val))/2 > length-3:
                        while (len(val.encode('utf-8'))+len(val))/2 > length-3:
                            val=val[0:-2]
                        self.tbody[r][col][0]=val+'...'

    def merge_cells(self,row,col,rowspan=0,colspan=0):
        if rowspan>0 and colspan>0:
            tmp=self.tbody[row][col]
            for r in range(rowspan):
                for c in range(colspan):
                    self.tbody[row+r][col+c]=''
            self.tbody[row][col]=tmp
            self.tbody[row][col].set_attributes(colspan=colspan,rowspan=rowspan)
        elif rowspan>0:
            self.tbody[row][col].set_attributes(rowspan=rowspan)
            for r in range(1,rowspan):
                self.tbody[row+r][col]=''
        elif colspan>0:
            self.tbody[row][col].set_attributes(colspan=colspan)
            for c in range(1,colspan):
                self.tbody[row][col+c]=''
        else:
            pass

    def auto_fill_cell(self,tbody,r,c):
        if tbody[r][c]==['']:
            return self.auto_fill_cell(tbody,r-1,c)
        else:
            return tbody[r][c]

    def auto_fill(self,cols=[]):
        for c in cols:
            for r in range(len(self.tbody)):
                self.tbody[r][c]=self.auto_fill_cell(self.tbody,r,c)

    def to_int(self,cols=[]):
        for c in cols:
            for r in range(len(self.tbody)):
                if self.tbody[r][c][0].split('.')[-1]=='0':
                    self.tbody[r][c][0]=self.tbody[r][c][0].split('.')[0]
                elif self.tbody[r][c][0]=='-':
                    self.tbody[r][c]=td(style='background-color:#DDD;')

    def to_percentage(self,cols=[],color=''):
        for c in cols:
            for r in range(len(self.tbody)):
                if self.tbody[r][c][0] in ['1','1.0']:
                    self.tbody[r][c][0]='100.00%'
                    if color=='asc':
                        self.tbody[r][c].attributes['style']='background-color:#ff9d80'
                    elif color=='desc':  
                        pass
                elif self.tbody[r][c][0].split('.')[0]=='0':
                    res=self.tbody[r][c][0]+'000000'
                    self.tbody[r][c][0]=res[2:4]+'.'+res[4:6]+'%'
                    if color=='asc':
                        if int(res[2:4])<20:
                            self.tbody[r][c].attributes['style']=''
                        elif int(res[2:4])<=40:
                            self.tbody[r][c].attributes['style']='background-color:#FFF599'
                        elif int(res[2:4])>40:
                            self.tbody[r][c].attributes['style']='background-color:#ff9d80'
                            print(int(res[2:4]))
                    elif color=='desc':
                        if int(res[2:4])>=90:
                            pass
                        elif int(res[2:4])>=80:
                            self.tbody[r][c].attributes['style']='background-color:#fff599'
                        elif int(res[2:4])<80:
                            self.tbody[r][c].attributes['style']='background-color:#ff9d80'
                            print(int(res[2:4]))
                else:
                    self.tbody[r][c][0]=''

    def transform_a(self,r,c,**kw):
        self.tbody[r][c][0]=a(self.tbody[r][c][0],**kw)


class CapolHtml_ProjectPage(CapolHtml_TablePage):
    def __init__(self, *arg, **kw):
        CapolHtml_TablePage.__init__(self, *arg, **kw)
        self.prjtitle=''
        self.link_div=''
        self.main_frame=div(style="padding-left:20px;padding-right: 20px;")

    def generate(self):
        for css in self.css:
            self.page.addCSS(css)
        self.head<<style(self.page_css,type='text/css')
        for js in self.js:
            self.page.addJS(js)
        #self.head<< script(self.page_js,type='text/javascript')
        self.body<<self.top
        self.body<<div(self.breadcrumb,self.prjtitle,self.main_frame,self.link_div)
        self.main_frame.addObj(self.tab1_left)
        self.main_frame.addObj(self.selection)
        self.main_frame.addObj(self.tabletitle)
        self.main_frame.addObj(self.tabletools)
        self.main_frame.addObj(self.table)

    def set_selection(self,type=0,selection=[],checkbox=[],underline=True):
        if type==1:
            if underline:
                self.selection=div(style="width:100%;border-bottom: 1px solid #ccc;")
            else:
                self.selection=div(style="width:100%")
            self.selection.addObj(div(style="width:100%;float: left;"))
            for item in selection:
                self.selection_dict={
                '所属公司':self.select_company,
                '所属部门':self.select_dept,
                '项目所属公司':self.select_prjcomp,
                '项目所属部门':self.select_prjdept,
                '年份':self.select_year,
                '工程阶段':self.select_prjstage,
                '子项':self.select_subentry,
                '工程编号':self.select_prjno,
                '工程名称':self.select_prjname,
                '关键字':self.select_keywords}
                self.selection.div.addObj(self.selection_dict[item])
            for item in checkbox:
                self.checkbox_dict={'专业':self.major_checkbox,'工程阶段':self.prj_stage_checkbox,'工程状态':self.prj_status_checkbox,'人员状态':self.hr_status,'意见类型':self.opinion_type_checkbox}
                self.selection.div.addObj(self.checkbox_dict[item])
            self.selection.addObj(div(style='clear:both;'))
        else:
            self.selection.addObj(self.select_year)
            self.selection.addObj(self.select_company)
            self.selection.addObj(self.select_dept)
            self.selection.addObj(self.select_keywords)

    def generate_checkbox(self,objname,lst=[],checked=[]):
        if lst:
            obj=div(div(objname,"：&nbsp;&nbsp;",style='height:24px;float:left;font-weight:bold;'),cl="checkbox",style="margin-left: 24px; float: left;margin-top:17px;margin-bottom:10px;margin-right:10px;")
            for item in lst:
                if item in checked:
                    obj.addObj(label(input(type="checkbox",checked='true'),item+'&nbsp;'))
                else:
                    obj.addObj(label(input(type="checkbox"),item+'&nbsp;'))
            return obj
        else:
            return ''   
     

 
page_js='''
    $(document).ready(function() {
        $("#close").click(function() {
            $("#window").hide();
        });
    });
    $(document).ready(function() {
        $("#open").click(function() {
            $("#window").show();
        });
    });
    '''
meta='''<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">'''
icon='<link rel="icon" href="./static/favicon.ico">'


if __name__ == '__main__':
    t=table()

    t.read_excel('./static/质量管控表单.xlsx',sheet_name='项目设计人员校审情况一览表')
    #t.read_excel('./static/质量管控表单.xlsx',sheet_name='项目校审情况一览表')

    t.to_percentage([23,24])
