
# apl-source:1
# مثال 4640 — الاحتفاظ بـ (رقم) في نص
# apl-source:2
# String: keep only digit
# apl-source:3
# Demonstrates: نصوص وحلقات وشروط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4640-string-keep-digit.apl
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
    if خ.isdigit():
      # apl-source:22
      ن = ن + خ
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("2026-11-28 launch"), "20261128", "حالة 1")
# apl-source:26
تأكد_يساوي(ف("ZZtop and the Beatles"), "", "حالة 2")
# apl-source:27
تأكد_يساوي(ف("a1b2c3d4"), "1234", "حالة 3")
# apl-source:28
تأكد_يساوي(ف("quick brown fox"), "", "حالة 4")
# apl-source:29
تأكد_يساوي(ف(""), "", "حالة 5")
# apl-source:30
