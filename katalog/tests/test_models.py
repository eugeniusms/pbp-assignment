from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):

    def setUp(self):
        self.katalog1 = CatalogItem.objects.create(
            item_name = "Macbook Air M1",
            item_price = 17649000,
            item_stock = 69,
            description = "Best Macbook in The World",
            rating = 5,
            item_url = "https://www.tokopedia.com/dwicompany/resmi-ibox-macbook-air-m2-2022-2023-256gb-512gb-chip-terbaru-m2-inter-256gb-space-gray"
        )

    def test_catalogitems_on_creation(self):
        self.assertEquals(self.katalog1.item_name, "Macbook Air M1") # mengecek apakah kedua argumen bernilai sama
        self.assertEquals(self.katalog1.item_price, 17649000)
        self.assertEquals(self.katalog1.item_stock, 69)
        self.assertEquals(self.katalog1.description, "Best Macbook in The World")
        self.assertEquals(self.katalog1.rating, 5)
        self.assertEquals(self.katalog1.item_url, "https://www.tokopedia.com/dwicompany/resmi-ibox-macbook-air-m2-2022-2023-256gb-512gb-chip-terbaru-m2-inter-256gb-space-gray")