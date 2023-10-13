import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            ask_price = quote.get("top_ask")["price"]
            bid_price = quote.get("top_bid")["price"]
            stock = quote.get("stock")
            price = (ask_price + bid_price) / 2
            self.assertEqual(getDataPoint(quote),
                             (stock, bid_price, ask_price, price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            ask_price = quote.get("top_ask")["price"]
            bid_price = quote.get("top_bid")["price"]
            stock = quote.get("stock")
            price = (ask_price + bid_price) / 2
            self.assertEqual(getDataPoint(quote),
                             (stock, bid_price, ask_price, price))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_price_b_zero(self):
        price_a = 20
        price_b = 0

        self.assertIsNone(getRatio(20, 0))

    def test_getRatio_is_correct(self):
        price_a = float(20)
        price_b = float(30)
        ratio = price_a / price_b

        self.assertEqual(ratio, getRatio(price_a, price_b))

    def test_ratio_price_a_zero(self):
        price_a = float(0)
        price_b = float(10)
        ratio = price_a / price_b
        self.assertEqual(ratio, getRatio(price_a, price_b))


if __name__ == '__main__':
    unittest.main()
