
# apl-source:1
# مثال 2317 — أقواس متوازنة
# apl-source:2
# Balanced round brackets
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2317-balanced-brackets-round-only.apl
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
  for ح in ن:
    # apl-source:21
    if ح == "(":
      # apl-source:22
      ع = ع + 1
    # apl-source:23
    elif ح == ")":
      # apl-source:24
      ع = ع - 1
      # apl-source:25
      if ع < 0:
        # apl-source:26
        return False
  # apl-source:27
  return ع == 0
# apl-source:28

# apl-source:29
تأكد_يساوي(ف("(())"), True, "حالة 1")
# apl-source:30
تأكد_يساوي(ف("(()"), False, "حالة 2")
# apl-source:31
تأكد_يساوي(ف("())("), False, "حالة 3")
# apl-source:32
تأكد_يساوي(ف(""), True, "حالة 4")
# apl-source:33
تأكد_يساوي(ف("()()"), True, "حالة 5")
# apl-source:34
