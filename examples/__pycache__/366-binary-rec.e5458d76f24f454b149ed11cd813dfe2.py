
# apl-source:1
# مثال 366 — التحويل لثنائي بالعودية
# apl-source:2
# Recursive binary conversion
# apl-source:3
# Demonstrates: بناء النص من البواقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/366-binary-rec.apl
# apl-source:6

# apl-source:7
def إلى_ثنائي(عدد):
    # apl-source:8
    if عدد < 2:
        # apl-source:9
        return str(عدد)
    # apl-source:10
    return إلى_ثنائي(عدد // 2) + str(عدد % 2)
# apl-source:11

# apl-source:12
print("10 =", إلى_ثنائي(10))
# apl-source:13
print("42 =", إلى_ثنائي(42))
# apl-source:14
print("255 =", إلى_ثنائي(255))
# apl-source:15
