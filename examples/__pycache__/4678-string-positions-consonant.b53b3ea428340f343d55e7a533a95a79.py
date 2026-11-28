
# apl-source:1
# مثال 4678 — مواضع (حرف ساكن) في نص
# apl-source:2
# String: positions of consonant
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4678-string-positions-consonant.apl
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
    if ord(خ.lower()) >= 97 and ord(خ.lower()) <= 122 and "aeiou".find(خ.lower()) == -1:
      # apl-source:23
      ن = ن + [ر]
    # apl-source:24
    ر = ر + 1
  # apl-source:25
  return ن
# apl-source:26

# apl-source:27
تأكد_يساوي(ف("apple PIE 7 and 9"), [1, 2, 3, 6, 13, 14], "حالة 1")
# apl-source:28
تأكد_يساوي(ف("MixedCASE123abc"), [0, 2, 4, 5, 7, 13, 14], "حالة 2")
# apl-source:29
تأكد_يساوي(ف("aeiou AEIOU xyz"), [12, 13, 14], "حالة 3")
# apl-source:30
تأكد_يساوي(ف("Hello World 42"), [0, 2, 3, 6, 8, 9, 10], "حالة 4")
# apl-source:31
تأكد_يساوي(ف(""), [], "حالة 5")
# apl-source:32
