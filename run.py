# -*- coding: utf-8 -*-


from flask import Flask


app = Flask(__name__)


# 首页路由
@app.route("/")
def index():
    return "这是首页啊，魂淡"


# 路由为hello的页面
@app.route("/hello")
def hello():
    return "Hello, world"


# 变量
@app.route("/hello/<name>")
def hello_to_someone(name):
    return "hello {}".format(name)


# 变量类型控制
@app.route("/var_limit/<int:pid>")
def get_pid(pid):
    return "Pid : {:d}".format(pid)


# slash的影响
@app.route("/projects/")
def projects():
    return "The project page"


# /about/就会有not found的错误
@app.route("/about")
def about():
    return "The about page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
