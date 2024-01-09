#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/27 15:44
@Author  : Caps
@File    : 查找Enovia widget
"""


def useCsv():
    import csv
    with open('all bus objects of AppDefinition.xlsx', 'r', encoding='UTF8', newline='') as f:
        reader = csv.reader(f)
        for i, item in enumerate(reader):
            print(item)


def usePd():
    import pandas as pd
    # 读取excel文件
    df = pd.read_excel('all bus objects of AppDefinition.xlsx', engine='openpyxl')
    columns = ['App Brand', 'App Display Name', 'App Type', 'App URL']
    other_cols = [col for col in df.columns if col not in columns]

    df = df[columns + other_cols]

    df = df.sort_values(by=columns)

    # # 过滤出App Brand等于Enovia的记录
    # df_filtered = df[df['App Name'] == 'ENOVIA']
    #
    # # 写入一个新的excel
    # df_filtered.to_excel('filtered_data.xlsx', index=False)

    # 用pandas读取excel，并根据列名为App Brand的值分组，将不同分组的记录写入到不同excel中
    grouped = df.groupby('App Brand')
    for name, group in grouped:
        output_file = f'{name}.xlsx'
        group.to_excel(output_file, index=False)


if __name__ == '__main__':
    usePd()
