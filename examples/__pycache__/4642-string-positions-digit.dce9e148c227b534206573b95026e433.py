
# apl-source:1
# مثال 4642 — مواضع (رقم) في نص
# apl-source:2
# String: positions of digit
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4642-string-positions-digit.apl
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
  ن = []
  # apl-source:20
  ر = 0
  # apl-source:21
  for خ in س:
    # apl-source:22
    if خ.isdigit():
      # apl-source:23
      ن = ن + [ر]
    # apl-source:24
    ر = ر + 1
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف("  spaced   out  text "), [], "حالة 1")
# apl-source:28
تأكد_يساوي(ف("a1b2c3d4"), [1, 3, 5, 7], "حالة 2")
# apl-source:29
تأكد_يساوي(ف("Data Science 101"), [13, 14, 15], "حالة 3")
# apl-source:30
تأكد_يساوي(ف("MixedCASE123abc"), [9, 10, 11], "حالة 4")
# apl-source:31
تأكد_يساوي(ف(""), [], "حالة 5")
# apl-source:32
