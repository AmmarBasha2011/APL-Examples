
# apl-source:1
# مثال 1900 — فواصل الآلاف في الأرقام
# apl-source:2
# Format number with thousands separators
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1900-format-thousands-separator.apl
# apl-source:6

# apl-source:7
# نحول الرقم لنص
# apl-source:8
# نضيف فاصلة قبل كل ثلاث خانات من اليمين
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
def فواصل(ن):
  # apl-source:19
  س = str(ن)
  # apl-source:20
  خرج = ""
  # apl-source:21
  for ك in range(len(س)):
    # apl-source:22
    باقي = len(س) - ك
    # apl-source:23
    if ك > 0 and باقي % 3 == 0:
      # apl-source:24
      خرج = خرج + ","
    # apl-source:25
    خرج = خرج + س[ك]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(فواصل(1234567), "1,234,567", "ملايين")
# apl-source:29
تأكد_يساوي(فواصل(999), "999", "بلا فاصلة")
# apl-source:30
تأكد_يساوي(فواصل(1000), "1,000", "ألف")
# apl-source:31
