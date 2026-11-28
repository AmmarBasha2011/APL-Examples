
# apl-source:1
# مثال 463 — تسطيح القواميس المتداخلة
# apl-source:2
# Flatten nested dict
# apl-source:3
# Demonstrates: مفاتيح مسطحة بنقاط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/463-flatten-dict.apl
# apl-source:6

# apl-source:7
def سطح(قاموس, بادئة_مسار, نتيجة):
    # apl-source:8
    for مفتاح in قاموس.keys():
        # apl-source:9
        قيمة = قاموس[مفتاح]
        # apl-source:10
        مسار = بادئة_مسار + مفتاح
        # apl-source:11
        if type(قيمة) == dict:
            # apl-source:12
            سطح(قيمة, مسار + ".", نتيجة)
        # apl-source:13
        else:
            # apl-source:14
            نتيجة[مسار] = قيمة
# apl-source:15

# apl-source:16
متداخل = {"مستخدم": {"اسم": "عمار", "عمر": 26}, "نشط": True}
# apl-source:17
مسطح = {}
# apl-source:18
سطح(متداخل, "", مسطح)
# apl-source:19
print(مسطح)
# apl-source:20
