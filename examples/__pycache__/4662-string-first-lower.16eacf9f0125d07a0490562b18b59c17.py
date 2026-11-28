
# apl-source:1
# مثال 4662 — أول موضع (حرف صغير) في نص
# apl-source:2
# String: first position of lowercase letter
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4662-string-first-lower.apl
# apl-source:6

# apl-source:7
# نمرّ على حروف النص واحدًا واحدًا
# apl-source:8
# ونطبّق الشرط على كل حرف
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
def ف(س):
  # apl-source:19
  ر = 0
  # apl-source:20
  for خ in س:
    # apl-source:21
    if خ.islower():
      # apl-source:22
      return ر
    # apl-source:23
    ر = ر + 1
  # apl-source:24
  return -1
# apl-source:25

# apl-source:26
تأكد_يساوي(ف("a1b2c3d4"), 0, "حالة 1")
# apl-source:27
تأكد_يساوي(ف("Data Science 101"), 1, "حالة 2")
# apl-source:28
تأكد_يساوي(ف("quick brown fox"), 0, "حالة 3")
# apl-source:29
تأكد_يساوي(ف("aeiou AEIOU xyz"), 0, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(""), -1, "حالة 5")
# apl-source:31
