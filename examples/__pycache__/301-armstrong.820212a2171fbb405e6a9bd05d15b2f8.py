
# apl-source:1
# مثال 301 — أعداد أرمسترونج
# apl-source:2
# Armstrong numbers
# apl-source:3
# Demonstrates: مجموع قوى الأرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/301-armstrong.apl
# apl-source:6

# apl-source:7
def أرمسترونج(عدد):
    # apl-source:8
    أرقام = str(عدد)
    # apl-source:9
    طول_الأرقام = len(أرقام)
    # apl-source:10
    مجموع = 0
    # apl-source:11
    for رقم in أرقام:
        # apl-source:12
        مجموع = مجموع + int(رقم) ** طول_الأرقام
    # apl-source:13
    return مجموع == عدد
# apl-source:14

# apl-source:15
print("153:", أرمسترونج(153))
# apl-source:16
print("9474:", أرمسترونج(9474))
# apl-source:17
print("100:", أرمسترونج(100))
# apl-source:18

# apl-source:19
قائمة = [ن for ن in range(1, 1000) if أرمسترونج(ن)]
# apl-source:20
print("أرمسترونج حتى 1000:", قائمة)
# apl-source:21
