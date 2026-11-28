
# apl-source:1
# مثال 528 — تحقق لون للبطاقات
# apl-source:2
# Luhn card check
# apl-source:3
# Demonstrates: خوارزمية لون، تحقق بطاقات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/528-luhn-check.apl
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
# تحقق لون لأرقام البطاقات
# apl-source:15
def لون_صالح(رقم):
    # apl-source:16
    م = 0
    # apl-source:17
    ضاعف = False
    # apl-source:18
    for i in range(len(رقم), 0, -1):
        # apl-source:19
        ر = int(رقم[i-1])
        # apl-source:20
        if ضاعف:
            # apl-source:21
            ر = ر * 2
            # apl-source:22
            if ر > 9:
                # apl-source:23
                ر = ر - 9
        # apl-source:24
        م = م + ر
        # apl-source:25
        ضاعف = not ضاعف
    # apl-source:26
    return م % 10 == 0
# apl-source:27

# apl-source:28
تأكد_يساوي(لون_صالح("4539578763621486"), True, "لون: صالح")
# apl-source:29
تأكد_يساوي(لون_صالح("4539578763621487"), False, "لون: خاطئ")
# apl-source:30
تأكد_يساوي(لون_صالح("79927398713"), True, "لون: مثال كلاسيكي")
# apl-source:31
