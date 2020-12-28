from flask import Flask, redirect, url_for, request, render_template, flash
import myroutes 


app = Flask(__name__)

##adding routes
app.add_url_rule('/', view_func=myroutes.home)
app.add_url_rule('/register', view_func=myroutes.register)
app.add_url_rule('/register_user', view_func=myroutes.submit_file, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=myroutes.login)
app.add_url_rule('/loginAuth', view_func=myroutes.loginAuth,methods=['GET', 'POST'])
app.add_url_rule('/api_call', view_func=myroutes.api_call)
app.add_url_rule('/download', view_func=myroutes.download)

#main
if __name__ == '__main__':
    app.run()