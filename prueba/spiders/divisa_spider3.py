import scrapy
from prueba.items import Divisa

class DivisaSpider(scrapy.Spider):
    name = "divisas3"
    start_urls = [
        'https://www.lanacion.com.ar/economia/divisas',
    ]

    def parse(self, response):
        for fila in response.css('div.fila'):
            divisa = Divisa()
            divisa['descripcion'] = fila.css('label.mostrar-mobile::text')[0].extract()
            divisa['ultimo'] = fila.css('label.mostrar-mobile b::text').extract_first()
            #divisa['anterior'] = fila.css('label.mostrar-mobile::text')[1].extract() 
            divisa['variacion'] = fila.css('label.mostrar-mobile::text')[2].extract() 
            divisa['fecha'] = fila.css('label.mostrar-mobile::text')[3].extract()
            request = scrapy.Request(url2, parse2)
            request.meta['divisa'] = divisa
            yield request

    def parse2(self, response):
        divisa = response.meta['divisa']
        divisa['anterior'] = fila.css('label.mostrar-mobile::text')[1].extract()
        return divisa