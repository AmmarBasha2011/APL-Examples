
# apl-source:1
# مثال 305 — الأعداد المتناظرة
# apl-source:2
# Palindrome numbers
# apl-source:3
# Demonstrates: عكس العدد حسابيا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/305-palindrome-number.apl
# apl-source:6

# apl-source:7
def اعكس_عدد(عدد):
    # apl-source:8
    معكوس = 0
    # apl-source:9
    while عدد > 0:
        # apl-source:10
        reverse = معكوس * 10 + عدد % 10
        # apl-source:11
        عدد = عدد // 10
    # apl-source:12
    return معكوس
# apl-source:13

# apl-source:14
def متناظر(عدد):
    # apl-source:15
    if عدد < 0:
        # apl-source:16
        return False
    # apl-source:17
    return عدد == اعكس_عدد(عدد)
# apl-source:18

# apl-source:19
print("121:", متناظر(121))
# apl-source:20
print("12321:", متناظر(12321))
# apl-source:21
print("123:", متناظر(123))
# apl-source:22

# apl-source:23
قائمة = [ن for ن in range(1, 200) if متناظر(ن)]
# apl-source:24
print("عدد المتناظرة حتى 200:", len(قائمة))
# apl-source:25
