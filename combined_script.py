# 导入 select_stock 和 fetch_kline 的相关功能
from select_stock import main as select_stock_main
from fetch_kline import main as fetch_kline_main


def combined_main():
    # 先执行 fetch_kline 的主函数
    fetch_kline_main()

    # 然后执行 select_stock 的主函数
    select_stock_main()


if __name__ == "__main__":
    combined_main()