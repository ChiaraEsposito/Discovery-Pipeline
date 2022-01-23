import flask

from flask import request, jsonify, render_template
import os
import sys


IMAGE_FOLDER = os.path.join('static', 'images')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

import requests
import graphviz
from graphviz import Digraph
from pm4py.visualization.dfg import visualizer as dfg_visualization

  
@app.route('/', methods=['GET'])
def home():
    
    freq =requests.get('http://127.0.0.1:7777/dfgFrequency')
    perf =requests.get('http://127.0.0.1:7777/dfgPerformance')
    median =requests.get('http://127.0.0.1:7777/median')
    total =requests.get('http://127.0.0.1:7777/total')
        
    
    #print(total.text)
    #freq_png = graphviz.Source(freq.text, filename="frequency", format="png")
    #dfg_visualization.save(freq_png, "static/images/frequency.png")
    #freq_img = os.path.join(app.config['UPLOAD_FOLDER'], 'frequency.png')

    #perf_png = graphviz.Source(perf.text, filename="performance", format="png")
    #dfg_visualization.save(perf_png, "static/images/performance.png")
    #perf_img = os.path.join(app.config['UPLOAD_FOLDER'], 'performance.png')
    
    return render_template("index.html", stringF = str(freq.text), stringP = str(perf.text), median = median.text, total = total.text)
    #return render_template("viz-js.html")
    
    
    #return "<h1>This is just an example</h1><p>Here, you should see the Digraph in a String format.</p><img src='dfg.png'>" 

#@app.route('/', methods=['GET','POST'])
@app.route('/', methods=['POST'])
def myPost():
    
    #if request.method == 'POST' and request.form.get("frequency") != '':
    if request.form.get("tabType") == 'frequency':
        if request.form.get('myPathF') != '':
            myPathF = request.form.get('myPathF')
            myActF = request.form.get('myActF')
            
            #path = request.args.get('myPathF')
           
            params = {'myPathF' : myPathF, 'myActF' : myActF}
            f = requests.get('http://127.0.0.1:7777/dfgFreqReduced', params = params)
            perf =requests.get('http://127.0.0.1:7777/dfgPerformance')
           
            #f = requests.post('http://127.0.0.1:7777/dfgFreqReduced', path)
            #f = requests.get('http://127.0.0.1:7777/dfgFreqReduced?myPahtF='+path)
            return render_template("index.html", stringF = str(f.text), stringP = str(perf.text))
            
    if request.form.get("tabType") == 'performance':
        if request.form.get('myPathP') != '':
            myPathP = request.form.get('myPathP')
            myActP = request.form.get('myActP')
            
            #path = request.args.get('myPathF')
           
            params = {'myPathP' : myPathP, 'myActP' : myActP}
            p = requests.get('http://127.0.0.1:7777/dfgPerfReduced', params = params)
            freq =requests.get('http://127.0.0.1:7777/dfgFrequency')
           
            #f = requests.post('http://127.0.0.1:7777/dfgFreqReduced', path)
            #f = requests.get('http://127.0.0.1:7777/dfgFreqReduced?myPahtF='+path)
            return render_template("index.html", stringF = str(freq.text), stringP = str(p.text))        

app.run(host='127.0.0.1', port=8080)