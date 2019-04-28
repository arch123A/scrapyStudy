    
    scrapy startproject 项目名  新建爬虫项目
    scrapy genspider 爬虫名 xx.cn  建立具体的爬虫
    scrapy crawl itcast  运行具体的爬虫，需要在项目的目录下启动爬虫
    parse这个方法必须有
    .extract()提取XPATH对象中的文字
    .extract_first()提取XPATH对象中第一个的文字
    
    ITEM_PIPELINES = {
   'sprider11.pipelines.Sprider11Pipeline': 300,
   'sprider11.pipelines.Sprider11Pipeline1': 301,
}
    数据会先经过管道中与引擎近的管道
    
