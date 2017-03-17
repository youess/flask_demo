
现在介绍jinja2模板

模板引擎是通过对HTML页面和程序之间变量的沟通的固定形式的东西

他可以用来对重复的HTML进行抽象，节省大量的时间

0. 静态文件

[修改固定的静态文件目录][0]

```
# flask里面对静态文件的设置是固定为`static`
url_for('static', filename='style.css')       # 保证文件路径在`static/style.css`
```

1. 变量 `{{ ... }}`

```
{{ foo.bar }} 或 {{ foo['bar'] }}
# 通过python解析3步
# 1. foo.__getitem__('bar')
# 2. getattr(foo, 'bar')
# 3. 如果上两步没有找到则返回undefined object
```

2. 变量过滤

[内置过滤器][1]

```
{{ name|strptags|title }} # 相当于title(strptags(name))
```

3. if判断式

[内置判断式][2]

```
{% if loop.index is divisibleby 3 %}
```

4. for循环

```
{% for item in seq %}
<li>{{ item }}</li>
{% endfor %}
```

5. 注释

```
{# ... #}
```

6. 跳过模板自定义的符号

```
# inline one
{{ '{{' }}, {{ '}}' }}
# bigger section
{% raw %}
<ul>
  {% for item in seq %}
  <li>{{ item }}</li>
  {% endfor %}
</ul
{% endraw %}
```

7. 模板继承

```
# 参考base.html到child.html
```

8. html最小化

```
pip3 install django-htmlmin
```

9. 模板宏

精简固定的HTML代码

```
# 先定义
{% macro input(name, value='', type='text', size=20) -%}
<input type="{{ type  }}" name="{{ name  }}" value="{{
        value|e
}}" size="{{ size  }}">"
{% endmacro %}

# 后使用
<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>

# 不同模板之间需用import
# 靠，用法太多了
```

需要更多的时间去研究[宏用法][3]，感觉跟VB差不多了


[0]: http://flask.pocoo.org/snippets/102/
[1]: http://jinja.pocoo.org/docs/2.9/templates/#builtin-filters
[2]: http://jinja.pocoo.org/docs/2.9/templates/#builtin-tests
[3]: http://jinja.pocoo.org/docs/2.9/templates/#call
