
# apl-source:1
# مثال 1813 — أطول بادئة مشتركة
# apl-source:2
# Longest common prefix
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1813-common-prefix-of-words.apl
# apl-source:6

# apl-source:7
# نأخذ الكلمة الأولى مرجعاً
# apl-source:8
# نتوقف عند أول اختلاف
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
  أول = كلمات[0]
  # apl-source:22
  for ك in range(len(أول)):
    # apl-source:23
    for ك_كلمة in كلمات:
      # apl-source:24
      if ك >= len(ك_كلمة):
        # apl-source:25
        return أول[:ك]
      # apl-source:26
      if ك_كلمة[ك] != أول[ك]:
        # apl-source:27
        return أول[:ك]
  # apl-source:28
  return أول
# apl-source:29

# apl-source:30
تأكد_يساوي(بادئة(["flower", "flow", "flight"]), "fl", "كلاسيكي")
# apl-source:31
تأكد_يساوي(بادئة(["dog", "car"]), "", "لا شيء")
# apl-source:32
تأكد_يساوي(بادئة(["abc"]), "abc", "كلمة")
# apl-source:33
