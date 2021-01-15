from flask import Flask, redirect, url_for, request, render_template, flash
import myroutes 

app = Flask(__name__, static_url_path='/static')

##adding routes
app.add_url_rule('/', view_func=myroutes.home)
app.add_url_rule('/register', view_func=myroutes.register)
app.add_url_rule('/register_user', view_func=myroutes.submit_file, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=myroutes.login)
app.add_url_rule('/loginAuth', view_func=myroutes.loginAuth,methods=['POST'])
app.add_url_rule('/profile/<user_name>/<img_file_path>', view_func=myroutes.profile)
app.add_url_rule('/sendlogdata/<user_name>/<type>', view_func = myroutes.sendlogdata)

#main
if __name__ == '__main__':
    app.run()