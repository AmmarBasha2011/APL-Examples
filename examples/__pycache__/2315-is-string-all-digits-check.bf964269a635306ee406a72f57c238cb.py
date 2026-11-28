
# apl-source:1
# مثال 2315 — هل النص أرقام فقط
# apl-source:2
# Is all digits
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2315-is-string-all-digits-check.apl
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
  if ن == "":
    # apl-source:20
    return False
  # apl-source:21
  for ح in ن:
    # apl-source:22
    if ح.isdigit() == False:
      # apl-source:23
      return False
  # apl-source:24
  return True
# apl-source:25

# apl-source:26
تأكد_يساوي(ف("123"), True, "حالة 1")
# apl-source:27
تأكد_يساوي(ف("12a"), False, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(""), False, "حالة 3")
# apl-source:29
تأكد_يساوي(ف("007"), True, "حالة 4")
# apl-source:30
تأكد_يساوي(ف("1 2"), False, "حالة 5")
# apl-source:31
