# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
from tablepage import *
import cx_Oracle

import xgt


app = Flask(__name__)

app.add_url_rule('/xgt1',view_func=xgt.xgt1)
app.add_url_rule('/xgt2',view_func=xgt.xgt2)
app.add_url_rule('/3dp1',view_func=xgt.ThreeDPrinting1)
app.add_url_rule('/3dp2',view_func=xgt.ThreeDPrinting2)
app.add_url_rule('/hp1',view_func=xgt.hp1)
app.add_url_rule('/hp2',view_func=xgt.hp2)

@app.route('/prjreview')
def prjreview():
    name='项目校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','#'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status'),('项目校审记录表','./prj_review_record')],active=1)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['专业','工程阶段'],selection=['项目所属公司','项目所属部门','工程编号','工程名称','关键字'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/质量管控表单.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    js=''''''
    h.head.addObj(script(js,type='text/javascript'))
    return h.page.render()

@app.route('/prj_review_record')
def prj_review_record():
    name='项目校审记录表'
    h=CapolHtml_ProjectPage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left(lst=[('工程概况','#'),('阶段文件','#'),('会议纪要','#'),('工程联系单','#'),('设计更改通知单','#'),('校审记录表','#'),('工程形象','#'),('项目邮箱','#'),('工程总结','#')],active=6,width='100%')
    h.set_tab1_right()
    h.set_nav_lst1()
    h.set_tab2()
    h.set_status_checkbox()
    h.set_stage_checkbox()
    h.set_major_checkbox()
    h.set_opinion_type_checkbox(lst=['全部','图纸深度'],checked=[])
    h.set_selection(type=1,checkbox=['专业','意见类型'],selection=['工程阶段','子项'])
    h.set_tabletitle([name],type=0)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    h.table.attributes['id']='prj_review_record_table'
    t.attributes=h.table.attributes
    t.read_excel('./static/质量管控表单.xlsx',sheet=name) 
    t.datetime_str_split_line(10,13,15)
    t.str_length_control(100,8)
    t.str_length_control(45,16)
    t.str_length_control(120,17)
    for i in [4,9]:
        t.set_col_attr(i=i,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=8,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for i in [12,14,16,17]:
        t.set_col_attr(i=i,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    js='''$(document).ready(function(){
        $('#prj_review_record_table').DataTable({ "scrollX":true,"scrollY":"600px","scrollCollapse": true,"paging":false,"searching": false,"info": false,"columns": [ 
            { "width": "30px"}, { "width": "50px"}, { "width": "50px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "60px"}, { "width": "60px"}, { "width": "240px"},{ "width": "80px"},{ "width": "80px"}, { "width": "70px"}, { "width": "150px"}, { "width": "80px"}, { "width": "150px"},  { "width": "80px"}, { "width": "200px"}, { "width": "300px"}
            ]});
    });'''
    h.head.addObj(script(js,type='text/javascript',cl='init'))
    return h.page.render()




if __name__ == '__main__':
    app.run(debug=True)