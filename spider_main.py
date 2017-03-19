#coding:utf8

from baike_spider import html_downloader, html_parser, url_manager,html_outputer

import sys
reload(sys)

class SpiderMain(object):
    
    def __init__(self):
        self.urlManager = url_manager.UrlManager()
        self.htmlDownloader = html_downloader.HtmlDownloader()
        self.htmlParser = html_parser.HtmlParser()
        self.htmlOutputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        if root_url is None:
            return
        self.urlManager.add_new_url(root_url)
        count = 1
        while self.urlManager.has_new_url():
            try:
                new_url = self.urlManager.get_new_url()
                print 'craw %d:%s' %(count,new_url)
                html_content = self.htmlDownloader.download(new_url)
                new_urls,datas = self.htmlParser.parse(new_url,html_content)
                self.urlManager.add_new_urls(new_urls)
                self.htmlOutputer.collect_data(datas)
                
                if count == 100:
                    break
                
                count +=1
            except:
                print 'craw fail'
            
        self.htmlOutputer.output()   



if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python?sefr=cr"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)