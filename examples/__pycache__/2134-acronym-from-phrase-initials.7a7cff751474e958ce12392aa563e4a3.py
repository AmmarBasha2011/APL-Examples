
# apl-source:1
# مثال 2134 — اختصار من أوائل الكلمات
# apl-source:2
# Acronym from initials
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2134-acronym-from-phrase-initials.apl
# apl-source:6

# apl-source:7
# # نقسم الجملة إلى كلمات
# apl-source:8
# # ونجمع الأحرف الأولى
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
def اختصار(س):
  # apl-source:19
  خرج = ""
  # apl-source:20
  for ك in س.split():
    # apl-source:21
    خرج = خرج + ك[0].upper()
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
تأكد_يساوي(اختصار("portable network graphics"), "PNG", "PNG")
# apl-source:25
تأكد_يساوي(اختصار("as soon as possible"), "ASAP", "ASAP")
# apl-source:26
تأكد_يساوي(اختصار(""), "", "فارغ")
# apl-source:27
