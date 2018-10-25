import scrapy


class DivisaSpider(scrapy.Spider):
    name = "divisas"
    start_urls = [
        'https://www.lanacion.com.ar/economia/divisas',
    ]

    def parse(self, response):
        for fila in response.css('div.fila'):
            yield {
                'DESCRIPCION': fila.css('label.mostrar-mobile::text')[0].extract(),
                'ULTIMO': fila.css('label.mostrar-mobile b::text').extract_first(),
                'ANTERIOR': fila.css('label.mostrar-mobile::text')[1].extract(),
                'VARIACION':fila.css('label.mostrar-mobile::text')[2].extract(),
                'FECHA':fila.css('label.mostrar-mobile::text')[3].extract(),
            }