# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        """
        To manipulate data, to temporarly store data
        """
        adapter = ItemAdapter(item)

        # strip all whitespaces from string
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "name":
                adapter[field_name] = adapter[field_name].strip()
        # lowercase category
        adapter["category"] = adapter["category"].lower()
        # float price
        adapter["price"] = float(adapter["price"])
        # int availability
        adapter["availability"] = int(adapter["availability"])

        return item
