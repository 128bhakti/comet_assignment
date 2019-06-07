import scrapy
from scrapy.http import Response

class MediumScraper(scrapy.Spider):
	name = "medium"
	allowed_domain = ['medium.com']
	tag = 'yoga'
	start_urls = ['https://medium.com/search?q='+tag]

	def parse(self, response):
		for blog in response.xpath("//div[@class='u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block']"):
			#l = ItemLoader(item=CreatorItem(),selector=creator)
			#l.add_xpath('creator_text',".//div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a/text()").get()
			#yield l.load_item()
			yield{
					## //div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/span[@class='readingTime']

					'title': blog.xpath(".//div[@class='section-inner sectionLayout--insetColumn']/h3/text()").get(),
					'creator': blog.xpath(".//div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a/text()").get(),
					'details': blog.xpath(".//div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/a/time/text()").get(),
					'readingTime': blog.xpath(".//span[@class='readingTime']").extract_first()
				}
		#self.logger.info('aaa %s',item)
		#return item