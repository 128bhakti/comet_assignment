import scrapy
from scrapy.http import Response

class MediumScraper(scrapy.Spider):
	name = "medium"
	allowed_domain = ['medium.com']
	start_urls = ['https://medium.com/search?q=bitcoin']

	def parse(self, response):
		for blog in response.xpath("//div[@class='u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block']"):
			#l = ItemLoader(item=CreatorItem(),selector=creator)
			#l.add_xpath('creator_text',".//div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a/text()").get()
			#yield l.load_item()
			yield{


					#'title': response.css(''),
					#'creator_text': response.css('div.site-main surface-container > div.surface > div.screenContent surface-content > div.container u-foreground u-maxWidth1000 u-paddingTop40 > div.js-searchResults > div.row u-relative > div.col u-size9of12 u-sm-size12of12 > div.u-maxWidth600 js-postList > div.js-postListHandle > div.u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block > div.postArticle postArticle--short js-postArticle js-trackPostPresentation > div.u-clearfix u-marginBottom15 u-paddingTop5 > div.postMetaInline u-floatLeft > div.u-flexCenter > div.postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis > a.ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken::string').extract_first(),
					#'details': response.css('')
					

					## //div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/span[@class='readingTime']

					'title': blog.xpath(".//div[@class='section-inner sectionLayout--insetColumn']/h3/text()").get(),
					'creator': blog.xpath(".//div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a/text()").get(),
					'details': blog.xpath(".//div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/a/time/text()").get(),
					'readingTime': blog.xpath(".//span[@class='readingTime']/title/text()").get()
				}
		#self.logger.info('aaa %s',item)
		#return item