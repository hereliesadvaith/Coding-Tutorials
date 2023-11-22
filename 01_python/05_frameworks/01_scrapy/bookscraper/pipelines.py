# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


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


class SaveToDB:
    """
    To save to PostgreSQL database
    """

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost", dbname="mydb", user="postgres", password="db4136", port=5432
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(255),
            price FLOAT,
            availability INT
        )
        """)

    def process_item(self, item, spider):
        """
        To save data
        """
        self.cur.execute("""
        INSERT INTO books (
            name, category, price, availability
        ) VALUES (
            %s, %s, %s, %s
        )
        """, (
            item["name"],
            item["category"],
            item["price"],
            item["availability"]
        )
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """
        Close connection at end.
        """
        self.cur.close()
        self.conn.close()
