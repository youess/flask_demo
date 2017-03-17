# -*- coding: utf-8 -*-


from flask import Flask, render_template
from htmlmin.minify import html_minify


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="denis")


@app.route("/template_inheritance")
def inherit():
    render_html = render_template("child.html",
                                  title="atom", child_name="Curry")
    return html_minify(render_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
