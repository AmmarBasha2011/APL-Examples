
# apl-source:1
# مثال 561 — شركات المحمول المصرية
# apl-source:2
# Egyptian carrier detection
# apl-source:3
# Demonstrates: مقدمة رقم، فودافون، اتصالات، أورانج، وي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/561-egypt-carriers.apl
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
# معرفة شركة المحمول المصرية من مقدمة الرقم
# apl-source:15
def شركة(رقم):
    # apl-source:16
    مقدمة = رقم[:3]
    # apl-source:17
    if مقدمة == "010":
        # apl-source:18
        return "فودافون"
    # apl-source:19
    if مقدمة == "011":
        # apl-source:20
        return "اتصالات"
    # apl-source:21
    if مقدمة == "012":
        # apl-source:22
        return "أورانج"
    # apl-source:23
    if مقدمة == "015":
        # apl-source:24
        return "وي"
    # apl-source:25
    return "غير معروفة"
# apl-source:26

# apl-source:27
تأكد_يساوي(شركة("01012345678"), "فودافون", "010")
# apl-source:28
تأكد_يساوي(شركة("01198765432"), "اتصالات", "011")
# apl-source:29
تأكد_يساوي(شركة("01255512345"), "أورانج", "012")
# apl-source:30
تأكد_يساوي(شركة("01544433221"), "وي", "015")
# apl-source:31
تأكد_يساوي(شركة("01900000000"), "غير معروفة", "019")
# apl-source:32
