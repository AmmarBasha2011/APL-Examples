
# apl-source:1
# مثال 545 — الاختيار السريع
# apl-source:2
# Quickselect
# apl-source:3
# Demonstrates: اختيار سريع، ك-أصغر، تقسيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/545-quickselect.apl
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
# اختيار سريع: ك-أصغر عنصر دون فرز كامل
# apl-source:15
بيانات = [7, 10, 4, 3, 20, 15]
# apl-source:16

# apl-source:17
def اختر(ق, ك):
    # apl-source:18
    محور = ق[len(ق) - 1]
    # apl-source:19
    أصاغر = [س for س in ق if س < محور]
    # apl-source:20
    مساوون = [س for س in ق if س == محور]
    # apl-source:21
    أكابر = [س for س in ق if س > محور]
    # apl-source:22
    if ك <= len(أصاغر):
        # apl-source:23
        return اختر(أصاغر, ك)
    # apl-source:24
    elif ك <= len(أصاغر) + len(مساوون):
        # apl-source:25
        return محور
    # apl-source:26
    return اختر(أكابر, ك - len(أصاغر) - len(مساوون))
# apl-source:27

# apl-source:28
تأكد_يساوي(اختر(بيانات, 3), 7, "ثالث أصغر")
# apl-source:29
تأكد_يساوي(اختر(بيانات, 1), 3, "الأصغر")
# apl-source:30
تأكد_يساوي(اختر(بيانات, 6), 20, "الأكبر")
# apl-source:31
