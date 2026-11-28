
# apl-source:1
# مثال 1124 — نظام المترو
# apl-source:2
# Underground system average travel time
# apl-source:3
# Demonstrates: تسجيل الدخول والخروج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1124-underground-system.apl
# apl-source:6

# apl-source:7
# نسجل وقت دخول كل راكب ومحطته
# apl-source:8
# وعند الخروج نخزن زمن الرحلة لحساب المتوسط
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class مترو:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.ركاب = []
        # apl-source:21
        ذات.دخول = []
        # apl-source:22
        ذات.ازواج = []
        # apl-source:23
        ذات.ازمنة = []
# apl-source:24

    # apl-source:25
    def دخل(ذات, رقم, محطة, وقت):
        # apl-source:26
        ذات.ركاب = ذات.ركاب + [رقم]
        # apl-source:27
        ذات.دخول = ذات.دخول + [[محطة, وقت]]
# apl-source:28

    # apl-source:29
    def خرج(ذات, رقم, محطة, وقت):
        # apl-source:30
        ف = 0
        # apl-source:31
        while ذات.ركاب[ف] != رقم:
            # apl-source:32
            ف = ف + 1
        # apl-source:33
        بدأ = ذات.دخول[ف]
        # apl-source:34
        ذات.ركاب[ف] = -1
        # apl-source:35
        زوج = [بدأ[0], محطة]
        # apl-source:36
        if زوج not in ذات.ازواج:
            # apl-source:37
            ذات.ازواج = ذات.ازواج + [زوج]
            # apl-source:38
            ذات.ازمنة = ذات.ازمنة + [[]]
        # apl-source:39
        ك = 0
        # apl-source:40
        while ذات.ازواج[ك] != زوج:
            # apl-source:41
            ك = ك + 1
        # apl-source:42
        ذات.ازمنة[ك] = ذات.ازمنة[ك] + [وقت - بدأ[1]]
# apl-source:43

    # apl-source:44
    def متوسط_رحلة(ذات, من, الى):
        # apl-source:45
        ك = 0
        # apl-source:46
        while ذات.ازواج[ك] != [من, الى]:
            # apl-source:47
            ك = ك + 1
        # apl-source:48
        مج = 0
        # apl-source:49
        for ز in ذات.ازمنة[ك]:
            # apl-source:50
            مج = مج + ز
        # apl-source:51
        return مج / len(ذات.ازمنة[ك])
# apl-source:52

# apl-source:53
م = مترو()
# apl-source:54
م.دخل(45, "Leyton", 3)
# apl-source:55
م.دخل(32, "Paradise", 8)
# apl-source:56
م.دخل(27, "Leyton", 10)
# apl-source:57
م.خرج(45, "Waterloo", 15)
# apl-source:58
م.خرج(27, "Waterloo", 20)
# apl-source:59
م.خرج(32, "Cambridge", 22)
# apl-source:60
تأكد_يساوي(م.متوسط_رحلة("Paradise", "Cambridge"), 14.0, "باراديس إلى كامبريدج")
# apl-source:61
تأكد_يساوي(م.متوسط_رحلة("Leyton", "Waterloo"), 11.0, "ليتون إلى واترلو")
# apl-source:62
م.دخل(10, "Leyton", 24)
# apl-source:63
تأكد_يساوي(م.متوسط_رحلة("Leyton", "Waterloo"), 11.0, "لم يتغير بعد")
# apl-source:64
م.خرج(10, "Waterloo", 38)
# apl-source:65
تأكد_يساوي(م.متوسط_رحلة("Leyton", "Waterloo"), 12.0, "بعد رحلة ثالثة")
# apl-source:66
