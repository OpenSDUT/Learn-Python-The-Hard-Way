#!/usr/bin/env python
# coding=utf-8
import web

urls = {
    '/','index'
}

app = web.application(urls,globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        form = web.input(name="Nobody",greet="Hello")
        greeting = "%s,%s"%(form.greet,form.name)

        return render.index(greeting=greeting)
if __name__=='__main__':
    app.run()
