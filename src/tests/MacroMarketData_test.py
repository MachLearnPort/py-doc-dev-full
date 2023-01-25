import unittest
from unittest.mock import MagicMock, patch
from utils.macro_analysis import MacroMarketData

class TestStockMarketData(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_API_KEY"
        self.stock_market_data = MacroMarketData(self.api_key)
        
    def test_get_performance_metrics(self):
        # Test the get_performance_metrics method with a mocked response
        with patch('your_module.requests.get') as mocked_get:
            mocked_get.return_value = MagicMock(ok=True, json=lambda: {'Rank A: Real-Time Performance': {'Technology': {'Software': {'1 Day Performance': '1.25%', '5 Day Performance': '2.50%', '1 Month Performance': '3.75%', '3 Month Performance': '5.00%', 'YTD Performance': '6.25%'}}}})
            self.stock_market_data.get_performance_metrics("Technology", "Software")
            mocked_get.assert_called_once()
            mocked_get.assert_called_with(f"https://www.alphavantage.co/query?function=SECTOR&apikey={self.api_key}&region=US")
        
    def test_get_performance_metrics_no_data(self):
        # Test the get_performance_metrics method with a mocked response that returns no data
        with patch('your_module.requests.get') as mocked_get:
            mocked_get.return_value = MagicMock(ok=True, json=lambda: {'Rank A: Real-Time Performance': {}})
            self.assertRaises(KeyError, self.stock_market_data.get_performance_metrics, "Technology", "Software")
            mocked_get.assert_called_once()
            mocked_get.assert_called_with(f"https://www.alphavantage.co/query?function=SECTOR&apikey={self.api_key}&region=US")
            
    def test_get_performance_metrics_invalid_response(self):
        # Test the get_performance_metrics method with a mocked response that returns an invalid response
        with patch('your_module.requests.get') as mocked_get:
            mocked_get.return_value = MagicMock(ok=False)
            self.assertRaises(Exception, self.stock_market_data.get_performance_metrics, "Technology", "Software")
            mocked_get.assert_called_once()
            mocked_get.assert_called_with(f"https://www.alphavantage.co/query?function=SECTOR&apikey={self.api_key}&region=US")

if __name__ == '__main__':
    unittest.main()
