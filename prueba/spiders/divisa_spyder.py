import scrapy


class DivisaSpider(scrapy.Spider):
    name = "divisas"
    start_urls = [
        'https://www.lanacion.com.ar/economia/divisas',
    ]

    def parse(self, response):
        filas = response.css('div.fila')
        for fila in filas:
            yield {
                'descripcion': fila.css('label.mostrar-mobile::text')[0].extract(),
                'ultimo': fila.css('label.mostrar-mobile b::text').extract_first(),
                'anterior': fila.css('label.mostrar-mobile::text')[1].extract(),
                'variacion':fila.css('label.mostrar-mobile::text')[2].extract(),
                'fecha':fila.css('label.mostrar-mobile::text')[3].extract(),
            }