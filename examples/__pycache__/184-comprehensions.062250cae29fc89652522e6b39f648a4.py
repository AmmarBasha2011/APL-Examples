
# apl-source:1
# مثال 184 — التوليدات الشاملة المتقدمة
# apl-source:2
# Advanced list comprehensions
# apl-source:3
# Demonstrates: توليدات القوائم، المعالجة المتسلسلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/184-comprehensions.apl
# apl-source:6

# apl-source:7
مربعات = [س * س for س in range(10)]
# apl-source:8
print("المربعات:", مربعات)
# apl-source:9

# apl-source:10
مكعبات = [س * س * س for س in range(5)]
# apl-source:11
print("المكعبات:", مكعبات)
# apl-source:12

# apl-source:13
كلمات = ["تفاح", "موز", "كرز"]
# apl-source:14
أطوال = [len(ك) for ك in كلمات]
# apl-source:15
print("الأطوال:", أطوال)
# apl-source:16

# apl-source:17
أحرف = [ك[0] for ك in كلمات]
# apl-source:18
print("الأحرف الأولى:", أحرف)
# apl-source:19

# apl-source:20
مصفوفة = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# apl-source:21
قطري = [مصفوفة[ي][ي] for ي in range(3)]
# apl-source:22
print("القطري:", قطري)
# apl-source:23

# apl-source:24
منقولة = []
# apl-source:25
for ي in range(3):
    # apl-source:26
    صف_جديد = [مصفوفة[ص][ي] for ص in range(3)]
    # apl-source:27
    منقولة.append(صف_جديد)
# apl-source:28
print("المنقولة:", منقولة)
# apl-source:29
