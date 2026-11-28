
# apl-source:1
# مثال 1934 — أطول بادئة مشتركة للكلمات
# apl-source:2
# Longest common prefix of words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1934-longest-common-prefix-of-words.apl
# apl-source:6

# apl-source:7
# نأخذ الكلمة الأولى كمرجع
# apl-source:8
# نقف عند أول اختلاف
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
def بادئة(كلمات):
  # apl-source:19
  if len(كلمات) == 0:
    # apl-source:20
    return ""
  # apl-source:21
  اول = كلمات[0]
  # apl-source:22
  for ك in range(len(اول)):
    # apl-source:23
    for و in كلمات:
      # apl-source:24
      if ك >= len(و) or و[ك] != اول[ك]:
        # apl-source:25
        return اول[0:ك]
  # apl-source:26
  return اول
# apl-source:27

# apl-source:28
تأكد_يساوي(بادئة(["flower", "flow", "flight"]), "fl", "fl")
# apl-source:29
تأكد_يساوي(بادئة(["dog", "car"]), "", "لا بادئة")
# apl-source:30
تأكد_يساوي(بادئة(["same", "same"]), "same", "متطابقة")
# apl-source:31
