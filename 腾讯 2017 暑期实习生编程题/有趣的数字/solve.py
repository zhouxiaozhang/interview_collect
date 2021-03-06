#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
有n个数，两两组成二元组，差的绝对值最小的有多少对呢？差的绝对值最大的呢？
保证:
1<=N<=100000,0<=ai<=INT_MAX.

输出描述:
    对于每组数据，输出两个数，第一个数表示差的绝对值最小的对数，第二个数表示差的绝对值最大的对数。
输入例子:
6
45 12 45 32 5 6
输出例子:
1 2

以下参考网上的思路编写的
"""
from collections import OrderedDict

__author__ = '__L1n__w@tch'


def solve(n, data):
    """
    求解出差的绝对值最小的对数以及差的绝对值最大的对数
    :param n: 待输入数据的个数, such as 6
    :param data: 待输入的数据, such as [45, 12, 45, 32, 5, 6]
    :return: 差的绝对值最小的对数, 差的绝对值最大的对数, 比如 (1, 2)
    """
    data = sorted(list(map(int, data.split())))

    # 读取时创建字典, 判断是否有重复数字
    od = OrderedDict()
    has_same_number = False
    min_abs_sub_pairs, max_abs_sub_pairs = 0, 0

    if n == 1:
        return "{} {}".format(0, 0)

    for each_number in data:
        value = od.get(each_number, 0)
        if value > 0:
            has_same_number = True
        od[each_number] = value + 1

    # if 分支, 有重复数字则遍历求取, 每个有重复数字能提供 n * (n - 1) / 2 对
    if has_same_number:
        for each_number in od:
            min_abs_sub_pairs += od[each_number] * (od[each_number] - 1) // 2
    else:  # 无重复数字则依次遍历求取
        temp_od = od.copy()  # 拷贝一份以便后面处理
        pre_items = temp_od.popitem(last=False)  # 获取最小项
        min_abs_sub = -1  # 初始化

        # 遍历每一项
        for next_items in temp_od.items():
            if min_abs_sub == -1 or abs(pre_items[0] - next_items[0]) < min_abs_sub:
                min_abs_sub = abs(pre_items[0] - next_items[0])
                min_abs_sub_pairs = pre_items[1] * next_items[1]
            elif min_abs_sub == abs(pre_items[0] - next_items[0]):
                min_abs_sub_pairs += pre_items[1] * next_items[1]
            pre_items = next_items

    # 计算绝对值最大的对数, 最高和最低个数乘积即可
    max_abs_sub_pairs = od.popitem(last=True)[1] * od.popitem(last=False)[1]

    return "{} {}".format(min_abs_sub_pairs, max_abs_sub_pairs)


def right(n, a):
    try:
        n = n
        a = list(map(int, a.split()))
        # n = input()
        # a = map(int, input().split())
    except:
        exit()
    if n == 1:
        return 0, 0
    else:
        a = sorted(a)
        m = a[1] - a[0]
        for i in range(2, n):
            m = min(m, a[i] - a[i - 1])
            if m == 0:
                break
        cnt = 0
        if m == 0:
            from itertools import groupby
            for k, v in groupby(a):
                l = len(list(v))
                cnt += (l - 1) * l // 2
        else:
            for i in range(1, n):
                if a[i] - a[i - 1] == m:
                    cnt += 1
        return cnt, n * (n - 1) // 2 if a[0] == a[-1] else a.count(a[0]) * a.count(a[-1])


if __name__ == "__main__":
    length = 6
    a_list = "6173 1649 3865 7865 4549 8549"
    print(solve(length, a_list))
    print(right(length, a_list))
