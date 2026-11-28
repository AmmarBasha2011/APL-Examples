
# apl-source:1
# مثال 557 — مسألة جوزيفوس
# apl-source:2
# Josephus problem
# apl-source:3
# Demonstrates: جوزيفوس، إقصاء دائري، متتالية تكرارية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/557-josephus.apl
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
# مسألة جوزيفوس: الناجي من حلقة الإقصاء
# apl-source:15
def ناجي(ن, ك):
    # apl-source:16
    ب = 0
    # apl-source:17
    for i in range(2, ن + 1):
        # apl-source:18
        ب = (ب + ك) % i
    # apl-source:19
    return ب + 1
# apl-source:20

# apl-source:21
تأكد_يساوي(ناجي(7, 3), 4, "7 أشخاص بإقصاء 3")
# apl-source:22
تأكد_يساوي(ناجي(5, 2), 3, "5 بإقصاء 2")
# apl-source:23
تأكد_يساوي(ناجي(1, 1), 1, "شخص واحد")
# apl-source:24
تأكد_يساوي(ناجي(41, 3), 31, "اللغز التاريخي")
# apl-source:25
