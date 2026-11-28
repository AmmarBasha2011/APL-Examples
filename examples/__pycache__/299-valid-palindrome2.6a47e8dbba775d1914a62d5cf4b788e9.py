
# apl-source:1
# مثال 299 — متناظر بحذف حرف واحد
# apl-source:2
# Valid palindrome II
# apl-source:3
# Demonstrates: مؤشران مع فرصة حذف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/299-valid-palindrome2.apl
# apl-source:6

# apl-source:7
def متناظر(نص_الدخل, أيسر, أيمن):
    # apl-source:8
    while أيسر < أيمن:
        # apl-source:9
        if نص_الدخل[أيسر] != نص_الدخل[أيمن]:
            # apl-source:10
            return False
        # apl-source:11
        أيسر = أيسر + 1
        # apl-source:12
        أيمن = أيمن - 1
    # apl-source:13
    return True
# apl-source:14

# apl-source:15
def متناظر_بحذف(نص_الدخل):
    # apl-source:16
    أيسر = 0
    # apl-source:17
    أيمن = len(نص_الدخل) - 1
    # apl-source:18
    while أيسر < أيمن:
        # apl-source:19
        if نص_الدخل[أيسر] != نص_الدخل[أيمن]:
            # apl-source:20
            return متناظر(نص_الدخل, أيسر + 1, أيمن) or متناظر(نص_الدخل, أيسر, أيمن - 1)
        # apl-source:21
        أيسر = أيسر + 1
        # apl-source:22
        أيمن = أيمن - 1
    # apl-source:23
    return True
# apl-source:24

# apl-source:25
print(متناظر_بحذف("aba"))
# apl-source:26
print(متناظر_بحذف("abca"))
# apl-source:27
print(متناظر_بحذف("abc"))
# apl-source:28
