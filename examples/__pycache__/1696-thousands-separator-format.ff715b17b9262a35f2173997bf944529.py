
# apl-source:1
# مثال 1696 — فاصل الآلاف
# apl-source:2
# Thousands separator formatting
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1696-thousands-separator-format.apl
# apl-source:6

# apl-source:7
# نمر على الأرقام من اليمين
# apl-source:8
# نضيف الفاصلة بعد كل ثلاثة
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
def بفواصل(ن):
  # apl-source:19
  س = str(ن)
  # apl-source:20
  ناتج = ""
  # apl-source:21
  عد = 0
  # apl-source:22
  for ك in range(len(س) - 1, -1, -1):
    # apl-source:23
    if عد > 0 and عد % 3 == 0:
      # apl-source:24
      ناتج = "," + ناتج
    # apl-source:25
    ناتج = س[ك] + ناتج
    # apl-source:26
    عد = عد + 1
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(بفواصل(1234567), "1,234,567", "ملايين")
# apl-source:30
تأكد_يساوي(بفواصل(999), "999", "ثلاثة")
# apl-source:31
تأكد_يساوي(بفواصل(1000), "1,000", "ألف")
# apl-source:32
