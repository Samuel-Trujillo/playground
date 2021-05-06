from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/play')          
def three():
    return render_template('index.html',greet="Welcome!", box1= "", box2= "", box3='') 
@app.route('/play/<int:times>')
def multi(times):
    return render_template('index1.html', greet= "Welcome!", times= times, box= "")
@app.route('/play/<int:times>/<color_chg>')
def multicolor(times,color_chg):
    return render_template('index2.html', greet= "Welcome!", times= times, box= "", color= str(color_chg))

if __name__=="__main__":   
    app.run(debug=True)    
