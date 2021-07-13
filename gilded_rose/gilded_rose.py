class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def price_increase(self, item):
        #increasing quality as sale time approches 
        item.quality = item.quality + 1

    def price_decrease(self, item):
        #decreasing quality as sale time approches 
        item.quality = item.quality - 1
    
    def update_quality(self):
        #reducing item quality over time except for Brie & concert
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.price_decrease(item)
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
#                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                        if item.sell_in < 11:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
#                        if item.sell_in < 6:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
            
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self.price_decrease(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
