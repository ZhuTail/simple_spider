'''
@author: TAIL
'''

#coding:utf8

from idlelib.IOBinding import encoding
import parser
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self):
        self.new_urls = set()
    
    def _get_new_urls(self,page_html,soup):
        links =  soup.find_all('a',href = re.compile(r'/item/\S'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_html, new_url)
            self.new_urls.add(new_full_url)
        return self.new_urls
    
    
    def _get_datas(self,page_html,soup):
        res_data = {}
#         <dd class="lemmaWgt-lemmaTitle-title">
        title = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
#         <div class="lemma-summary" label-module="lemmaSummary">/
        summary = soup.find('div',class_ = 'lemma-summary')
        
        res_data['url'] = page_html
        res_data['title'] = title.get_text()
        res_data['summary'] = summary.get_text()
        return res_data
    
    def parse(self,page_url,html_content):
        if html_content is None:
            return None
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf8')
        new_urls = self._get_new_urls(page_url,soup)
        datas = self._get_datas(page_url,soup)
        return new_urls,datas



