# coding:utf-8
import os
from tablepage import *

def xgt1():
    name='效果图制作（内部）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["https://code.jquery.com/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=1)
    h.set_selection()
    h.set_tabletitle(['效果图制作申请一览表（内部）',
        a('查看预约情况',cl="under-line",style="font-weight: normal;font-size: 12px;"),
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">效果图制作申请单（内部）</th>
                            </tr>
                            <tr class="sm">
                                <td class="bold" style="width:12%">工程编号</td>
                                <td style="width:12%">
                                    <input class="form-control select" type="text" id="prjno" value="GC180066">
                                </td>
                                <td class="bold" style="width:12%">工程名称</td>
                                <td style="width:64%" colspan="5">
                                    <input class="form-control select" type="text" id="prjname" value="广州思科智慧城">
                                </td>
                            </tr>
                            <tr class="sm">
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">公建部</td>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">漆枋晨1</td>
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2018-6-14</td>
                            </tr>
                            <tr class="sm">
                                <td class="bold">效果图类型</td>
                                <td class="bold" style="text-align:left;padding-left:10px;" colspan="7">
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">单体</label>
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">群体</label>
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">规划</label>
                                </td>

                            </tr>
                            <tr class="sm">
                                <td class="bold" style="width:12%">数量及费用</td>
                                <td colspan="7" style="padding:5px;">
                                    <table class="table table-bordered" style="margin-bottom: 0px;">
                                        <tbody>
                                            <tr style="background-color: #EEE;">
                                                <td class="bold" style="width:12%">类别</td>
                                                <td class="bold" style="width:12%">新图（张）</td>
                                                <td class="bold" style="width:12%">修改（张）</td>
                                                <td class="bold" style="width:12%">修改量</td>
                                                <td class="bold" style="width:12%">单价</td>
                                                <td class="bold" style="width:40%">预计费用（元）</td>
                                            </tr>
                                            <tr class="sm">
                                                <td>鸟瞰图</td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="1">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="1">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept" class="combobox" style="width:100%;">
                                                        <option value="">0%</option>
                                                        <option value="">10%</option>
                                                        <option value="">20%</option>
                                                        <option value="">30%</option>
                                                        <option value="">40%</option>
                                                        <option value="" selected="selected">50%</option>
                                                        <option value="">60%</option>
                                                        <option value="">70%</option>
                                                        <option value="">80%</option>
                                                        <option value="">90%</option>
                                                        <option value="">100%</option>
                                                    </select>
                                                </td>
                                                <td>3500</td>
                                                <td style="text-align: right;">5250</td>
                                            </tr>
                                            <tr class="sm">
                                                <td>半鸟瞰</td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="1">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="1">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept" class="combobox" style="width:100%;">
                                                        <option value="">0%</option>
                                                        <option value="">10%</option>
                                                        <option value="">20%</option>
                                                        <option value="">30%</option>
                                                        <option value="">40%</option>
                                                        <option value="" selected="selected">50%</option>
                                                        <option value="">60%</option>
                                                        <option value="">70%</option>
                                                        <option value="">80%</option>
                                                        <option value="">90%</option>
                                                        <option value="">100%</option>
                                                    </select>
                                                </td>
                                                <td>2500</td>
                                                <td style="text-align: right;">3750</td>
                                            </tr>
                                            <tr class="sm">
                                                <td>人视图</td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="1">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="0">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept" class="combobox" style="width:100%;">
                                                        <option value="">0%</option>
                                                        <option value="">10%</option>
                                                        <option value="">20%</option>
                                                        <option value="">30%</option>
                                                        <option value="">40%</option>
                                                        <option value="">50%</option>
                                                        <option value="">60%</option>
                                                        <option value="">70%</option>
                                                        <option value="">80%</option>
                                                        <option value="">90%</option>
                                                        <option value="" selected="selected">100%</option>
                                                    </select>
                                                </td>
                                                <td>1400</td>
                                                <td style="text-align: right;">1400</td>
                                            </tr>
                                            <tr class="sm">
                                                <td>小透视</td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="0">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="0">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept" class="combobox" style="width:100%;">
                                                        <option value="">0%</option>
                                                        <option value="">10%</option>
                                                        <option value="">20%</option>
                                                        <option value="">30%</option>
                                                        <option value="">40%</option>
                                                        <option value="">50%</option>
                                                        <option value="">60%</option>
                                                        <option value="">70%</option>
                                                        <option value="">80%</option>
                                                        <option value="">90%</option>
                                                        <option value="" selected="selected">100%</option>
                                                    </select>
                                                </td>
                                                <td>500</td>
                                                <td style="text-align: right;">0</td>
                                            </tr>
                                            <tr class="sm">
                                                <td>立面图</td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="4">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner">
                                                        <input type="text" class="form-control" value="0">
                                                        <div class="input-group-btn-vertical">
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept" class="combobox" style="width:100%;">
                                                        <option value="">0%</option>
                                                        <option value="">10%</option>
                                                        <option value="">20%</option>
                                                        <option value="">30%</option>
                                                        <option value="">40%</option>
                                                        <option value="">50%</option>
                                                        <option value="">60%</option>
                                                        <option value="">70%</option>
                                                        <option value="">80%</option>
                                                        <option value="">90%</option>
                                                        <option value="" selected="selected">100%</option>
                                                    </select>
                                                </td>
                                                <td>100</td>
                                                <td style="text-align: right;">400</td>
                                            </tr>
                                            <tr style="background-color: #EEE;">
                                                <td>合计</td>
                                                <td>
                                                    0
                                                </td>
                                                <td>
                                                    0
                                                </td>
                                                <td>
                                                    -
                                                </td>
                                                <td>-</td>
                                                <td>10800</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr class="sm">
                                <td class="bold">预计开始时间</td>
                                <td colspan="3">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                                <td class="bold">预计结束时间</td>
                                <td colspan="3">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                            </tr>
                            <tr class="sm">
                                <td class="bold">备注</td>
                                <td colspan="7">
                                    <input class="form-control select" type="text" id="prjname" value="">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="table-title clearFix">效果图制作（内部）预约情况
                    </div>
                    <table class="table table-bordered gdate">
                        <tbody>
                            <tr>
                                <td class="bold gmonth" colspan="27">6月</td>
                                <td class="bold gmonth" colspan="31">7月</td>
                                <td class="bold gmonth" colspan="2">8月</td>
                            </tr>
                            <tr>
                                <td class="gday">4</td>
                                <td class="gday">5</td>
                                <td class="gday">6</td>
                                <td class="gday">7</td>
                                <td class="gday">8</td>
                                <td class="gday">9</td>
                                <td class="gday">10</td>
                                <td class="gday">11</td>
                                <td class="gday">12</td>
                                <td class="gday">13</td>
                                <td class="gday today">14</td>
                                <td class="gday">15</td>
                                <td class="gday">16</td>
                                <td class="gday">17</td>
                                <td class="gday">18</td>
                                <td class="gday">19</td>
                                <td class="gday">20</td>
                                <td class="gday">21</td>
                                <td class="gday">22</td>
                                <td class="gday">23</td>
                                <td class="gday">24</td>
                                <td class="gday">25</td>
                                <td class="gday">26</td>
                                <td class="gday">27</td>
                                <td class="gday">28</td>
                                <td class="gday">29</td>
                                <td class="gday">30</td>
                                <td class="gday">1</td>
                                <td class="gday">2</td>
                                <td class="gday">3</td>
                                <td class="gday">4</td>
                                <td class="gday">5</td>
                                <td class="gday">6</td>
                                <td class="gday">7</td>
                                <td class="gday">8</td>
                                <td class="gday">9</td>
                                <td class="gday">10</td>
                                <td class="gday">11</td>
                                <td class="gday">12</td>
                                <td class="gday">13</td>
                                <td class="gday">14</td>
                                <td class="gday">15</td>
                                <td class="gday">16</td>
                                <td class="gday">17</td>
                                <td class="gday">18</td>
                                <td class="gday">19</td>
                                <td class="gday">20</td>
                                <td class="gday">21</td>
                                <td class="gday">22</td>
                                <td class="gday">23</td>
                                <td class="gday">24</td>
                                <td class="gday">25</td>
                                <td class="gday">26</td>
                                <td class="gday">27</td>
                                <td class="gday">28</td>
                                <td class="gday">29</td>
                                <td class="gday">30</td>
                                <td class="gday">31</td>
                                <td class="gday">1</td>
                                <td class="gday">2</td>
                            </tr>
                            <tr>
                                <td colspan="2"></td>
                                <td colspan="10">
                                    <div class="accepted"></div>
                                </td>
                                <td colspan="48">GC170019 塘朗山F地块</td>
                            </tr>
                            <tr>
                                <td colspan="10"></td>
                                <td colspan="3">
                                    <div class="accepted"></div>
                                </td>
                                <td colspan="47">GC170248 金樾美泰天玺</td>
                            </tr>
                            <tr class="current">
                                <td colspan="12"></td>
                                <td colspan="4">
                                    <div class="inreview"></div>
                                </td>
                                <td colspan="44">GC180066 广州思科智慧城</td>
                            </tr>
                            <tr>
                                <td colspan="16"></td>
                                <td colspan="6">
                                    <div class="inreview"></div>
                                </td>
                                <td colspan="38">GC150184 清华大学深圳研究生院创新基地建设工程</td>
                            </tr>
                            <tr>
                                <td colspan="18"></td>
                                <td colspan="14">
                                    <div class="inreview"></div>
                                </td>
                                <td colspan="28">GC170280 清华研究院</td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="text-align:center;">
                        <div class="nodes-inline nodes-inline-node">
                            <div class="nodes nodes-green"><span class="nodes-icon glyphicon glyphicon-ok" aria-hidden="true"></span></div><span class="node_name">发起</span><span class="node_name person">漆枋晨1</span></div>
                        <div class="nodes-inline">
                            <div class="nodes-arrow"><span class="nodes-icon glyphicon glyphicon-arrow-right" aria-hidden="true"></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node">
                            <div class="nodes nodes-orange"></div><span class="node_name">项目负责人</span><span class="node_name person">肖睿</span></div>
                        <div class="nodes-inline">
                            <div class="nodes-arrow"><span class="nodes-icon glyphicon glyphicon-arrow-right" aria-hidden="true"></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node">
                            <div class="nodes nodes-blue"></div><span class="node_name">效果图负责人</span><span class="node_name person">李韵</span></div>
                        <div class="nodes-inline">
                            <div class="nodes-arrow"><span class="nodes-icon glyphicon glyphicon-arrow-right" aria-hidden="true"></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node">
                            <div class="nodes nodes-blue"></div><span class="node_name">完成制作</span><span class="node_name person">李韵</span></div>
                    </div>
                    <div style="text-align:center;">
                        <button class="btn btn-default btn-submit" type="submit">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()


def xgt2():
    name='效果图制作（外包）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=2)
    h.set_selection()
    h.set_tabletitle(['效果图制作申请一览表（外包）',
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">效果图制作申请单（外包）</th>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">工程编号</td>
                                <td style="width:12%">
                                    <input class="form-control select" type="text" id="prjno" value="GC180066">
                                </td>
                                <td class="bold" style="width:12%">工程名称</td>
                                <td style="width:64%" colspan="5">
                                    <input class="form-control select" type="text" id="prjname" value="广州思科智慧城">
                                </td>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">公建部</td>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">漆枋晨1</td>
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2018-6-14</td>
                            </tr>
                            <tr>
                                <td class="bold">制作数量（张）</td>
                                <td>
                                    <div class="input-group spinner">
                                        <input type="text" class="form-control" value="1">
                                        <div class="input-group-btn-vertical">
                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-up"></span></button>
                                            <button class="btn btn-default btn-spinner" type="button"><span class="caret caret-down"></span></button>
                                        </div>
                                    </div>
                                </td>
                                <td class="bold">预计费用（元）</td>
                                <td style="width:12%">
                                    <input class="form-control select" type="text" id="prjno" ">
                                </td>
                                <td class="bold ">预计开始时间</td>
                                <td colspan="1 ">
                                    <div class="input-group ">
                                        <div class="input-group-addon ">
                                            <span class="glyphicon glyphicon-calendar " style="font-size:12px; "></span>
                                        </div>
                                        <input type="text " class="form-control " id="exampleInputAmount ">
                                    </div>
                                </td>
                                <td class="bold ">预计结束时间</td>
                                <td colspan="1 ">
                                    <div class="input-group ">
                                        <div class="input-group-addon ">
                                            <span class="glyphicon glyphicon-calendar " style="font-size:12px; "></span>
                                        </div>
                                        <input type="text " class="form-control " id="exampleInputAmount ">
                                    </div>
                                </td>
                            </tr>
                            <tr class="sm "  style="display:none ">
                                <td class="bold " style="text-align:left;padding-left:10px; " colspan="7 ">
                                    <label class="radio-inline ">
                                        <input class="sm " type="radio " name="inlineRadioOptions " id="inlineRadio1 " value="option1 ">单体</label>
                                    <label class="radio-inline ">
                                        <input class="sm " type="radio " name="inlineRadioOptions " id="inlineRadio1 " value="option1 ">群体</label>
                                    <label class="radio-inline ">
                                        <input class="sm " type="radio " name="inlineRadioOptions " id="inlineRadio1 " value="option1 ">规划</label>
                                </td>

                            </tr>
                            <tr class="sm " style="display:none ">
                                <td class="bold " style="width:12% ">数量及费用</td>
                                <td colspan="7 " style="padding:5px; ">
                                    <table class="table table-bordered " style="margin-bottom: 0px; ">
                                        <tbody>
                                            <tr style="background-color: #EEE; ">
                                                <td class="bold " style="width:12% ">类别</td>
                                                <td class="bold " style="width:12% ">新图（张）</td>
                                                <td class="bold " style="width:12% ">修改（张）</td>
                                                <td class="bold " style="width:12% ">修改量</td>
                                                <td class="bold " style="width:12% ">单价</td>
                                                <td class="bold " style="width:40% ">预计费用（元）</td>
                                            </tr>
                                            <tr class="sm ">
                                                <td>鸟瞰图</td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="1 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="1 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept " class="combobox " style="width:100%; ">
                                                        <option value=" ">0%</option>
                                                        <option value=" ">10%</option>
                                                        <option value=" ">20%</option>
                                                        <option value=" ">30%</option>
                                                        <option value=" ">40%</option>
                                                        <option value=" " selected="selected ">50%</option>
                                                        <option value=" ">60%</option>
                                                        <option value=" ">70%</option>
                                                        <option value=" ">80%</option>
                                                        <option value=" ">90%</option>
                                                        <option value=" ">100%</option>
                                                    </select>
                                                </td>
                                                <td>3500</td>
                                                <td style="text-align: right; ">5250</td>
                                            </tr>
                                            <tr class="sm ">
                                                <td>半鸟瞰</td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="1 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="1 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept " class="combobox " style="width:100%; ">
                                                        <option value=" ">0%</option>
                                                        <option value=" ">10%</option>
                                                        <option value=" ">20%</option>
                                                        <option value=" ">30%</option>
                                                        <option value=" ">40%</option>
                                                        <option value=" " selected="selected ">50%</option>
                                                        <option value=" ">60%</option>
                                                        <option value=" ">70%</option>
                                                        <option value=" ">80%</option>
                                                        <option value=" ">90%</option>
                                                        <option value=" ">100%</option>
                                                    </select>
                                                </td>
                                                <td>2500</td>
                                                <td style="text-align: right; ">3750</td>
                                            </tr>
                                            <tr class="sm ">
                                                <td>人视图</td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="1 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="0 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept " class="combobox " style="width:100%; ">
                                                        <option value=" ">0%</option>
                                                        <option value=" ">10%</option>
                                                        <option value=" ">20%</option>
                                                        <option value=" ">30%</option>
                                                        <option value=" ">40%</option>
                                                        <option value=" ">50%</option>
                                                        <option value=" ">60%</option>
                                                        <option value=" ">70%</option>
                                                        <option value=" ">80%</option>
                                                        <option value=" ">90%</option>
                                                        <option value=" " selected="selected ">100%</option>
                                                    </select>
                                                </td>
                                                <td>1400</td>
                                                <td style="text-align: right; ">1400</td>
                                            </tr>
                                            <tr class="sm ">
                                                <td>小透视</td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="0 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="0 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept " class="combobox " style="width:100%; ">
                                                        <option value=" ">0%</option>
                                                        <option value=" ">10%</option>
                                                        <option value=" ">20%</option>
                                                        <option value=" ">30%</option>
                                                        <option value=" ">40%</option>
                                                        <option value=" ">50%</option>
                                                        <option value=" ">60%</option>
                                                        <option value=" ">70%</option>
                                                        <option value=" ">80%</option>
                                                        <option value=" ">90%</option>
                                                        <option value=" " selected="selected ">100%</option>
                                                    </select>
                                                </td>
                                                <td>500</td>
                                                <td style="text-align: right; ">0</td>
                                            </tr>
                                            <tr class="sm ">
                                                <td>立面图</td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="4 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="input-group spinner ">
                                                        <input type="text " class="form-control " value="0 ">
                                                        <div class="input-group-btn-vertical ">
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-up "></span></button>
                                                            <button class="btn btn-default btn-spinner " type="button "><span class="caret caret-down "></span></button>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <select id="filter-dept " class="combobox " style="width:100%; ">
                                                        <option value=" ">0%</option>
                                                        <option value=" ">10%</option>
                                                        <option value=" ">20%</option>
                                                        <option value=" ">30%</option>
                                                        <option value=" ">40%</option>
                                                        <option value=" ">50%</option>
                                                        <option value=" ">60%</option>
                                                        <option value=" ">70%</option>
                                                        <option value=" ">80%</option>
                                                        <option value=" ">90%</option>
                                                        <option value=" " selected="selected ">100%</option>
                                                    </select>
                                                </td>
                                                <td>100</td>
                                                <td style="text-align: right; ">400</td>
                                            </tr>
                                            <tr style="background-color: #EEE; ">
                                                <td>合计</td>
                                                <td>
                                                    0
                                                </td>
                                                <td>
                                                    0
                                                </td>
                                                <td>
                                                    -
                                                </td>
                                                <td>-</td>
                                                <td>10800</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr  style="display:none ">
                                <td class="bold ">预计开始时间</td>
                                <td colspan="3 ">
                                    <div class="input-group ">
                                        <div class="input-group-addon ">
                                            <span class="glyphicon glyphicon-calendar " style="font-size:12px; "></span>
                                        </div>
                                        <input type="text " class="form-control " id="exampleInputAmount ">
                                    </div>
                                </td>
                                <td class="bold ">预计结束时间</td>
                                <td colspan="3 ">
                                    <div class="input-group ">
                                        <div class="input-group-addon ">
                                            <span class="glyphicon glyphicon-calendar " style="font-size:12px; "></span>
                                        </div>
                                        <input type="text " class="form-control " id="exampleInputAmount ">
                                    </div>
                                </td>
                            </tr>
                            <tr style="height:80px;">
                                <td class="bold ">备注</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="table-title clearFix ">效果图制作（内部）预约情况
                    </div>
                    <table class="table table-bordered gdate ">
                        <tbody>
                            <tr>
                                <td class="bold gmonth " colspan="27 ">6月</td>
                                <td class="bold gmonth " colspan="31 ">7月</td>
                                <td class="bold gmonth " colspan="2 ">8月</td>
                            </tr>
                            <tr>
                                <td class="gday ">4</td>
                                <td class="gday ">5</td>
                                <td class="gday ">6</td>
                                <td class="gday ">7</td>
                                <td class="gday ">8</td>
                                <td class="gday ">9</td>
                                <td class="gday ">10</td>
                                <td class="gday ">11</td>
                                <td class="gday ">12</td>
                                <td class="gday ">13</td>
                                <td class="gday today ">14</td>
                                <td class="gday ">15</td>
                                <td class="gday ">16</td>
                                <td class="gday ">17</td>
                                <td class="gday ">18</td>
                                <td class="gday ">19</td>
                                <td class="gday ">20</td>
                                <td class="gday ">21</td>
                                <td class="gday ">22</td>
                                <td class="gday ">23</td>
                                <td class="gday ">24</td>
                                <td class="gday ">25</td>
                                <td class="gday ">26</td>
                                <td class="gday ">27</td>
                                <td class="gday ">28</td>
                                <td class="gday ">29</td>
                                <td class="gday ">30</td>
                                <td class="gday ">1</td>
                                <td class="gday ">2</td>
                                <td class="gday ">3</td>
                                <td class="gday ">4</td>
                                <td class="gday ">5</td>
                                <td class="gday ">6</td>
                                <td class="gday ">7</td>
                                <td class="gday ">8</td>
                                <td class="gday ">9</td>
                                <td class="gday ">10</td>
                                <td class="gday ">11</td>
                                <td class="gday ">12</td>
                                <td class="gday ">13</td>
                                <td class="gday ">14</td>
                                <td class="gday ">15</td>
                                <td class="gday ">16</td>
                                <td class="gday ">17</td>
                                <td class="gday ">18</td>
                                <td class="gday ">19</td>
                                <td class="gday ">20</td>
                                <td class="gday ">21</td>
                                <td class="gday ">22</td>
                                <td class="gday ">23</td>
                                <td class="gday ">24</td>
                                <td class="gday ">25</td>
                                <td class="gday ">26</td>
                                <td class="gday ">27</td>
                                <td class="gday ">28</td>
                                <td class="gday ">29</td>
                                <td class="gday ">30</td>
                                <td class="gday ">31</td>
                                <td class="gday ">1</td>
                                <td class="gday ">2</td>
                            </tr>
                            <tr>
                                <td colspan="2 "></td>
                                <td colspan="10 ">
                                    <div class="accepted "></div>
                                </td>
                                <td colspan="48 ">GC170019 塘朗山F地块</td>
                            </tr>
                            <tr>
                                <td colspan="10 "></td>
                                <td colspan="3 ">
                                    <div class="accepted "></div>
                                </td>
                                <td colspan="47 ">GC170248 金樾美泰天玺</td>
                            </tr>
                            <tr class="current ">
                                <td colspan="12 "></td>
                                <td colspan="4 ">
                                    <div class="inreview "></div>
                                </td>
                                <td colspan="44 ">GC180066 广州思科智慧城</td>
                            </tr>
                            <tr>
                                <td colspan="16 "></td>
                                <td colspan="6 ">
                                    <div class="inreview "></div>
                                </td>
                                <td colspan="38 ">GC150184 清华大学深圳研究生院创新基地建设工程</td>
                            </tr>
                            <tr>
                                <td colspan="18 "></td>
                                <td colspan="14 ">
                                    <div class="inreview "></div>
                                </td>
                                <td colspan="28 ">GC170280 清华研究院</td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="text-align:center; ">
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-green "><span class="nodes-icon glyphicon glyphicon-ok " aria-hidden="true "></span></div><span class="node_name ">发起</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-orange "></div><span class="node_name ">项目负责人</span><span class="node_name person ">肖睿</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">效果图负责人</span><span class="node_name person ">李韵</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">部门运营副总经理</span><span class="node_name person ">张胜强</span></div>
                            <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">公司主管领导</span><span class="node_name person ">吕柱</span></div>
                    </div>
                    <div style="text-align:center; ">
                        <button class="btn btn-default btn-submit " type="submit ">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()


def ThreeDPrinting1():
    name='3D打印（工程）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=3)
    h.set_selection()
    h.set_tabletitle(['3D打印申请一览表（工程）',
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">3D打印申请单（工程）</th>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">工程编号</td>
                                <td style="width:12%">
                                    <input class="form-control select" type="text" id="prjno" value="GC160019">
                                </td>
                                <td class="bold" style="width:12%">工程名称</td>
                                <td style="width:64%" colspan="5">
                                    <input class="form-control select" type="text" id="prjname" value="深业世纪山谷城市更新单元">
                                </td>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">公建部</td>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">漆枋晨1</td>
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2017-12-3</td>
                            </tr>
                            
                            <tr class="sm">
                                <td class="bold">预约打印日期</td>
                                <td colspan="7">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td class="bold">打印比例</td>
                                <td colspan="7" style="text-align: left;">
                                    <select id="filter-dept" class="combobox" style="width:100px;">
                                        <option value="" selected="selected">1:2000</option>
                                        <option value="">1:1000</option>
                                        <option value="">1:500</option>
                                        <option value="">1:200</option>
                                        <option value="">1:100</option>
                                    </select>
                                </td>
                            </tr>
                            <tr class="sm">
                                <td class="bold">是否需要建模</td>
                                <td class="bold" style="text-align:left;padding-left:10px;" colspan="7">
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">需要</label>
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">不需要</label>
                                </td>
                            </tr>
                            <tr style="height:80px;">
                                <td class="bold ">备注</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="text-align:center; ">
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-green "><span class="nodes-icon glyphicon glyphicon-ok " aria-hidden="true "></span></div><span class="node_name ">发起</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-orange "></div><span class="node_name ">项目负责人</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node " style="width:76px;">
                            <div class="nodes nodes-blue "></div><span class="node_name ">3D打印负责人</span><span class="node_name person ">李韵</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">打印完成</span><span class="node_name person ">李韵</span></div>
                    </div>
                    <div style="text-align:center; ">
                        <button class="btn btn-default btn-submit " type="submit ">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()


def ThreeDPrinting2():
    name='3D打印（部门）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=5)
    h.set_selection()
    h.set_tabletitle(['3D打印申请一览表（部门）',
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">3D打印申请单（部门）</th>
                            </tr>                          
                            <tr>
                                <td class="bold">预约打印日期</td>
                                <td colspan="7">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                            </tr>
                            <tr style="height:80px;">
                                <td class="bold ">打印内容</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                            <tr>
                                <td class="bold">打印比例</td>
                                <td colspan="7" style="text-align: left;">
                                    <select id="filter-dept" class="combobox" style="width:100px;">
                                        <option value="" selected="selected">1:2000</option>
                                        <option value="">1:1000</option>
                                        <option value="">1:500</option>
                                        <option value="">1:200</option>
                                        <option value="">1:100</option>
                                    </select>
                                </td>
                            </tr>
                            <tr class="sm">
                                <td class="bold">是否需要建模</td>
                                <td class="bold" style="text-align:left;padding-left:10px;" colspan="7">
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">需要</label>
                                    <label class="radio-inline">
                                        <input class="sm" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">不需要</label>
                                </td>
                            </tr>
                            
                            <tr>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">陈忱</td>
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">市场品牌推广部</td>
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2017-12-3</td>
                            </tr>
                            
                            
                            <tr style="height:80px;">
                                <td class="bold ">备注</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="text-align:center; ">
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-green "><span class="nodes-icon glyphicon glyphicon-ok " aria-hidden="true "></span></div><span class="node_name ">发起</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-orange "></div><span class="node_name ">部门负责人</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node " style="width:76px;">
                            <div class="nodes nodes-blue "></div><span class="node_name ">3D打印负责人</span><span class="node_name person ">李韵</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">打印完成</span><span class="node_name person ">李韵</span></div>
                    </div>
                    <div style="text-align:center; ">
                        <button class="btn btn-default btn-submit " type="submit ">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()   


def hp1():
    name='航拍（工程）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=4)
    h.set_selection()
    h.set_tabletitle(['航拍申请一览表（工程）',
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">航拍申请单（工程）</th>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">工程编号</td>
                                <td style="width:12%">
                                    <input class="form-control select" type="text" id="prjno" value="GC160019">
                                </td>
                                <td class="bold" style="width:12%">工程名称</td>
                                <td style="width:64%" colspan="5">
                                    <input class="form-control select" type="text" id="prjname" value="深业世纪山谷城市更新单元">
                                </td>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">公建部</td>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">漆枋晨1</td>  
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2017-12-3</td>
                            </tr>

                            
                            
                                            <tr class="sm">
                                <td class="bold">预约航拍日期</td>
                                <td colspan="7">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                            </tr>
                            
                            <tr style="height:80px;">
                                <td class="bold ">备注</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  
                    <div style="text-align:center; ">
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-green "><span class="nodes-icon glyphicon glyphicon-ok " aria-hidden="true "></span></div><span class="node_name ">发起</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-orange "></div><span class="node_name ">项目负责人</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">航拍负责人</span><span class="node_name person ">李韵</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">航拍完成</span><span class="node_name person ">李韵</span></div>
                            
                    </div>
                    <div style="text-align:center; ">
                        <button class="btn btn-default btn-submit " type="submit ">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()


def hp2():
    name='航拍（部门）'
    h=CapolHtml_TablePage()
    h.head.addObj(meta)
    h.head.addObj(icon)
    h.css=["./static/css/bootstrap.min.css","./static/css/jquery.dataTables.min.css","./static/css/CAPOL_WEB_UI.css"]
    h.js=["./static/js/jquery-3.3.1.js","./static/js/bootstrap.min.js","./static/js/jquery.dataTables.min.js"]
    h.page_js=page_js
    h.set_breadcrumb([('工作空间','#'),('流程中心','')])
    h.set_tab1_left([('华阳设计','#'),('华阳造价','#'),('华泰盛','#'),('润阳智造','#')],active=1)
    h.set_tab1_right([('待完成 [1]','#'),('待我审核 [0]','#'),('我发起的 [2]','#')],active=0)
    h.set_nav_lst1([('通用','#'),('运营','#'),('经营','#'),('财务','#'),('人力资源','#'),('市场品牌推广','#'),('采购','#'),('知识产权','#'),('法务','#'),('其他','#')])
    h.set_nav_lst2(index=1,lst=[('盖章申请流程','#'),('……','#'),('……','#')])
    h.set_nav_lst2(index=2,lst=[('效果图制作','#'),('……','#'),('……','#')],active=1)
    h.set_tab2(lst=[('效果图制作（内部）','./xgt1'),('效果图制作（外包）','./xgt2'),('3D打印（工程）','./3dp1'),('航拍（工程）','./hp1'),('3D打印（部门）','./3dp2'),('航拍（部门）','./hp2')],active=6)
    h.set_selection()
    h.set_tabletitle(['航拍申请一览表（部门）',
        button(span(cl="glyphicon glyphicon-plus",aria_hidden="true"),'发起流程',type="button",cl="btn btn-default btn-xs btn-red right-buttons",id="open")])
    t=table()
    t.attributes=h.table.attributes
    t.read_excel('./static/流程-效果图制作.xlsx',sheet=name)
    t.set_col_attr(i=1,style='color:#0068B7;text-decoration: underline;')
    t.set_col_attr(i=3,style='text-align:left;')
    h.table=t
    h.set_form_window(name)
    form='''<div class="form-window-content">
                <form class="table" method="post" action="" style="padding:10px;">
                    <table class="table table-bordered">
                        <tbody>
                            <tr class="title">
                                <th colspan="8" style="background:url(http://cip.capol.cn/capol/homepage/resource/img/logo.png)no-repeat;">航拍申请单（部门）</th>
                            </tr>
                            <tr>
                                <td class="bold">预约航拍日期</td>
                                <td colspan="7">
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <span class="glyphicon glyphicon-calendar" style="font-size:12px;"></span>
                                        </div>
                                        <input type="text" class="form-control" id="exampleInputAmount">
                                    </div>
                                </td>
                            </tr>
                            <tr style="height:80px;">
                                <td class="bold ">计划航拍内容</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                            <tr>
                                <td class="bold" style="width:12%">申请人</td>
                                <td style="width:12%">漆枋晨1</td>
                                <td class="bold" style="width:12%">所属公司</td>
                                <td style="width:12%">深圳公司</td>
                                <td class="bold" style="width:12%">所属部门</td>
                                <td style="width:12%">公建部</td>
                                <td class="bold" style="width:12%">申请日期</td>
                                <td style="width:16%">2017-12-3</td>
                            </tr>
                            <tr style="height:80px;">
                                <td class="bold ">备注</td>
                                <td colspan="7">
                                    <input class="form-control select " type="text" id="prjname " value="" style="height:69px;">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                  
                    <div style="text-align:center; ">
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-green "><span class="nodes-icon glyphicon glyphicon-ok " aria-hidden="true "></span></div><span class="node_name ">发起</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-orange "></div><span class="node_name ">部门负责人</span><span class="node_name person ">漆枋晨1</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">航拍负责人</span><span class="node_name person ">李韵</span></div>
                        <div class="nodes-inline ">
                            <div class="nodes-arrow "><span class="nodes-icon glyphicon glyphicon-arrow-right " aria-hidden="true "></span></div>
                        </div>
                        <div class="nodes-inline nodes-inline-node ">
                            <div class="nodes nodes-blue "></div><span class="node_name ">航拍完成</span><span class="node_name person ">李韵</span></div>
                            
                    </div>
                    <div style="text-align:center; ">
                        <button class="btn btn-default btn-submit " type="submit ">提交</button>
                    </div>
                </form>
            </div>'''
    h.form_window.addObj(form)
    h.generate()
    h.head.addObj(script(page_js,type='text/javascript'))
    return h.page.render()
