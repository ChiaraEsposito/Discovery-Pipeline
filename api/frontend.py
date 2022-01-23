import flask

from flask import request, jsonify, render_template
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

import requests
import graphviz
from graphviz import Digraph
from pm4py.visualization.dfg import visualizer as dfg_visualization
  
@app.route('/', methods=['GET'])
def myfunction():
    
    freq =requests.get('http://127.0.0.1:7777/dfgFrequency')
    perf =requests.get('http://127.0.0.1:7777/dfgPerformance')
    
    freq_png = graphviz.Source(freq.text, filename="frequency", format="png")
    dfg_visualization.save(freq_png, "static/images/frequency.png")
    freq_img = os.path.join(app.config['UPLOAD_FOLDER'], 'frequency.png')

    perf_png = graphviz.Source(perf.text, filename="performance", format="png")
    dfg_visualization.save(perf_png, "static/images/performance.png")
    perf_img = os.path.join(app.config['UPLOAD_FOLDER'], 'performance.png')
    
    
 
    return render_template("index.html", img_freq = freq_img, img_perf = perf_img, string = str(perf.text))
    #return render_template("viz-js.html")
    
    
    #return "<h1>This is just an example</h1><p>Here, you should see the Digraph in a String format.</p><img src='dfg.png'>" 


app.run(host='127.0.0.1', port=8080)