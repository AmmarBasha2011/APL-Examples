
# apl-source:1
# مثال 4631 — الاحتفاظ بـ (حرف علة) في نص
# apl-source:2
# String: keep only vowel
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4631-string-keep-vowel.apl
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
  ن = ""
  # apl-source:20
  for خ in س:
    # apl-source:21
    if "aeiou".find(خ.lower()) != -1:
      # apl-source:22
      ن = ن + خ
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("Hello World 42"), "eoo", "حالة 1")
# apl-source:26
تأكد_يساوي(ف("apple PIE 7 and 9"), "aeIEa", "حالة 2")
# apl-source:27
تأكد_يساوي(ف("ZZtop and the Beatles"), "oaeeae", "حالة 3")
# apl-source:28
تأكد_يساوي(ف("Data Science 101"), "aaiee", "حالة 4")
# apl-source:29
تأكد_يساوي(ف(""), "", "حالة 5")
# apl-source:30
