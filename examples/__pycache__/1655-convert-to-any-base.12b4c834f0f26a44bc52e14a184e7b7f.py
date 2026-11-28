
# apl-source:1
# مثال 1655 — تحويل إلى أي أساس
# apl-source:2
# Convert to any base up to 16
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1655-convert-to-any-base.apl
# apl-source:6

# apl-source:7
# نقسم على الأساس ونحفظ البواقي
# apl-source:8
# الأرقام فوق التسعة حروف
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
def بالأساس(ن, أساس):
  # apl-source:19
  رموز = "0123456789abcdef"
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return "0"
  # apl-source:22
  ناتج = ""
  # apl-source:23
  while ن > 0:
    # apl-source:24
    ناتج = رموز[ن % أساس] + ناتج
    # apl-source:25
    ن = ن // أساس
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(بالأساس(10, 2), "1010", "ثنائي")
# apl-source:29
تأكد_يساوي(بالأساس(255, 16), "ff", "سداسي عشري")
# apl-source:30
تأكد_يساوي(بالأساس(64, 8), "100", "ثماني")
# apl-source:31
تأكد_يساوي(بالأساس(0, 5), "0", "صفر")
# apl-source:32
