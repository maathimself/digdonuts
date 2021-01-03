from flask import Flask, request, render_template

app = Flask(__name__)

browserList = ['chrome','edge','firefox','konqueror','mozilla','msie','netscape','opera','safari']
#@app.route('/')
#def default_index():
#    if request.user_agent.browser not in browserList:
#       return request.remote_addr+"\n"
#    else:
#       return request.remote_addr
@app.route('/')
def index():
    #if request.user_agent.browser not in browserList:
       return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True, port=5000, host='0.0.0.0')
