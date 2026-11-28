
# apl-source:1
# مثال 214 — الشجرة الثنائية وجولاتها
# apl-source:2
# Binary tree traversals
# apl-source:3
# Demonstrates: عودية على الشجرة، ترتيبات الجولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/214-binary-tree.apl
# apl-source:6

# apl-source:7
class عقدة:
    # apl-source:8
    def __init__(ذات, قيمة):
        # apl-source:9
        ذات.قيمة = قيمة
        # apl-source:10
        ذات.أيسر = None
        # apl-source:11
        ذات.أيمن = None
# apl-source:12

# apl-source:13
def داخلية(عقدة, نتيجة):
    # apl-source:14
    if عقدة == None:
        # apl-source:15
        return
    # apl-source:16
    داخلية(عقدة.أيسر, نتيجة)
    # apl-source:17
    نتيجة.append(عقدة.قيمة)
    # apl-source:18
    داخلية(عقدة.أيمن, نتيجة)
# apl-source:19

# apl-source:20
def قبلية(عقدة, نتيجة):
    # apl-source:21
    if عقدة == None:
        # apl-source:22
        return
    # apl-source:23
    نتيجة.append(عقدة.قيمة)
    # apl-source:24
    قبلية(عقدة.أيسر, نتيجة)
    # apl-source:25
    قبلية(عقدة.أيمن, نتيجة)
# apl-source:26

# apl-source:27
def بعدية(عقدة, نتيجة):
    # apl-source:28
    if عقدة == None:
        # apl-source:29
        return
    # apl-source:30
    بعدية(عقدة.أيسر, نتيجة)
    # apl-source:31
    بعدية(عقدة.أيمن, نتيجة)
    # apl-source:32
    نتيجة.append(عقدة.قيمة)
# apl-source:33

# apl-source:34
جذر = عقدة(1)
# apl-source:35
جذر.أيسر = عقدة(2)
# apl-source:36
جذر.أيمن = عقدة(3)
# apl-source:37
جذر.أيسر.أيسر = عقدة(4)
# apl-source:38
جذر.أيسر.أيمن = عقدة(5)
# apl-source:39

# apl-source:40
أ = []
# apl-source:41
داخلية(جذر, أ)
# apl-source:42
print("داخلية:", أ)
# apl-source:43
ب = []
# apl-source:44
قبلية(جذر, ب)
# apl-source:45
print("قبلية:", ب)
# apl-source:46
ج = []
# apl-source:47
بعدية(جذر, ج)
# apl-source:48
print("بعدية:", ج)
# apl-source:49
