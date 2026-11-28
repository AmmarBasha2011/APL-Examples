
# apl-source:1
# مثال 254 — تقسيم الالحساب والإكرامية
# apl-source:2
# Bill and tip splitter
# apl-source:3
# Demonstrates: حساب نسبة وتقسيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/254-tip-split.apl
# apl-source:6

# apl-source:7
def قسم_الالحساب(الحساب, نسبة_إكرامية, أشخاص):
    # apl-source:8
    إكرامية = الحساب * نسبة_إكرامية / 100
    # apl-source:9
    إجمالي = الحساب + إكرامية
    # apl-source:10
    return {"إكرامية": round(إكرامية, 2), "إجمالي": round(إجمالي, 2), "للشخص": round(إجمالي / أشخاص, 2)}
# apl-source:11

# apl-source:12
ن = قسم_الالحساب(250, 10, 4)
# apl-source:13
print("الإكرامية:", ن["إكرامية"])
# apl-source:14
print("الإجمالي:", ن["إجمالي"])
# apl-source:15
print("نصيب كل شخص:", ن["للشخص"])
# apl-source:16
