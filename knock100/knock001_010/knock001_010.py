# import numpy
import os
import pandas as pd

# ファイルの配置ディレクトリ
path_dir = 'D:\\Users\\k\\PycharmProjects\\pythonTrainingKnock\\knock100\\knock001_010\\'


def read_csv(file):
    return pd.read_csv(path_dir + file)


def knock001():
    customer_master = read_csv('customer_master.csv')
    item_master = read_csv('item_master.csv')
    # print(customer_master.head())
    return customer_master, item_master


def knock002():
    transaction_1 = read_csv('transaction_1.csv')
    transaction_2 = read_csv('transaction_2.csv')
    transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
    # print(transaction.head())
    # print(len(transaction1))
    # print(len(transaction2))
    # print(len(transaction))
    transaction_detail_1 = read_csv('transaction_detail_1.csv')
    transaction_detail_2 = read_csv('transaction_detail_2.csv')
    transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
    # print(transaction_detail.head())
    return transaction, transaction_detail


def knock003():
    _t, _td = knock002()
    join_data = pd.merge(_td, _t[["transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")
    # print(join_data.head())
    return join_data


def knock004():
    _customer_master, _item_master = knock001()
    _join_data = knock003()
    _join_data = pd.merge(_join_data, _customer_master, on="customer_id", how="left")
    _join_data = pd.merge(_join_data, _item_master, on="item_id", how="left")
    # print(_join_data.head())
    return _join_data


def knock005():
    _join_data = knock004()
    _join_data["price"] = _join_data["quantity"] * _join_data["item_price"]
    # print(_join_data[["quantity", "item_price", "price"]].head())
    return _join_data


def knock006():
    _t, _td = knock002()
    _join_data = knock005()

    print(_t["price"].sum() == _join_data["price"].sum())


def knock007():
    _join_data = knock005()
    print(_join_data.isnull().sum())
    print(_join_data.describe())
    print(_join_data["payment_date"].min())
    print(_join_data["payment_date"].max())


def knock008():
    _join_data = knock005()
    # print(_join_data.dtypes)
    _join_data["payment_date"] = pd.to_datetime(_join_data["payment_date"])
    _join_data["payment_month"] = _join_data["payment_date"].dt.strftime("%Y%m")
    # print(_join_data[["payment_date", "payment_month"]].head())
    print(_join_data.groupby("payment_month").sum()["price"])
    # return _join_data


def knock009():
    pd.show_versions()

