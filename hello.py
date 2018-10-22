# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
from tablepage import *

import xgt,prjquality


app = Flask(__name__)

app.add_url_rule('/xgt1',view_func=xgt.xgt1)
app.add_url_rule('/xgt2',view_func=xgt.xgt2)
app.add_url_rule('/3dp1',view_func=xgt.ThreeDPrinting1)
app.add_url_rule('/3dp2',view_func=xgt.ThreeDPrinting2)
app.add_url_rule('/hp1',view_func=xgt.hp1)
app.add_url_rule('/hp2',view_func=xgt.hp2)

app.add_url_rule('/prjreview',view_func=prjquality.prjreview)
app.add_url_rule('/prj_review_record',view_func=prjquality.prj_review_record)
app.add_url_rule('/prj_design_review_status',view_func=prjquality.prj_design_review_status)
app.add_url_rule('/design_prj_review_status',view_func=prjquality.design_prj_review_status)
app.add_url_rule('/prj_review_review_status',view_func=prjquality.prj_review_review_status)
app.add_url_rule('/review_prj_review_status',view_func=prjquality.review_prj_review_status)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    #prjreview()