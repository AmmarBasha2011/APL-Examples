
# apl-source:1
# مثال 4638 — هل يوجد (حرف علة) في نص
# apl-source:2
# String: is there any vowel
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4638-string-anyq-vowel.apl
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
    if "aeiou".find(خ.lower()) != -1:
      # apl-source:21
      return True
  # apl-source:22
  return False
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("2026-11-28 launch"), True, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("MixedCASE123abc"), True, "حالة 2")
# apl-source:26
تأكد_يساوي(ف("  spaced   out  text "), True, "حالة 3")
# apl-source:27
تأكد_يساوي(ف("apple PIE 7 and 9"), True, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(""), False, "حالة 5")
# apl-source:29
