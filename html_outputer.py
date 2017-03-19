'''
@author: TAIL
'''
#coding:utf8

class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output(self):
        file = open('output.html','w')
        file.write("<html>")
        file.write("<body>")
        file.write("<table>")
        for data in self.datas:
            file.write("<tr>")
            file.write("<td>%s</td>" % data['url'].encode('utf-8'))
            file.write("<td>%s</td>" % data['title'].encode('utf-8'))
            file.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            file.write("</tr>")
        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()
    
    
    



