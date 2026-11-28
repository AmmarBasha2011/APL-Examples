
# apl-source:1
# مثال 1016 — درجات الحرارة اليومية
# apl-source:2
# Daily temperatures
# apl-source:3
# Demonstrates: مكدس رتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1016-daily-temperatures.apl
# apl-source:6

# apl-source:7
# مكدس يحفظ فهارس أيام لم يأت بعدها يوم أدفأ
# apl-source:8
# كل يوم أدفأ يغلق الأيام الأبرد على قمة المكدس
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
def ايام_للدفء(حرارة):
  # apl-source:19
  جواب = [0] * len(حرارة)
  # apl-source:20
  مكدس = []
  # apl-source:21
  for ع in range(len(حرارة)):
    # apl-source:22
    while (len(مكدس) > 0) and (حرارة[ع] > حرارة[مكدس[len(مكدس) - 1]]):
      # apl-source:23
      ق = مكدس.pop()
      # apl-source:24
      جواب[ق] = ع - ق
    # apl-source:25
    مكدس = مكدس + [ع]
  # apl-source:26
  return جواب
# apl-source:27

# apl-source:28
تأكد_يساوي(ايام_للدفء([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0], "أسبوع")
# apl-source:29
تأكد_يساوي(ايام_للدفء([30, 40, 50, 60]), [1, 1, 1, 0], "تصاعد")
# apl-source:30
تأكد_يساوي(ايام_للدفء([30, 20, 10]), [0, 0, 0], "هبوط")
# apl-source:31
