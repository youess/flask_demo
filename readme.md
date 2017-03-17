
现在更加深入的了解路由是什么，路由即是用户访问页面的URL

每个页面对应一个路由，那么用户就不用每次都到一个固定的地方，然后继续跳转

Flask路由是基于Werkzeug的路由模块

1. 简单直接

```
@app.route("/hello/fix_url")
def func():
  return "hello fix url"
```

2. 变量规则的URL，可以对变量进行类型限制

```
# <id:pid>, <name>
@app.route("/hello/<name>")
def hello(name):
  return "hello {}".format(name)
```

3. URL路径后加不加`/`

```
# flask的url匹配模式`'admin/'`
# 由于`/project/`这种路由，如果用户输入了/project的话，
# flask也会进行跳转到/project/，所以POST数据可能会丢失
# 所以写路由的时候，最后不要加`/`
@app.route("/about")
def about():
  return "about page"
```

4. 路由加HTTP方法

```
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    do_the_login()
  else:
    show_the_login_form()
```

HTTP方法解释：

1. `GET`, 浏览器告诉服务器仅仅获取当前页面存储的信息
2. `HEAD`，服务器只会读页面的`header`部分
3. `POST`，提交数据到服务器，并只在页面停留一次
4. 其他如`PUT`, `DELETE`, `OPTIONS`


* [flask的/解释][1]



[1]: http://www.it610.com/article/1243223.htm
