
# apl-source:1
# مثال 1790 — عدد مرات ظهور رقم في مدى
# apl-source:2
# Count digit occurrences in range
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1790-count-digit-occurrences-range.apl
# apl-source:6

# apl-source:7
# نفصل أرقام كل عدد
# apl-source:8
# نعد المطابق
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
def عد_الرقم(ن, ر):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    ع = ك
    # apl-source:22
    while ع > 0:
      # apl-source:23
      if ع % 10 == ر:
        # apl-source:24
        عد = عد + 1
      # apl-source:25
      ع = ع // 10
  # apl-source:26
  return عد
# apl-source:27

# apl-source:28
تأكد_يساوي(عد_الرقم(13, 1), 6, "واحد حتى ثلاثة عشر")
# apl-source:29
تأكد_يساوي(عد_الرقم(20, 2), 3, "اثنان")
# apl-source:30
تأكد_يساوي(عد_الرقم(9, 5), 1, "خمسة")
# apl-source:31
