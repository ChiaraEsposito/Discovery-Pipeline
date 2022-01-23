import flask

from flask import request, jsonify, render_template
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


from graphviz import Digraph
#import file xes
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization


    
@app.route('/dfgFrequency', methods=['GET'])
def dfgFrequency():
    log = xes_importer.apply('C:\\Users\\lucia\\Downloads\\running-example.xes')
    
    #DFG - process discovery
    dfg_freq = dfg_discovery.apply(log)
    
    #visualize DFG - frequency
    
    gviz_freq = dfg_visualization.apply(dfg_freq, log=log, variant=dfg_visualization.Variants.FREQUENCY)
    #dfg_visualization.save(gviz_freq, "static/images/frequency.png")
    #freq_img = os.path.join(app.config['UPLOAD_FOLDER'], 'frequency.png')
 
    
    #return render_template("index.html", img_freq = freq_img, img_perf = perf_img, string = str(gviz_freq))
    
    return str(gviz_freq)
    
@app.route('/dfgPerformance', methods=['GET'])
def dfgPerformance():
    log = xes_importer.apply('C:\\Users\\lucia\\Downloads\\running-example.xes')
    
    #DFG - process discovery
    dfg_perf = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
    parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
    
    #visualize DFG - performance 
    gviz_perf = dfg_visualization.apply(dfg_perf, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
    #dfg_visualization.view(gviz)
    #dfg_visualization.save(gviz_perf, "static/images/performance.png")
    #perf_img = os.path.join(app.config['UPLOAD_FOLDER'], 'performance.png')
    
    #return render_template("index.html", img_freq = freq_img, img_perf = perf_img, string = str(gviz_freq))
    #string_html = render_template("string.html", string = str(gviz_freq))
    #frequency = render_template("img_freq.html", img_freq = freq_img)
    #performance = render_template("img_perf.html", img_perf = perf_img)
    
    return str(gviz_perf)
    
app.run(host='127.0.0.1', port=7777)