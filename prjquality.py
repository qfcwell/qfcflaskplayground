# coding:utf-8
import os
from tablepage import *

excel='./static/质量管控表单.xlsx'

def prjreview():
    name='项目校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
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
    h.set_selection(type=1,checkbox=['工程阶段','专业'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes['cl']="table table-bordered table-bordered2"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name=name,header=[0,1,2])
    t[0]=thead(tr( 
        th('序号',rowspan=3),
        th('工程编号',rowspan=3),
        th('工程名称',rowspan=3),
        th('所属公司',rowspan=3),
        th('所属部门',rowspan=3),
        th('工程阶段',rowspan=3),
        th('校审阶段',rowspan=3),
        th('校审意见数量',colspan=12),
        th('项目总体情况',colspan=3,rowspan=2)
        ),tr(
        th('自校',colspan=4),
        th('校对',colspan=4),
        th('审核',colspan=4)
        ),tr(
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('校审意见总数'),th('处理率'),th('完成率')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    t.to_int(range(20))
    t.to_percentage(cols=[20,21],color='desc')
    #t.auto_fill(range(5))
    for r in [0,4]:
        for c in [0,1,2,3,4,5,19,20,21]:
            t.merge_cells(row=r,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    '''js=function initLoad() {
                $("#prjreview").rowspan(0); 
                $("#prjreview").rowspan(1);
                $("#prjreview").rowspan(2);
                $("#prjreview").rowspan(3);
                $("#prjreview").rowspan(4);
        }
        $(document).ready(function () {
            initLoad();
        });'''
    #h.head.addObj(script(js,type='text/javascript'))
    return h.page.render()

def prj_review_record():
    name='项目校审记录表'
    h=CapolHtml_ProjectPage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.prjtitle=div('GC160165 恒大江门悦珑湾二期',style='font-weight:bold;text-align:center;font-size:20px;')
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','./prjreview'),('GC160165 恒大江门悦珑湾二期','')])
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
    t.read_excel(excel,sheet_name=name) 
    t.datetime_str_split_line(10,13,15)
    t.str_length_control(100,8)
    t.str_length_control(45,16)
    t.str_length_control(120,17)
    for i in [4,9]:
        t.set_col_attr(i=i,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=8,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for i in [12,14,16,17]:
        t.set_col_attr(i=i,style='text-align:left;')
    t.to_int([0])
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


def prj_design_review_status():
    name='项目设计人员校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','#'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status'),('项目校审记录表','./prj_review_record')],active=2)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','专业'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes['cl']="table table-bordered table-bordered2"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name=name,header=[0,1,2])
    t[0]=thead(tr( 
        th('序号',rowspan=3),
        th('工程编号',rowspan=3),
        th('工程名称',rowspan=3),
        th('所属公司',rowspan=3),
        th('所属部门',rowspan=3),
        th('工程阶段',rowspan=3),
        th('姓名',rowspan=3),
        th('专业',rowspan=3),
        th('角色',rowspan=3),
        th('校审阶段',rowspan=3),
        th('校审意见数量',colspan=12),
        th('项目总体情况',colspan=3,rowspan=2)
        ),tr(
        th('自校',colspan=4),
        th('校对',colspan=4),
        th('审核',colspan=4)
        ),tr(
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('校审意见总数'),th('未处理百分比'),th('处理中百分比')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    t.to_int(range(23))
    t.to_percentage(cols=[23,24])
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=28,colspan=0)
    for r in range(7):
        for c in [6,7,8,22,23,24]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def design_prj_review_status():
    name='设计人员项目校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','#'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status'),('项目校审记录表','./prj_review_record')],active=3)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段'],selection=['年份','所属公司','一级部门','二级部门'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes['cl']="table table-bordered table-bordered2"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name=name,header=[0,1,2])
    t[0]=thead(tr( 
        th('序号',rowspan=3),
        th('工号',rowspan=3),
        th('姓名',rowspan=3),
        th('所属公司',rowspan=3),
        th('一级部门',rowspan=3),
        th('二级部门',rowspan=3),
        th('工程编号',rowspan=3),
        th('工程名称',rowspan=3),
        th('工程阶段',rowspan=3),
        th('专业',rowspan=3),
        th('角色',rowspan=3),
        th('校审阶段',rowspan=3),
        th('校审意见数量',colspan=12),
        th('项目总体情况',colspan=3,rowspan=2)
        ),tr(
        th('自校',colspan=4),
        th('校对',colspan=4),
        th('审核',colspan=4)
        ),tr(
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('待处理'), th('处理中'),th('已完成'),th('总数'),
        th('校审意见总数'),th('未处理百分比'),th('处理中百分比')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    t.to_int(range(25))
    t.to_percentage(cols=[25,26])
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=8,colspan=0)
    for r in range(2):
        for c in [6,7,8,9,10,24,25,26]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def prj_review_review_status():
    name='项目校审人员校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','#'),('项目关键节点控制一览表','#')]) 
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status'),('项目校审记录表','./prj_review_record')],active=4)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','专业'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes['cl']="table table-bordered table-bordered2"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name=name,header=[0,1,2])
    t[0]=thead(tr( 
        th('序号',rowspan=3),
        th('工程编号',rowspan=3),
        th('工程名称',rowspan=3),
        th('所属公司',rowspan=3),
        th('所属部门',rowspan=3),
        th('工程阶段',rowspan=3),
        th('姓名',rowspan=3),
        th('专业',rowspan=3),
        th('角色',rowspan=3),
        th('校审阶段',rowspan=3),
        th('校审意见数量',colspan=8),
        th('项目总体情况',colspan=3,rowspan=2)
        ),tr(
        th('校对',colspan=4),
        th('审核',colspan=4)
        ),tr(
        th('待设计人员处理'), th('待复核'),th('已完成'),th('总数'),
        th('待设计人员处理'), th('待复核'),th('已完成'),th('总数'),
        th('意见总数量'),th('待设计人员处理百分比'),th('待复核百分比')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    t.to_int(range(19))
    t.to_percentage(cols=[19,20])
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=8,colspan=0)
    for r in range(2):
        for c in [6,7,8,18,19,20]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def review_prj_review_status():
    name='校审人员项目校审情况一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','#'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status'),('项目校审记录表','./prj_review_record')],active=5)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段'],selection=['年份','所属公司','一级部门','二级部门'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    t.attributes['cl']="table table-bordered table-bordered2"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name=name,header=[0,1,2])
    t[0]=thead(tr( 
        th('序号',rowspan=3),
        th('工号',rowspan=3),
        th('姓名',rowspan=3),
        th('所属公司',rowspan=3),
        th('一级部门',rowspan=3),
        th('二级部门',rowspan=3),
        th('工程编号',rowspan=3),
        th('工程名称',rowspan=3),
        th('工程阶段',rowspan=3),
        th('专业',rowspan=3),
        th('角色',rowspan=3),
        th('校审阶段',rowspan=3),
        th('校审意见数量',colspan=8),
        th('项目总体情况',colspan=3,rowspan=2)
        ),tr(
        th('校对',colspan=4),
        th('审核',colspan=4)
        ),tr(
        th('待设计人员处理'), th('待复核'),th('已完成'),th('总数'),
        th('待设计人员处理'), th('待复核'),th('已完成'),th('总数'),
        th('意见总数量'),th('待设计人员处理百分比'),th('待复核百分比')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    t.to_int(range(21))
    t.to_percentage(cols=[21,22])
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=8,colspan=0)
    for r in range(2):
        for c in [6,7,8,9,10,20,21,22]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

