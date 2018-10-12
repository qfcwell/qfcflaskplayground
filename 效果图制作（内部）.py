# -*- coding:utf-8 -*-

from tablepage import *

def main():
    print("Content-type:text/html;charset=gb2312")
    print("")
    print('<!DOCTYPE html>')
    h=CapolHtml_TablePage()
    h.head.addObj('''<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="./static/favicon.ico">''')
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js='''$(document).ready(function() {
        $('#example1').DataTable({ "scrollY": "500px", "paging": true, "searching": false, "info": false });
    });
    $(document).ready(function() {
        $('#example2').DataTable({ "scrollY": "500px", "scrollCollapse": true, "paging": false, "searching": false, "info": false });
    });
    </script>
    <script type="text/javascript">
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
    h.page_css='''div.form-window {
        top: 50px;
    }

    form.table table.gdate {
        table-layout: fixed;
    }

    form.table table.gdate tr td {
        height: 20px;
        padding: 0px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        text-align: left;
        border-bottom-color: #777;
        border-top-color: #777;
    }

    form.table table.gdate tr td.gmonth {
        height: 24px;
        padding: 0px;
        background-color: #EEE;
    }

    form.table table.gdate tr td.gday {
        min-width: 16px;
        height: 24px;
        padding: 0px;
        background-color: #EEE;
    }

    form.table table.gdate tr td div.finished {
        background-color: #DDD;
    }

    form.table table.gdate tr td div.inreview {
        background-color: #ffebcc;
        height: 12px;
        border: 1px solid #FF9800;
    }

    form.table table.gdate tr td div.accepted {
        background-color: #cfe8fc;
        height: 12px;
        border: 1px solid #2196F3;
    }

    form.table table.gdate tr.current {
        background-color: #ffe5e5;
    }

    form.table table.gdate tr td.today {
        background-color: #777;
        color: #FFF;
    }

    form.table tr.sm td {
        height: 36px;
    }'''

    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','#'),('效果图制作（外包）','./效果图制作（外包）.py'),('3D打印（工程）','#'),('航拍（工程）','#'),('3D打印（部门）','#'),('航拍（部门）','#')],active=1)
    h.set_selection()
    h.set_tabletitle(['效果图制作申请一览表（内部）',
        a('查看预约情况',cl="under-line",style="font-weight: normal;font-size: 12px;"),
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('D:\\1.xlsx',sheet='Sheet1')
    '''
    cols=['序号','申请编号','工程编号','工程名称','所属公司','所属部门','预计开始时间','预计结束时间','实际开始时间',
    '实际结束时间','预计张数','预计费用','实际张数','实际费用','申请人','项目负责人','效果图负责人','执行状态','操作']
    t.add_cols(cols)
    rows=[('1','SQ-XGT1-170265','GC170019','塘朗山F地块','深圳公司','国际部','2017-12-21','2017-12-27','','','5',' 5000','','','吴庆贤','孔辉','','待接受','<a class="under-line">接受</a> <a class="under-line">拒绝</a>'),
    ('1','SQ-XGT1-170264','GC170248','金樾美泰天玺','深圳公司','都市部','2017-12-17','2017-12-27','','','6',' 6600','','','胡睿','胡睿','李韵','已接受','<a class="under-line">完成</a> <a class="under-line">取消</a>')]
    t.add_rows(rows)'''
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.generate()
    #print(h.page.render())



if __name__ == '__main__':
    main()
