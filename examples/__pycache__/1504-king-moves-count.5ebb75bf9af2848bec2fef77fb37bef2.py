
# apl-source:1
# مثال 1504 — حركات الملك المتاحة
# apl-source:2
# Legal king moves on empty board
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1504-king-moves-count.apl
# apl-source:6

# apl-source:7
# كل الجيران الثمانية
# apl-source:8
# نستبعد من خرج عن الرقعة
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
def حركات_الملك(ص, ع):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ز_ص in [-1, 0, 1]:
    # apl-source:21
    for ز_ع in [-1, 0, 1]:
      # apl-source:22
      if ز_ص != 0 or ز_ع != 0:
        # apl-source:23
        ن_ص = ص + ز_ص
        # apl-source:24
        ن_ع = ع + ز_ع
        # apl-source:25
        if ن_ص >= 0 and ن_ص < 8 and ن_ع >= 0 and ن_ع < 8:
          # apl-source:26
          عد = عد + 1
  # apl-source:27
  return عد
# apl-source:28

# apl-source:29
تأكد_يساوي(حركات_الملك(0, 0), 3, "ركن")
# apl-source:30
تأكد_يساوي(حركات_الملك(0, 4), 5, "حافة")
# apl-source:31
تأكد_يساوي(حركات_الملك(4, 4), 8, "وسط")
# apl-source:32
