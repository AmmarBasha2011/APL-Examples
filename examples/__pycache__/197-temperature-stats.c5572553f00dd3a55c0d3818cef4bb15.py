
# apl-source:1
# مثال 197 — إحصاءات درجات الحرارة
# apl-source:2
# Temperature statistics
# apl-source:3
# Demonstrates: حسابات يدوية، مفرز، تقرير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/197-temperature-stats.apl
# apl-source:6

# apl-source:7
درجات = [22, 25, 19, 30, 27, 24, 21, 26, 28, 23]
# apl-source:8

# apl-source:9
مجموع = 0
# apl-source:10
for د in درجات:
    # apl-source:11
    مجموع = مجموع + د
# apl-source:12
متوسط = مجموع / len(درجات)
# apl-source:13

# apl-source:14
مرتبة = sorted(درجات)
# apl-source:15
أدنى = مرتبة[0]
# apl-source:16
أقصى = مرتبة[-1]
# apl-source:17
قيمة_وسيطة = (مرتبة[4] + مرتبة[5]) / 2
# apl-source:18

# apl-source:19
print("القراءات:", درجات)
# apl-source:20
print("المتوسط:", متوسط)
# apl-source:21
print("القيمة_وسيطة:", قيمة_وسيطة)
# apl-source:22
print("أدنى:", أدنى, "| أقصى:", أقصى)
# apl-source:23
print("المدى:", أقصى - أدنى)
# apl-source:24
