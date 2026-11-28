
# apl-source:1
# مثال 520 — مرشح بلوم
# apl-source:2
# Bloom filter
# apl-source:3
# Demonstrates: مرشح بلوم، تجزئة متعددة، عضوية تقريبية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/520-bloom-filter.apl
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
# مرشح بلوم: عضوية تقريبية بثلاث تجزئات
# apl-source:15
حجم = 32
# apl-source:16
مرشح = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# apl-source:17

# apl-source:18
def تجزئة_بذرة(نص, بذرة):
    # apl-source:19
    ح = بذرة
    # apl-source:20
    for حرف in نص:
        # apl-source:21
        ح = (ح * 31 + ord(حرف)) % حجم
    # apl-source:22
    return ح
# apl-source:23

# apl-source:24
def أضف_عنصر(نص):
    # apl-source:25
    for بذرة in [3, 7, 11]:
        # apl-source:26
        مرشح[تجزئة_بذرة(نص, بذرة)] = 1
# apl-source:27

# apl-source:28
def ربما_موجود(نص):
    # apl-source:29
    for بذرة in [3, 7, 11]:
        # apl-source:30
        if مرشح[تجزئة_بذرة(نص, بذرة)] == 0:
            # apl-source:31
            return False
    # apl-source:32
    return True
# apl-source:33

# apl-source:34
أضف_عنصر("تفاح")
# apl-source:35
أضف_عنصر("موز")
# apl-source:36
تأكد_يساوي(ربما_موجود("تفاح"), True, "بلوم: المضاف يوجد")
# apl-source:37
تأكد_يساوي(ربما_موجود("موز"), True, "بلوم: الثاني يوجد")
# apl-source:38
تأكد_يساوي(ربما_موجود("عنب"), False, "بلوم: الغائب مرفوض هنا")
# apl-source:39
