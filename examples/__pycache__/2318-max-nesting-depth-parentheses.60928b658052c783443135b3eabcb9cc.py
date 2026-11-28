
# apl-source:1
# مثال 2318 — أقصى عمق للأقواس
# apl-source:2
# Max nesting depth
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2318-max-nesting-depth-parentheses.apl
# apl-source:6

# apl-source:7
# # ندخل النص
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  ع = 0
  # apl-source:20
  ك = 0
  # apl-source:21
  for ح in ن:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      ع = ع + 1
      # apl-source:24
      if ع > ك:
        # apl-source:25
        ك = ع
    # apl-source:26
    elif ح == ")":
      # apl-source:27
      ع = ع - 1
  # apl-source:28
  return ك
# apl-source:29

# apl-source:30
تأكد_يساوي(ف("(())"), 2, "حالة 1")
# apl-source:31
تأكد_يساوي(ف("()()"), 1, "حالة 2")
# apl-source:32
تأكد_يساوي(ف("((()))"), 3, "حالة 3")
# apl-source:33
تأكد_يساوي(ف("abc"), 0, "حالة 4")
# apl-source:34
تأكد_يساوي(ف("(a(b)(c(d)))"), 3, "حالة 5")
# apl-source:35
