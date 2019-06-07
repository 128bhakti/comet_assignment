from django import forms
import scrapy
import json
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

class RegistrationForm(forms.Form):
	tag_name=forms.CharField(max_length=25)


