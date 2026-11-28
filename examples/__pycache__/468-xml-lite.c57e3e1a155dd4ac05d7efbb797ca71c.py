
# apl-source:1
# مثال 468 — قارئ وسوم مبسط
# apl-source:2
# Simple tag parser
# apl-source:3
# Demonstrates: استخراج محتوى الوسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/468-xml-lite.apl
# apl-source:6

# apl-source:7
def محتوى_اسم_وسم(نص_الدخل, اسم_وسم):
    # apl-source:8
    بداية_اسم_وسم = "<" + اسم_وسم + ">"
    # apl-source:9
    نهاية_اسم_وسم = "</" + اسم_وسم + ">"
    # apl-source:10
    ب = نص_الدخل.find(بداية_اسم_وسم) + len(بداية_اسم_وسم)
    # apl-source:11
    ن = نص_الدخل.find(نهاية_اسم_وسم)
    # apl-source:12
    return نص_الدخل[ب:ن]
# apl-source:13

# apl-source:14
مستند = "<user><name>عمار</name><age>26</age></user>"
# apl-source:15
print("الاسم:", محتوى_اسم_وسم(مستند, "name"))
# apl-source:16
print("العمر:", محتوى_اسم_وسم(مستند, "age"))
# apl-source:17
