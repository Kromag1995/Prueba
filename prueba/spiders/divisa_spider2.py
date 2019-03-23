import scrapy
from prueba.items import Divisa

class DivisaSpider(scrapy.Spider):
    name = "divisas2"
    start_urls = [
        'https://www.lanacion.com.ar/economia/divisas',
    ]

    def parse(self, response):
        for fila in response.css('div.fila'):
            divisa = Divisa()
            divisa['descripcion'] = fila.css('label.mostrar-mobile::text')[0].extract()
            divisa['ultimo'] = fila.css('label.mostrar-mobile b::text').extract_first()
            divisa['anterior'] = fila.css('label.mostrar-mobile::text')[1].extract() 
            divisa['variacion'] = fila.css('label.mostrar-mobile::text')[2].extract() 
            divisa['fecha'] = fila.css('label.mostrar-mobile::text')[3].extract()
            yield divisa