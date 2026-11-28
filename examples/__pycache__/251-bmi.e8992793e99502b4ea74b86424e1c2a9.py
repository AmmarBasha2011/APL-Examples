
# apl-source:1
# مثال 251 — حاسبة كتلة الجسم
# apl-source:2
# BMI calculator
# apl-source:3
# Demonstrates: حساب وتصنيف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/251-bmi.apl
# apl-source:6

# apl-source:7
def كتلة_الجسم(وزن_كجم, طول_م):
    # apl-source:8
    return وزن_كجم / (طول_م * طول_م)
# apl-source:9

# apl-source:10
def صنف_الكتلة(قيمة):
    # apl-source:11
    if قيمة < 18.5:
        # apl-source:12
        return "نحافة"
    # apl-source:13
    elif قيمة < 25:
        # apl-source:14
        return "طبيعي"
    # apl-source:15
    elif قيمة < 30:
        # apl-source:16
        return "زيادة وزن"
    # apl-source:17
    else:
        # apl-source:18
        return "سمنة"
# apl-source:19

# apl-source:20
for شخص in [{"اسم": "أحمد", "وزن": 70, "طول": 1.75}, {"اسم": "سارة", "وزن": 55, "طول": 1.60}, {"اسم": "خالد", "وزن": 95, "طول": 1.70}]:
    # apl-source:21
    قيمة = كتلة_الجسم(شخص["وزن"], شخص["طول"])
    # apl-source:22
    print(شخص["اسم"], ":", round(قيمة, 1), "-", صنف_الكتلة(قيمة))
# apl-source:23
