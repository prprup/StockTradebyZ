import pandas as pd
from mootdx.quotes import Quotes



def main():
    client = Quotes.factory(market='std')
    data = client.quotes(symbol=["002891"])
    print(data.columns)

    # 打印列名
    print("字段列表:")
    print(data.columns.tolist())

    # 打印每只股票的所有字段值
    for index, row in data.iterrows():
        print(f"\n股票代码: {row['code']}")
        for col in data.columns:
            if col == "price":
                print(f"{col}: {row[col]:.2f}")
            if col == "servertime":
                print(f"{col}: {row[col]}")

if __name__ == '__main__':
    main()