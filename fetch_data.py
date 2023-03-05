from icrawler.builtin import GoogleImageCrawler

classes = ['cat']
size = 30

for c in classes :
    crawler = GoogleImageCrawler(storage={'root_dir':f'dataset/{c.replace(" ", ".")}'})
    crawler.crawl(keyword=c, filters=None, max_num=size, offset=0)