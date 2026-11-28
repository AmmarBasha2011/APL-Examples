
# apl-source:1
# مثال 1117 — امتداد سعر السهم
# apl-source:2
# Online stock span
# apl-source:3
# Demonstrates: مكدس أزواج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1117-stock-spanner.apl
# apl-source:6

# apl-source:7
# المكدس يحفظ السعر وامتداده
# apl-source:8
# كل سعر جديد يبتلع الأسعار الأقل أو المساوية ويجمع امتداداتها
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
class امتداد_السهم:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.مكدس = []
# apl-source:21

    # apl-source:22
    def سعر_جديد(ذات, سعر):
        # apl-source:23
        امتداد = 1
        # apl-source:24
        while (len(ذات.مكدس) > 0) and (ذات.مكدس[-1][0] <= سعر):
            # apl-source:25
            امتداد = امتداد + ذات.مكدس.pop()[1]
        # apl-source:26
        ذات.مكدس = ذات.مكدس + [[سعر, امتداد]]
        # apl-source:27
        return امتداد
# apl-source:28

# apl-source:29
س = امتداد_السهم()
# apl-source:30
نتائج = []
# apl-source:31
for ع in [100, 80, 60, 70, 60, 75, 85]:
    # apl-source:32
    نتائج = نتائج + [س.سعر_جديد(ع)]
# apl-source:33
تأكد_يساوي(نتائج, [1, 1, 1, 2, 1, 4, 6], "الامتدادات")
# apl-source:34
تأكد_يساوي(س.سعر_جديد(50), 1, "سعر أقل")
# apl-source:35
تأكد_يساوي(س.سعر_جديد(200), 9, "سعر أعلى من الكل")
# apl-source:36
