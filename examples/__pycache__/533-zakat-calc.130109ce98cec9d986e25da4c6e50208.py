
# apl-source:1
# مثال 533 — حساب زكاة المال
# apl-source:2
# Zakat calculator
# apl-source:3
# Demonstrates: زكاة، نصاب، نسبة 2.5%
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/533-zakat-calc.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# حساب زكاة المال: 2.5% فوق النصاب
# apl-source:15
def زكاة(مال, سعر_جرام_ذهب):
    # apl-source:16
    نصاب = 85 * سعر_جرام_ذهب
    # apl-source:17
    if مال < نصاب:
        # apl-source:18
        return [0, نصاب]
    # apl-source:19
    return [مال * 25 / 1000, نصاب]
# apl-source:20

# apl-source:21
ن1 = زكاة(300000, 3000)
# apl-source:22
print("مال 300000:", ن1)
# apl-source:23
تأكد_يساوي(ن1[0], 7500, "زكاة 300 ألف")
# apl-source:24
تأكد_يساوي(ن1[1], 255000, "النصاب")
# apl-source:25
تأكد_يساوي(زكاة(200000, 3000)[0], 0, "دون النصاب لا زكاة")
# apl-source:26
