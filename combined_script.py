# 导入 select_stock 和 fetch_kline 的相关功能
from select_stock import main as select_stock_main
from fetch_kline import main as fetch_kline_main


def combined_main():
    fetch_kline_main()
    select_stock_main()


if __name__ == "__main__":
    combined_main()