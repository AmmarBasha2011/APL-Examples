
# apl-source:1
# مثال 1910 — تحويل عدد عشري لأي أساس
# apl-source:2
# Convert decimal to any base
# apl-source:3
# Demonstrates: تحويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1910-decimal-to-any-base-string.apl
# apl-source:6

# apl-source:7
# الباقي هو الخانة الأخيرة
# apl-source:8
# نقسم حتى يصير العدد صفرا
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
def اساس(ن, ب):
  # apl-source:19
  رموز = "0123456789abcdef"
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return "0"
  # apl-source:22
  خرج = ""
  # apl-source:23
  while ن > 0:
    # apl-source:24
    خرج = رموز[ن % ب] + خرج
    # apl-source:25
    ن = ن // ب
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(اساس(10, 2), "1010", "ثنائي")
# apl-source:29
تأكد_يساوي(اساس(255, 16), "ff", "ست عشري")
# apl-source:30
تأكد_يساوي(اساس(0, 8), "0", "صفر")
# apl-source:31
تأكد_يساوي(اساس(64, 8), "100", "ثماني")
# apl-source:32
