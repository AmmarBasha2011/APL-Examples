
# apl-source:1
# مثال 2140 — عدد الكبيرة والصغيرة والأرقام
# apl-source:2
# Count upper lower digits
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2140-count-upper-lower-digit-characters.apl
# apl-source:6

# apl-source:7
# # نفحص كل حرف
# apl-source:8
# # ونرجع قائمة من ثلاثة أعداد
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
def عدادات(س):
  # apl-source:19
  ك = 0
  # apl-source:20
  ص = 0
  # apl-source:21
  ر = 0
  # apl-source:22
  for ح in س:
    # apl-source:23
    if ح.isupper():
      # apl-source:24
      ك = ك + 1
    # apl-source:25
    elif ح.islower():
      # apl-source:26
      ص = ص + 1
    # apl-source:27
    elif ح.isdigit():
      # apl-source:28
      ر = ر + 1
  # apl-source:29
  return [ك, ص, ر]
# apl-source:30

# apl-source:31
تأكد_يساوي(عدادات("Hello World 2026"), [2, 8, 4], "عبارة")
# apl-source:32
تأكد_يساوي(عدادات(""), [0, 0, 0], "فارغ")
# apl-source:33
