
# apl-source:1
# مثال 2920 — اقتطاع أول 20 أحرف
# apl-source:2
# First 20 chars
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2920-truncate-text-to-first-20-chars.apl
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
  return ن[:20]
# apl-source:20

# apl-source:21
تأكد_يساوي(ف("hello world"), "hello world", "حالة 1")
# apl-source:22
تأكد_يساوي(ف("ab"), "ab", "حالة 2")
# apl-source:23
تأكد_يساوي(ف("abcdefghijkl"), "abcdefghijkl", "حالة 3")
# apl-source:24
تأكد_يساوي(ف(""), "", "حالة 4")
# apl-source:25
