# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        ## stip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "description":
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()

        ## availability --> extract number of books in stock
        availability_string = adapter.get("availability")
        split_string_array = availability_string.split("(")
        if len(split_string_array) < 2:
            adapter["availability"] = 0
        else:
            availability_array = split_string_array[1].split(" ")
            adapter["availability"] = int(availability_array[0])

        return item
