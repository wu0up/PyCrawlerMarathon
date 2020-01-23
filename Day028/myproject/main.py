import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    ]
    process = CrawlerProcess(get_project_settings())   #假如框架中有不同爬蟲可以在這邊給予不同設定 (e.g. 每個請求之間要 delay 幾秒)
    process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')  #每個爬蟲都有⼀個全局唯一的名稱
                                                                                                        #可以直接透過這個名稱來決定要開始執行哪個爬蟲
                                                                                                        #給予爬蟲有定義的參數來改變爬蟲結果(e.g. start_urls 是⽬目標網⾴頁的參參數)

    process.start()

if __name__ == '__main__':
    main()
