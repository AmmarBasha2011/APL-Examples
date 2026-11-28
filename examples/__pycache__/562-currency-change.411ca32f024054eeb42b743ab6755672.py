
# apl-source:1
# مثال 562 — فك فئات الجنيه
# apl-source:2
# Egyptian currency change
# apl-source:3
# Demonstrates: فئات نقدية، جشع، قروش
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/562-currency-change.apl
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
# فك مبلغ إلى فئات الجنيه المصري (بالقروش لتفادي الكسور)
# apl-source:15
def فك_مبلغ(قروش):
    # apl-source:16
    فئات = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 25]
    # apl-source:17
    نتيجة = dict()
    # apl-source:18
    متبقي = قروش
    # apl-source:19
    for فئة in فئات:
        # apl-source:20
        عد = متبقي // فئة
        # apl-source:21
        if عد > 0:
            # apl-source:22
            نتيجة[فئة] = عد
            # apl-source:23
            متبقي = متبقي - عد * فئة
    # apl-source:24
    return [نتيجة, متبقي]
# apl-source:25

# apl-source:26
نتيجة = فك_مبلغ(78675)
# apl-source:27
print("786.75 جنيه =", نتيجة[0])
# apl-source:28
تأكد_يساوي(نتيجة[0][20000], 3, "ثلاث ورقات 200")
# apl-source:29
تأكد_يساوي(نتيجة[1], 0, "بلا باقي")
# apl-source:30
قطع = 0
# apl-source:31
for فئة in نتيجة[0]:
    # apl-source:32
    قطع = قطع + نتيجة[0][فئة]
# apl-source:33
تأكد_يساوي(قطع, 11, "11 ورقة وعملة")
# apl-source:34
