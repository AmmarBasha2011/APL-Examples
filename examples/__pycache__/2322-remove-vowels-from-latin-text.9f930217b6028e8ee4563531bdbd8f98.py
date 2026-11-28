
# apl-source:1
# مثال 2322 — حذف الحروف الصوتية
# apl-source:2
# Remove vowels
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2322-remove-vowels-from-latin-text.apl
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
  ر = ""
  # apl-source:20
  for ح in ن:
    # apl-source:21
    if "aeiouAEIOU".find(ح) == -1:
      # apl-source:22
      ر = ر + ح
  # apl-source:23
  return ر
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("hello"), "hll", "حالة 1")
# apl-source:26
تأكد_يساوي(ف("AEIOU"), "", "حالة 2")
# apl-source:27
تأكد_يساوي(ف("rhythm"), "rhythm", "حالة 3")
# apl-source:28
تأكد_يساوي(ف("Programming Language"), "Prgrmmng Lngg", "حالة 4")
# apl-source:29
