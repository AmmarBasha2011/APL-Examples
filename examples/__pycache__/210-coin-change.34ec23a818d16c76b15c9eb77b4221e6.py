
# apl-source:1
# مثال 210 — أقل عدد عملات (برمجة ديناميكية)
# apl-source:2
# Coin change (minimum coins)
# apl-source:3
# Demonstrates: جدول ديناميكي، قيمة لا نهائية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/210-coin-change.apl
# apl-source:6

# apl-source:7
def أقل_عملات(عملات, مبلغ):
    # apl-source:8
    لانهائي = مبلغ + 1
    # apl-source:9
    جدول = [لانهائي for _ in range(مبلغ + 1)]
    # apl-source:10
    جدول[0] = 0
    # apl-source:11
    for م in range(1, مبلغ + 1):
        # apl-source:12
        for عملة in عملات:
            # apl-source:13
            if عملة <= م:
                # apl-source:14
                if جدول[م - عملة] + 1 < جدول[م]:
                    # apl-source:15
                    جدول[م] = جدول[م - عملة] + 1
    # apl-source:16
    if جدول[مبلغ] > مبلغ:
        # apl-source:17
        return -1
    # apl-source:18
    return جدول[مبلغ]
# apl-source:19

# apl-source:20
print("مبلغ 11 بعملات [1,2,5]:", أقل_عملات([1, 2, 5], 11))
# apl-source:21
print("مبلغ 3 بعملات [2]:", أقل_عملات([2], 3))
# apl-source:22
print("مبلغ 41 بعملات [1,5,10,25]:", أقل_عملات([1, 5, 10, 25], 41))
# apl-source:23
