
# apl-source:1
# مثال 1690 — هل العدد قوة للاثنين
# apl-source:2
# Is power of two by bit trick
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1690-is-power-of-two-bit.apl
# apl-source:6

# apl-source:7
# قوة الاثنين فيها بت واحد
# apl-source:8
# الطرح يقلب ذلك البت
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
def قوة_اثنين(ن):
  # apl-source:19
  if ن <= 0:
    # apl-source:20
    return False
  # apl-source:21
  return (ن & (ن - 1)) == 0
# apl-source:22

# apl-source:23
تأكد_يساوي(قوة_اثنين(1), True, "واحد")
# apl-source:24
تأكد_يساوي(قوة_اثنين(64), True, "أربعة وستون")
# apl-source:25
تأكد_يساوي(قوة_اثنين(12), False, "اثنا عشر")
# apl-source:26
تأكد_يساوي(قوة_اثنين(0), False, "صفر")
# apl-source:27
