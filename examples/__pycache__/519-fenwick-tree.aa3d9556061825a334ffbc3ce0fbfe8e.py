
# apl-source:1
# مثال 519 — شجرة فينويك
# apl-source:2
# Fenwick tree (BIT)
# apl-source:3
# Demonstrates: شجرة فينويك، مجاميع بادئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/519-fenwick-tree.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# شجرة فينويك (BIT) للمجاميع البادئة
# apl-source:15
ن = 6
# apl-source:16
شجرة = [0, 0, 0, 0, 0, 0, 0]
# apl-source:17

# apl-source:18
def زد(i, فرق):
    # apl-source:19
    while i <= ن:
        # apl-source:20
        شجرة[i] = شجرة[i] + فرق
        # apl-source:21
        i = i + (i & (0 - i))
# apl-source:22

# apl-source:23
def بادئة(i):
    # apl-source:24
    م = 0
    # apl-source:25
    while i > 0:
        # apl-source:26
        م = م + شجرة[i]
        # apl-source:27
        i = i - (i & (0 - i))
    # apl-source:28
    return م
# apl-source:29

# apl-source:30
قيم = [3, 2, -1, 6, 5, 4]
# apl-source:31
for i in range(ن):
    # apl-source:32
    زد(i + 1, قيم[i])
# apl-source:33
تأكد_يساوي(بادئة(6), 19, "المجموع الكلي")
# apl-source:34
تأكد_يساوي(بادئة(3), 4, "بادئة حتى 3")
# apl-source:35
زد(4, 2)
# apl-source:36
تأكد_يساوي(بادئة(4), 12, "بعد إضافة 2 للعنصر 4")
# apl-source:37
