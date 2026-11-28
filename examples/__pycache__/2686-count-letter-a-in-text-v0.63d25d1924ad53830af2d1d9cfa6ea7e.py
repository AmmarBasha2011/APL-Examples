
# apl-source:1
# مثال 2686 — عدد الحرف a في النص
# apl-source:2
# Count letter a
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2686-count-letter-a-in-text-v0.apl
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
  return ن.count("a")
# apl-source:20

# apl-source:21
تأكد_يساوي(ف("elephant"), 1, "حالة 1")
# apl-source:22
تأكد_يساوي(ف("aaa"), 3, "حالة 2")
# apl-source:23
تأكد_يساوي(ف("status quo"), 1, "حالة 3")
# apl-source:24
تأكد_يساوي(ف("mississippi"), 0, "حالة 4")
# apl-source:25
