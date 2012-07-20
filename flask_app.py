from flask import Flask, render_template, request
flask_app = Flask(__name__)

flask_app.vars = {}

@flask_app.route('/index',methods=['GET','POST'])
def index():
    nquestions = 5
    if request.method == "GET":
        return render_template('userinfo.html',num=nquestions)
    else: #method was POST if not GET, by construction
        flask_app.vars['name'] = request.form['user_name']
        flask_app.vars['age'] = request.form['age']
        f = open('%s %s.txt' %(flask_app.vars['name'],flask_app.vars['age']),'w')
        f.write('Name: %s\n' %(flask_app.vars['name']))
        f.write('Age: %s\n' %(flask_app.vars['age']))
        f.close()

        return render_template('layout.html',num=1,question='How many eyes do you have?',ans1='1',ans2='2',ans3='3')

@flask_app.route('/Next%20Question',methods=['POST'])
def Next%20Question():



if __name__ == '__main__':
    flask_app.run(debug = True)
