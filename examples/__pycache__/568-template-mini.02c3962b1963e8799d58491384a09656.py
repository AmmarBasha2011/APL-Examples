
# apl-source:1
# مثال 568 — محرك قوالب مصغر
# apl-source:2
# Mini template engine
# apl-source:3
# Demonstrates: قوالب، متغيرات، معالجة نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/568-template-mini.apl
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
# محرك قوالب مصغر بمتغيرات {{اسم}}
# apl-source:15
def املأ(قالب, قيم):
    # apl-source:16
    ناتج = ""
    # apl-source:17
    باقي = قالب
    # apl-source:18
    while "{{" in باقي:
        # apl-source:19
        قبل = باقي.split("{{", 1)[0]
        # apl-source:20
        بعد_فتح = باقي.split("{{", 1)[1]
        # apl-source:21
        اسم = بعد_فتح.split("}}", 1)[0]
        # apl-source:22
        باقي = بعد_فتح.split("}}", 1)[1]
        # apl-source:23
        ناتج = ناتج + قبل
        # apl-source:24
        if اسم in قيم:
            # apl-source:25
            ناتج = ناتج + str(قيم[اسم])
        # apl-source:26
        else:
            # apl-source:27
            ناتج = ناتج + "{{" + اسم + "}}"
    # apl-source:28
    return ناتج + باقي
# apl-source:29

# apl-source:30
قالب = "أهلاً {{الاسم}}، رصيدك {{الرصيد}} جنيه في {{البنك}}."
# apl-source:31
قيم = {"الاسم": "عمار", "الرصيد": 1250, "البنك": "الأهلي"}
# apl-source:32
تأكد_يساوي(املأ(قالب, قيم), "أهلاً عمار، رصيدك 1250 جنيه في الأهلي.", "قالب مكتمل")
# apl-source:33
تأكد_يساوي(املأ("x{{مفقود}}y", قيم), "x{{مفقود}}y", "المفقود يبقى كما هو")
# apl-source:34
