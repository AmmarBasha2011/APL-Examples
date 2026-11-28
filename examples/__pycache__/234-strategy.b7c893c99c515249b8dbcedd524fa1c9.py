
# apl-source:1
# مثال 234 — نمط الاستراتيجية
# apl-source:2
# Strategy pattern
# apl-source:3
# Demonstrates: تبديل الخوارزمية وقت التشغيل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/234-strategy.apl
# apl-source:6

# apl-source:7
def خصم_عادي(سعر):
    # apl-source:8
    return سعر
# apl-source:9

# apl-source:10
def خصم_طالب(سعر):
    # apl-source:11
    return سعر * 0.9
# apl-source:12

# apl-source:13
def خصم_ذهبي(سعر):
    # apl-source:14
    return سعر * 0.75
# apl-source:15

# apl-source:16
def احسب(سعر, استراتيجية):
    # apl-source:17
    return استراتيجية(سعر)
# apl-source:18

# apl-source:19
سعر = 200
# apl-source:20
print("عادي:", احسب(سعر, خصم_عادي))
# apl-source:21
print("طالب:", احسب(سعر, خصم_طالب))
# apl-source:22
print("ذهبي:", احسب(سعر, خصم_ذهبي))
# apl-source:23
