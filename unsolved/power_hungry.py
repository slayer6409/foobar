# -*- coding: utf-8 -*-
"""
Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!).

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Python
======

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Test cases
==========

Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"

Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"
"""

def answer(xs):
    input_list = xs
    positive_list = []
    negative_list = []

    for i, num in enumerate(input_list):
        if num in range(1, 1001):
            # 正の数
            positive_list.append(num)
        elif num in range(-1001, 0):
            # 負の数
            negative_list.append(num)

    # 大きい順に並べ替え
    positive_list.reverse()
    print positive_list

    # 絶対値が大きい順に並べ替え
    negative_list.reverse()
    print negative_list

    multi_positive = 1
    multi_negative = 1

    # 正の数の掛け算の合計
    for i, num in enumerate(positive_list):
        multi_positive *= num

    print multi_positive

    # 負の数の掛け算の合計
    negative_list_length = len(negative_list)
    if negative_list_length % 2 == 0:
        # 偶数個の要素
        for i, num in enumerate(negative_list):
            print 'num:', num
            multi_negative *= num
    else:
        # 奇数個の要素
        for i in range(len(negative_list) - 1):
            print 'num:', negative_list[i]
            multi_negative *= negative_list[i]

    print multi_negative

    result = str(multi_positive * multi_negative)

    return result

# xs = [2, 0, 2, 2, 0]
#"8"

xs = [-2, -3, 4, -5, -101, -102, 0]
#"60"

print answer(xs)