from flask import Flask, render_template
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def index():  
    return render_template('index.html')  
  
if __name__ =='__main__':  
    app.run(debug = True)