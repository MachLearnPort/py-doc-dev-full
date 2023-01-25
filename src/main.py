from log.logger import configure_logger
from utils.submodule import ex_class
from decouple import config

# Use decouple library to import secrets
secret = config('secret')

def main():
    logger = configure_logger("./log/logs/main.log")
    stock_market_data = ex_class(secret)
    stock_market_data.sub_def("Information Technology", "Software")
    logger.info("Retrieved stock market data successfully")

if __name__ == '__main__':
    main()
