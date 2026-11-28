
# apl-source:1
# مثال 4655 — هل كل الأحرف (حرف كبير) في نص
# apl-source:2
# String: are all characters uppercase letter
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4655-string-allq-upper.apl
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
  for خ in س:
    # apl-source:20
    if not (خ.isupper()):
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("quick brown fox"), False, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("a1b2c3d4"), False, "حالة 2")
# apl-source:26
تأكد_يساوي(ف("aeiou AEIOU xyz"), False, "حالة 3")
# apl-source:27
تأكد_يساوي(ف("  spaced   out  text "), False, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(""), True, "حالة 5")
# apl-source:29
