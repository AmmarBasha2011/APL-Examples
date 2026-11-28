
# apl-source:1
# مثال 29 — مشكلة تغيير العملات
# apl-source:2
# Coin Change Problem (Dynamic Programming)
# apl-source:3
# Demonstrates: dynamic programming, nested loops, counting combinations
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/29-coin-change.apl
# apl-source:6

# apl-source:7
def دالة_عدد_التركيبات(الحد, العملات):
    # apl-source:8
    جدول = [0] * (الحد + 1)
    # apl-source:9
    جدول[0] = 1
    # apl-source:10
    رقم = 0
    # apl-source:11
    while رقم < len(العملات):
        # apl-source:12
        قيمة = العملات[رقم]
        # apl-source:13
        مبلغ = قيمة
        # apl-source:14
        while مبلغ <= الحد:
            # apl-source:15
            جدول[مبلغ] = جدول[مبلغ] + جدول[مبلغ - قيمة]
            # apl-source:16
            مبلغ = مبلغ + 1
        # apl-source:17
        رقم = رقم + 1
    # apl-source:18
    return جدول[الحد]
# apl-source:19

# apl-source:20
عدد_التركيبات = دالة_عدد_التركيبات
def دالة_أقل_عدد(الحد, العملات):
    # apl-source:21
    الأفضل = [0] * (الحد + 1)
    # apl-source:22
    مبلغ = 1
    # apl-source:23
    while مبلغ <= الحد:
        # apl-source:24
        الأفضل[مبلغ] = مبلغ
        # apl-source:25
        رقم = 0
        # apl-source:26
        while رقم < len(العملات):
            # apl-source:27
            قيمة = العملات[رقم]
            # apl-source:28
            if قيمة <= مبلغ:
                # apl-source:29
                مرشح = الأفضل[مبلغ - قيمة] + 1
                # apl-source:30
                if مرشح < الأفضل[مبلغ]:
                    # apl-source:31
                    الأفضل[مبلغ] = مرشح
            # apl-source:32
            رقم = رقم + 1
        # apl-source:33
        مبلغ = مبلغ + 1
    # apl-source:34
    return الأفضل[الحد]
# apl-source:35

# apl-source:36
أقل_عدد = دالة_أقل_عدد
العملات = [1, 3, 4]
# apl-source:37
print("=== تغيير العملات ===")
# apl-source:38
print("العملات المتاحة: " + str(العملات))
# apl-source:39
print("")
# apl-source:40
print("--- عدد التركيبات الممكنة ---")
# apl-source:41
for مبلغ in [0, 4, 6, 8, 12]:
    # apl-source:42
    print("  " + str(مبلغ) + " -> " + str(عدد_التركيبات(مبلغ, العملات)) + " تركيبة")
# apl-source:43
print("")
# apl-source:44
print("--- أقل عدد عملات ---")
# apl-source:45
for مبلغ in [6, 7, 9, 11, 20]:
    # apl-source:46
    print("  " + str(مبلغ) + " -> " + str(أقل_عدد(مبلغ, العملات)) + " عملة")
# apl-source:47
