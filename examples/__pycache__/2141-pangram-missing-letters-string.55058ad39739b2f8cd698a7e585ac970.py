
# apl-source:1
# مثال 2141 — الأحرف الناقصة لتصبح الجملة بانجرام
# apl-source:2
# Pangram missing letters
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2141-pangram-missing-letters-string.apl
# apl-source:6

# apl-source:7
# # نمر على الأبجدية
# apl-source:8
# # ونفحص وجود كل حرف
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
def ناقصة(س):
  # apl-source:19
  س = س.lower()
  # apl-source:20
  خرج = ""
  # apl-source:21
  for ح in "abcdefghijklmnopqrstuvwxyz":
    # apl-source:22
    if (ح in س) == False:
      # apl-source:23
      خرج = خرج + ح
  # apl-source:24
  return خرج
# apl-source:25

# apl-source:26
تأكد_يساوي(ناقصة("the quick brown fox"), "adgjlmpsvyz", "ناقصة")
# apl-source:27
تأكد_يساوي(ناقصة("The quick brown fox jumps over the lazy dog"), "", "كاملة")
# apl-source:28
