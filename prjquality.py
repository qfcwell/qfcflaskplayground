# coding:utf-8
import os
from tablepage import *

excel='./static/质量管控表单.xlsx'
excel2='./static/项目成本预结算.xlsx'

def prjreview():
    name='各项目校审一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('各项目校审一览表','./prjreview'),('项目人员校审一览表','./prj_design_review_status'),('人员项目校审一览表','./design_prj_review_status')],active=1)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=0)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.review_type=h.generate_checkbox('校审类别',lst=['全部','校对','审核','抽复查'],checked='all')
    h.set_selection(type=1,checkbox=['工程阶段','专业','校审类别'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=1)
    h.tabletools.addObj(h.percentage_color_desc(name='处理率、复核通过率：'))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name='项目校审情况一览表',header=[0,1])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:30px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:180px;'),
        th('所属公司',rowspan=2,style='width:60px;'),
        th('所属部门',rowspan=2,style='width:60px;'),
        th('质量管控得分',rowspan=2,style='width:90px;'),
        th('工程阶段',rowspan=2,style='width:60px;'),
        th('校审阶段',rowspan=2,style='width:60px;'),
        th('校对',colspan=4),
        th('审核',colspan=4),
        th('抽复查',colspan=4),
        th('校审意见总计',colspan=3)
        )
        ,tr(
        th('意见总数',style='width:60px;'), th('未处理',style='width:60px;'),th('处理中',style='width:60px;'),th('复核通过',style='width:60px;'),
        th('意见总数',style='width:60px;'), th('未处理',style='width:60px;'),th('处理中',style='width:60px;'),th('复核通过',style='width:60px;'),
        th('意见总数',style='width:60px;'), th('未处理',style='width:60px;'),th('处理中',style='width:60px;'),th('复核通过',style='width:60px;'),
        th('意见总数',style='width:60px;'),th('处理率',style='width:60px;'),th('复核通过率',style='width:72px;')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=2,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for r in range(2):
        for c in [1,2]:
            t.transform_a(r*4,c,href='./prj_review_record')
    t.to_int([0,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    t.to_percentage(cols=[21,22],color='desc')
    #t.auto_fill(range(5))
    for r in [0,4]:
        for c in [0,1,2,3,4,5,6,16,17,18,19,20,21,22,21]:
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
    h.prjtitle=div('GC160165 恒大江门悦珑湾二期',style='font-weight:bold;text-align:center;font-size:20px;height:36px;')
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','./prjreview'),('GC160165 恒大江门悦珑湾二期','')])
    h.set_tab1_left(lst=[('工程概况','#'),('阶段文件','#'),('会议纪要','#'),('工程联系单','#'),('设计更改通知单','#'),('校审记录表','./prj_review_record'),('工程形象','#'),('项目邮箱','#'),('工程总结','#'),('质量评价','./prj_value')],active=6,width='100%')
    h.set_tab1_right()
    h.set_nav_lst1()
    h.set_tab2()
    h.set_status_checkbox()
    h.set_stage_checkbox()
    h.set_major_checkbox()
    h.set_opinion_type_checkbox(lst=['全部','图纸深度','图面表达','品质优化','错漏碰缺','一般性规范','强条'],checked=[])
    h.set_selection(type=1,checkbox=['专业','意见类型'],selection=['工程阶段','子项'])
    h.set_tabletitle([name],type=0)
    h.set_tabletools('导出Excel',date=1)
    t=table()
    h.table.attributes['id']='prj_review_record_table'
    t.attributes=h.table.attributes
    t.attributes['cl']="table table-bordered table-bordered1"
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

def prj_value():
    name='质量评价'
    h=CapolHtml_ProjectPage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.prjtitle=div('GC160165 恒大江门悦珑湾二期',style='font-weight:bold;text-align:center;font-size:20px;height:36px;')
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','./prjreview'),('GC160165 恒大江门悦珑湾二期','')])
    h.set_tab1_left(lst=[('工程概况','#'),('阶段文件','#'),('会议纪要','#'),('工程联系单','#'),('设计更改通知单','#'),('校审记录表','./prj_review_record'),('工程形象','#'),('项目邮箱','#'),('工程总结','#'),('质量评价','./prj_value')],active=10,width='100%')
    h.set_tab1_right()
    h.set_nav_lst1()
    h.set_tab2()
    h.set_status_checkbox()
    h.set_stage_checkbox()
    h.set_major_checkbox()
    h.set_opinion_type_checkbox(lst=['全部','图纸深度','图面表达','品质优化','错漏碰缺','一般性规范','强条'],checked=[])
    h.selection=''
    h.set_tabletitle([name+'（本界面待完善）'],type=0)
    h.generate()
    h.page.body.addObj('''<ul align="center" style="margin-left: 100px;list-style: none;">
            <li style="border:1px solid #ccc;width:600px;height:100px;padding:10px;margin:10px;">
                <div class="doc_img_div"></div>
                <div class="doc_title_div" style="font-weight:bold;">流程执行：</div>
                <div class="doc_title_div">30%</div>             
            </li>
            <li style="border:1px solid #ccc;width:600px;height:100px;padding:10px;margin:10px;">
                <div class="doc_img_div"></div>
                <div class="doc_title_div" style="font-weight:bold;">质量管控得分：</div>
                <div class="doc_title_div">50%</div>             
            </li>
            <li style="border:1px solid #ccc;width:600px;height:100px;padding:10px;margin:10px;">
                <div class="doc_img_div"></div>
                <div class="doc_title_div" style="font-weight:bold;">工时系数：</div>
                <div class="doc_title_div">10%</div>             
            </li>
            <li style="border:1px solid #ccc;width:600px;height:100px;padding:10px;margin:10px;">
                <div class="doc_img_div"></div>
                <div class="doc_title_div" style="font-weight:bold;">项目预算：</div>
                <div class="doc_title_div">10%</div>             
            </li>
            <li style="border:1px solid #ccc;width:600px;height:100px;padding:10px;margin:10px;">
                <div class="doc_img_div"></div>
                <div class="doc_title_div" style="font-weight:bold;">投诉和表扬：</div>
                <div class="doc_title_div">加分和减分</div>             
            </li>
            
        </ul>''')

    
    return h.page.render()
    

def prj_design_review_status():
    name='项目人员校审一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('各项目校审一览表','./prjreview'),('项目人员校审一览表','./prj_design_review_status'),('人员项目校审一览表','./design_prj_review_status')],active=2)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=0)
    h.set_tab2(lst=[('设计人员','./prj_design_review_status'),('校审人员','./prj_review_review_status')],active=1)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','专业','校审类别'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name,'（设计人员）'],type=1)
    h.set_tabletools('导出Excel',date=1)
    h.tabletools.addObj(h.percentage_color_desc(name='处理率、复核通过率：'))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name='项目设计人员校审情况一览表',header=[0,1])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:30px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:180px;'),
        th('所属公司',rowspan=2,style='width:60px;'),
        th('所属部门',rowspan=2,style='width:60px;'),
        th('工程阶段',rowspan=2,style='width:60px;'),
        th('姓名',rowspan=2,style='width:60px;'),
        th('专业',rowspan=2,style='width:60px;'),
        th('岗位',rowspan=2,style='width:60px;'),
        th('校审阶段',rowspan=2,style='width:60px;'),
        th('校对',colspan=4),
        th('审核',colspan=4),
        th('校审意见总计',colspan=3)
        ),tr(
        th('意见总数'), th('未处理'),th('处理中'),th('复核通过'),
        th('意见总数'), th('未处理'),th('处理中'),th('复核通过'),
        th('意见总数'),th('处理率'),th('复核通过率')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=2,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for r in range(2):
        for c in [1,2]:
            t.transform_a(r*4,c,href='./prj_review_record')
    t.to_int([0,10,11,12,13,14,15,16,17,18])
    t.to_percentage(cols=[19,20],color='desc')
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=28,colspan=0)
    for r in range(7):
        for c in [6,7,8,18,19,20]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def design_prj_review_status():
    name='人员项目校审一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('各项目校审一览表','./prjreview'),('项目人员校审一览表','./prj_design_review_status'),('人员项目校审一览表','./')],active=3)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=0)
    h.set_tab2(lst=[('设计人员','./design_prj_review_status'),('校审人员','./review_prj_review_status')],active=1)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','校审类别'],selection=['年份','所属公司','一级部门','二级部门'])
    h.set_tabletitle([name,'（设计人员）'],type=1)
    h.set_tabletools('导出Excel',date=1)
    h.tabletools.addObj(h.percentage_color_desc(name='处理率、复核通过率：'))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name='设计人员项目校审情况一览表',header=[0,1])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:30px;'),
        th('工号',rowspan=2,style='width:60px;'),
        th('姓名',rowspan=2,style='width:60px;'),
        th('所属公司',rowspan=2,style='width:60px;'),
        th('一级部门',rowspan=2,style='width:60px;'),
        th('二级部门',rowspan=2,style='width:60px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:180px;'),
        th('工程阶段',rowspan=2,style='width:60px;'),
        th('专业',rowspan=2,style='width:60px;'),
        th('岗位',rowspan=2,style='width:60px;'),
        th('校审阶段',rowspan=2,style='width:60px;'),
        th('校对',colspan=4),
        th('审核',colspan=4),
        th('校审意见总计',colspan=3)
        ),tr(
        th('意见总数',style='width:60px;'), th('未处理',style='width:60px;'),th('处理中',style='width:60px;'),th('复核通过',style='width:60px;'),
        th('意见总数',style='width:60px;'), th('未处理',style='width:60px;'),th('处理中',style='width:60px;'),th('复核通过',style='width:60px;'),
        th('意见总数',style='width:60px;'),th('处理率',style='width:60px;'),th('复核通过率',style='width:72px;')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=6,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=7,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for r in range(2):
        for c in [6,7]:
            t.transform_a(r*4,c,href='./prj_review_record')
    t.to_int([0,12,13,14,15,16,17,18,19,20])
    t.to_percentage(cols=[21,22],color='desc')
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

def prj_review_review_status():
    name='项目人员校审一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')]) 
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('各项目校审一览表','./prjreview'),('项目人员校审一览表','./prj_design_review_status'),('人员项目校审一览表','./design_prj_review_status')],active=2)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=0)
    h.set_tab2(lst=[('设计人员','./prj_design_review_status'),('校审人员','./prj_review_review_status')],active=2)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','专业','校审类别'],selection=['年份','项目所属公司','项目所属部门','工程编号','工程名称'])
    h.set_tabletitle([name,'（校审人员）'],type=1)
    h.set_tabletools('导出Excel',date=1)
    h.tabletools.addObj(h.percentage_color_asc(name='待复核百分比：'))
    h.tabletools.addObj(h.percentage_color_desc(name='及时校对率、及时审核率：'))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name='项目校审人员校审情况一览表',header=[0,1])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:30px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:180px;'),
        th('所属公司',rowspan=2,style='width:60px;'),
        th('所属部门',rowspan=2,style='width:60px;'),
        th('工程阶段',rowspan=2,style='width:60px;'),
        th('姓名',rowspan=2,style='width:60px;'),
        th('专业',rowspan=2,style='width:60px;'),
        th('岗位',rowspan=2,style='width:60px;'),
        th('校审阶段',rowspan=2,style='width:60px;'),
        th('校对',colspan=5),
        th('审核',colspan=5),
        th('校审意见总计',colspan=3)
        ),tr(
        th('意见总数',style='width:60px;'),th('待设计人员</br>处理',style='width:72px;'), th('待复核',style='width:60px;'),th('复核通过',style='width:60px;'),th('及时校对率',style='width:72px;'),
        th('意见总数',style='width:60px;'),th('待设计人员</br>处理',style='width:72px;'), th('待复核',style='width:60px;'),th('复核通过',style='width:60px;'),th('及时审核率',style='width:72px;'),
        th('意见总数',style='width:60px;'),th('待复核</br>百分比',style='width:60px;')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=2,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for r in range(2):
        for c in [1,2]:
            t.transform_a(r*4,c,href='./prj_review_record')
    t.to_int([0,10,11,12,13,15,16,17,18,20])
    t.to_percentage(cols=[21],color='asc')
    t.to_percentage(cols=[14,19],color='desc')
    #t.auto_fill(range(5))
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=8,colspan=0)
    for r in range(2):
        for c in [6,7,8,20,21]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def review_prj_review_status():
    name='人员项目校审一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('各项目校审一览表','./prjreview'),('项目人员校审一览表','./prj_design_review_status'),('人员项目校审一览表','./design_prj_review_status')],active=3)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=0)
    h.set_tab2(lst=[('设计人员','./design_prj_review_status'),('校审人员','./review_prj_review_status')],active=2)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程阶段','校审类别'],selection=['年份','所属公司','一级部门','二级部门'])
    h.set_tabletitle([name,'（校审人员）'],type=1)
    h.set_tabletools('导出Excel',date=1)
    h.tabletools.addObj(h.percentage_color_asc(name='待复核百分比：'))
    h.tabletools.addObj(h.percentage_color_desc(name='及时校对率、及时审核率：'))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjreview'
    t.read_excel(excel,sheet_name='校审人员项目校审情况一览表',header=[0,1])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:30px;'),
        th('工号',rowspan=2,style='width:60px;'),
        th('姓名',rowspan=2,style='width:60px;'),
        th('所属公司',rowspan=2,style='width:60px;'),
        th('一级部门',rowspan=2,style='width:60px;'),
        th('二级部门',rowspan=2,style='width:60px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:180px;'),
        th('工程阶段',rowspan=2,style='width:60px;'),
        th('专业',rowspan=2,style='width:60px;'),
        th('岗位',rowspan=2,style='width:60px;'),
        th('校审阶段',rowspan=2,style='width:60px;'),
        th('校对',colspan=5),
        th('审核',colspan=5),
        th('校审意见总计',colspan=3)
        ),tr(
        th('意见总数',style='width:60px;'),th('待设计人员</br>处理',style='width:72px;'), th('待复核',style='width:60px;'),th('复核通过',style='width:60px;'),th('及时校对率',style='width:72px;'),
        th('意见总数',style='width:60px;'),th('待设计人员</br>处理',style='width:72px;'), th('待复核',style='width:60px;'),th('复核通过',style='width:60px;'),th('及时审核率',style='width:72px;'),
        th('意见总数',style='width:60px;'),th('待复核</br>百分比',style='width:60px;')
        ),style='border-bottom:2px solid #ccc;')
    t.set_col_attr(i=6,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=7,style='text-align:left;color:#0068B7;text-decoration: underline;')
    for r in range(2):
        for c in [6,7]:
            t.transform_a(r*4,c,href='./prj_review_record')
    t.to_int([0,12,13,14,15,17,18,19,20])
    t.to_percentage(cols=[23],color='asc')
    t.to_percentage(cols=[16,21],color='desc')
    for r in range(1):
        for c in [0,1,2,3,4,5]:
            t.merge_cells(row=r,col=c,rowspan=8,colspan=0)
    for r in range(2):
        for c in [6,7,8,9,10,22,23]:
            t.merge_cells(row=r*4,col=c,rowspan=4,colspan=0)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()

def prjcost():
    name='项目成本预结算一览表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status')],active=0)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=1)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=['工程状态'],selection=['年份','所属公司','所属部门'])
    h.set_tabletitle(['深圳公司XX部门 ',name],type=1)
    h.set_tabletools('导出Excel',date=0)
    h.tabletools.addObj(span('单位：元',style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    h.tabletools.addObj(span('日期：',datetime.datetime.now().strftime('%Y-%m-%d'),style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjcost'
    #t.read_excel(excel2,sheet_name=name,header=[4,5])
    t[0]=thead(tr( 
        th('序号',rowspan=2),
        th('工程编号',rowspan=2),
        th('工程名称',rowspan=2),
        th('所属公司',rowspan=2),
        th('所属部门',rowspan=2),
        th('项目负责人',rowspan=2),
        th('阶段组合',rowspan=2),
        th('工程状态',rowspan=2),
        th('工程额',rowspan=2),
        th('标准工程额',rowspan=2),
        th('产值奖金',colspan=4),
        th('项目直接成本',colspan=5),
        th('外部分包合同额',colspan=4),
        th('合计',colspan=7),
        th('备注',rowspan=2)
        ),tr(
        th('预算'), th('结算'),th('剩余'),th('结算/预算'),
        th('标准预算'),th('调整预算'), th('结算'),th('剩余'),th('结算/调整预算'),
        th('预算'), th('结算'),th('剩余'),th('结算/预算'),
        th('预算'), th('结算'),th('剩余'),th('结算/预算'),th('预算占工程额比例'),th('结算占工程额比例'),th('剩余占工程额比例')
        ),style='border-bottom:2px solid #ccc;')
    lst=[]
    for i in range(31):
        lst.append('')
    for i in range(20):
        t.add_row(lst)
    t.tbody[0][20].append('结算即实际</br>签订合同额')
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    js='''$(document).ready(function(){
        $('#prjcost').DataTable({ "scrollX":true,"scrollY":false,"scrollCollapse": true,"paging":false,"searching": false,"info": false,"columns": [ 
            { "width": "30px"}, { "width": "80px"}, { "width": "240px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"},{ "width": "80px"},
            { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"},
            { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"},
            { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, 
            { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"}, { "width": "80px"},
            { "width": "80px"}
            ]});
    });'''
    h.head.addObj(script(js,type='text/javascript'))
    h.body.attributes['style']=''
    return h.page.render()

def prj_bonus():
    name='项目产值奖金预结算表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status')],active=0)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=2)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=[],selection=['年份','所属公司','所属部门','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=0)
    h.tabletools.addObj(span('单位：元',style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    h.tabletools.addObj(span('日期：',datetime.datetime.now().strftime('%Y-%m-%d'),style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjcost'
    #t.read_excel(excel2,sheet_name=name,header=[4,5])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:60px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:240px;'),
        th('所属公司',rowspan=2,style='width:80px;'),
        th('所属部门',rowspan=2,style='width:80px;'),
        th('项目负责人',rowspan=2,style='width:80px;'),
        th('阶段组合',rowspan=2,style='width:80px;'),
        th('工程状态',rowspan=2,style='width:80px;'),
        th('工程额',rowspan=2,style='width:80px;'),
        th('标准工程额',rowspan=2,style='width:80px;'),
        th('产值奖金',colspan=4)
        ),tr(
        th('预算',style='width:80px;'), th('结算',style='width:80px;'),th('剩余',style='width:80px;'),th('结算/预算',style='width:80px;')
        ),style='border-bottom:2px solid #ccc;')
    lst=[]
    for i in range(14):
        lst.append('')
    for i in range(20):
        t.add_row(lst)
    h.table=t
    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    js=''''''
    h.head.addObj(script(js,type='text/javascript'))
    h.body.attributes['style']=''
    return h.page.render()

def prj_direct_cost():
    name='项目直接成本预结算表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status')],active=0)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=3)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=[],selection=['年份','所属公司','所属部门','br','方案负责人','项目负责人','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=0)
    h.tabletools.addObj(span('单位：元',style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    h.tabletools.addObj(span('日期：',datetime.datetime.now().strftime('%Y-%m-%d'),style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjcost'
    #t.read_excel(excel2,sheet_name=name,header=[4,5])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:60px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:240px;'),
        th('所属公司',rowspan=2,style='width:80px;'),
        th('所属部门',rowspan=2,style='width:80px;'),
        th('方案负责人',rowspan=2,style='width:80px;'),
        th('项目负责人',rowspan=2,style='width:80px;'),
        th('阶段组合',rowspan=2,style='width:80px;'),
        th('工程状态',rowspan=2,style='width:80px;'),
        th('工程额',rowspan=2,style='width:80px;'),
        th('标准工程额',rowspan=2,style='width:80px;'),
        th('项目直接成本',colspan=5)
        ),tr(
        th('标准预算',style='width:80px;'),th('调整预算',style='width:80px;'), th('结算',style='width:80px;'),th('剩余',style='width:80px;'),th('结算/预算',style='width:80px;')
        ),style='border-bottom:2px solid #ccc;')
    lst=[]
    for i in range(16):
        lst.append('')
    for i in range(20):
        t.add_row(lst)
    h.table=t

    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    js=''''''
    h.head.addObj(script(js,type='text/javascript'))
    h.body.attributes['style']=''
    return h.page.render()

def prj_outsourcing_cost():
    name='项目外部分包预结算表'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js","./static/js/jquery.table.rowspan.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('工程管理平台','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1,width='100%')
    h.set_tab1_right([],active=0)
    h.set_nav_lst1([('工程管理','#'),('运营管理5张表','#'),('质量管控','#'),('项目成本预结算','#')])
    h.set_nav_lst2(index=1,lst=[('工程台账','http://pm.capol.cn/projectManage/index.jsp'),('项目关键节点控制一览表','#')])
    h.set_nav_lst2(index=2,lst=[('人员信息表','#'),('人员架构表','#'),('各设计阶段项目一览表','#'),('人员项目表','#'),('项目人员表','#')])
    h.set_nav_lst2(index=3,lst=[('项目校审情况一览表','./prjreview'),('项目设计人员校审情况一览表','./prj_design_review_status'),('设计人员项目校审情况一览表','./design_prj_review_status'),('项目校审人员校审情况一览表','./prj_review_review_status'),('校审人员项目校审情况一览表','./review_prj_review_status')],active=0)
    h.set_nav_lst2(index=4,lst=[('项目成本预结算一览表','./prjcost'),('项目产值奖金预结算表','./prj_bonus'),('项目直接成本预结算表','./prj_direct_cost'),('项目外部分包预结算表','./prj_outsourcing_cost')],active=4)
    h.set_tab2(lst=[],active=6)
    h.set_status_checkbox()
    h.set_stage_checkbox(['全部','初步设计','施工图'])
    h.set_major_checkbox()
    h.set_selection(type=1,checkbox=[],selection=['年份','所属公司','所属部门','br','方案负责人','项目负责人','工程编号','工程名称'])
    h.set_tabletitle([name],type=1)
    h.set_tabletools('导出Excel',date=0)
    h.tabletools.addObj(span('单位：元',style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    h.tabletools.addObj(span('日期：',datetime.datetime.now().strftime('%Y-%m-%d'),style="position: relative;float: right;font-size: 12px;font-weight: normal;margin: 5px 5px 0px 5px;"))
    t=table()
    t.attributes['cl']="table table-bordered table-bordered1"
    t.attributes['id']='prjcost'
    #t.read_excel(excel2,sheet_name=name,header=[4,5])
    t[0]=thead(tr( 
        th('序号',rowspan=2,style='width:60px;'),
        th('工程编号',rowspan=2,style='width:80px;'),
        th('工程名称',rowspan=2,style='width:240px;'),
        th('所属公司',rowspan=2,style='width:80px;'),
        th('所属部门',rowspan=2,style='width:80px;'),
        th('方案负责人',rowspan=2,style='width:80px;'),
        th('项目负责人',rowspan=2,style='width:80px;'),
        th('阶段组合',rowspan=2,style='width:80px;'),
        th('工程状态',rowspan=2,style='width:80px;'),
        th('工程额',rowspan=2,style='width:80px;'),
        th('标准工程额',rowspan=2,style='width:80px;'),
        th('外部分包合同额',colspan=4)
        ),tr(
        th('预算',style='width:80px;'), th('结算',style='width:80px;'),th('剩余',style='width:80px;'),th('结算/预算',style='width:80px;')
        ),style='border-bottom:2px solid #ccc;')
    lst=[]
    for i in range(15):
        lst.append('')
    for i in range(20):
        t.add_row(lst)
    t.tbody[0][12].append('结算即实际</br>签订合同额')
    h.table=t

    h.set_form_window(name)
    form=''''''
    h.form_window.addObj(form)
    h.generate()
    js=''''''
    h.head.addObj(script(js,type='text/javascript'))
    h.body.attributes['style']=''
    return h.page.render()