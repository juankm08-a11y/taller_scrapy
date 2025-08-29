import scrapy 

class WorldPopulationSpider(scrapy.Spider):
    name = "world_population"
    start_urls = [
        "https://www.worldmeters.info/world-population/"
    ]
    
    def parse(self,response):
        rows = response.css("table#example2 tbody tr")
        
        for row in rows:
            yield {
                "country": row.css("td:nth-child(2) a::text").get(),
                "population_2024": row.css("td:nth-child(3)::text").get(),
                "yearly_change": row.css("td:nth-child(4)::text").get(),
                "net_change": row.css("td:nth-child(5)::text").get(),
                "density_per_km2": row.css("td:nth-child(6)::text").get(),
                "land_area_km2": row.css("td:nth-child(7)::text").get(),
            }
            