# -*- coding:utf-8 -*-
from pyh import *
import pandas as pd
import datetime

class CapolHtml_TablePage():
    def __init__(self):
        self.page=PyH('CAPOL_WEB_UI')
        self.head=self.page.head
        self.body=self.page.body
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
        self.select_year=div(span('年份'),select(option('不限',value=''),option('2018',value=''),option('2017',value=''),option('2016',value=''),option('2015及以前',value=''),id="filter-module",cl="combobox",style="width:100px;"),cl="select-item",style="margin-right:40px;")
        self.select_company=div(span('所属公司'),self.comp_selection,cl="select-item")
        self.select_dept=div(span('所属部门'),self.dept_selection,cl="select-item",style="padding-right: 40px;")
        self.select_keywords=div(span('关键字',cl="float",style='margin-top:8px;'),div('<input class="form-control input-sm" type="text" placeholder="名称、内容、负责人……" style="width:200px;border-right:0px;"><span class="input-group-search-btn"> 搜索</span>',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;margin-left:100px;")
        self.select_prjno=div(span('工程编号',cl="float",style='margin-top:8px;'),div('<input class="form-control select" type="text" style="width:80px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px; ")
        self.select_prjname=div(span('工程名称',cl="float",style='margin-top:8px;'),div('<input class="form-control select" type="text" style="width:200px;height: 29px;border-radius: 4px;">',cl="input-group"),cl="select-item",id="so",style="margin-right: 10px;")
        self.tabletitle=div(cl="table-title clearFix")
        self.tabletools=''
        self.table=table(cl="table table-bordered")
        self.form_window=''
        self.select_prjcomp=div(span('项目所属公司'),self.comp_selection,cl="select-item")
        self.select_prjdept=div(span('项目所属部门'),self.dept_selection,cl="select-item")
        self.select_prjstage=div(span('工程阶段'),self.stage_selection,cl="select-item")
        self.select_subentry=div(span('子项'),self.no_selection,cl="select-item")
        self.prj_status_checkbox=''
        self.prj_stage_checkbox=''
        self.major_checkbox=''
        self.opinion_type_checkbox=''
        self.hr_status=self.generate_checkbox('人员状态',lst=['全部','在职','离职'],checked=[1])

    def generate_checkbox(self,objname,lst=[],checked=[]):
        if lst:
            obj=div(div(objname,"：&nbsp;&nbsp;",style='width:80px;height:24px;float:left;'),cl="checkbox",style="margin-left: 5px;width: 49%; float: left;margin-top:10px;margin-bottom:10px;")
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
            checked=[1,2,3,4,5,6,7]
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
        self.thead=thead()
        self.tbody=tbody()
        self<<self.thead
        self<<self.tbody

    def add_col(self,col_name):
        self.thead<<th(col_name)

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

    def read_excel(self,excel,sheet=0):
        excel=pd.read_excel(excel,sheet_name=sheet)
        excel=excel.fillna('')
        self.add_cols(excel.columns)
        self.add_rows(excel.values)

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

    def str_length_control(self,length,*cols):
        for col in cols:
            for r in range(len(self.tbody)):
                if isinstance(self.tbody[r][col][0],str):
                    val=self.tbody[r][col][0]
                    if (len(val.encode('utf-8'))+len(val))/2 > length-3:
                        while (len(val.encode('utf-8'))+len(val))/2 > length-3:
                            val=val[0:-2]
                        self.tbody[r][col][0]=val+'...'


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
            obj=div(div(objname,"：&nbsp;&nbsp;",style='height:24px;float:left;'),cl="checkbox",style="margin-left: 24px; float: left;margin-top:17px;margin-bottom:10px;margin-right:10px;")
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
    });'''
meta='''<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">'''
icon='<link rel="icon" href="./static/favicon.ico">'