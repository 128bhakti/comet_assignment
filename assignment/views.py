import scrapy
import json

import threading
import time
from scrapy.crawler import Crawler
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy import log, signals, Spider, Item, Field
from scrapy.settings import Settings
from twisted.internet import reactor
from scrapy.http import Response
from scrapy.crawler import CrawlerProcess
from django.shortcuts import render
from django.http import HttpResponse
from scrapy.http import Request
# Create your views here.
from . forms import RegistrationForm

def index(request):
	form= RegistrationForm()
	context={
		"myregistrationform": form
	}
	return render(request,"assignment/index.html",context)


class MediumScraper(scrapy.Spider):
	name = "medium"
	allowed_domain = ['medium.com']
	tag = "bitcoin"
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

def medium_crawl(request):
	form= RegistrationForm()
	tag= request.POST['tag_name']
	print (tag)
	context_a={
		"myregistrationform": form,
		#"crawled_data": request.POST['tag_name']
	}
	settings = Settings()
	settings.set("FEED_FORMAT", "data.csv")
	crawler = CrawlerProcess(settings)
	crawler.signals.connect(abc, signal=signals.spider_closed)
	crawler.configure()
	
	crawler.crawl(MediumScraper())
	time.sleep(5)
	print ("STARTING ENGINE")
	crawler.start()

	return render(request,"assignment/index.html",context_a)