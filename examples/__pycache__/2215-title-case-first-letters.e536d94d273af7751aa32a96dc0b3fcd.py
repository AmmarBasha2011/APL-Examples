
# apl-source:1
# مثال 2215 — أول حرف كبير لكل كلمة
# apl-source:2
# Capitalize each word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2215-title-case-first-letters.apl
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
  ك = []
  # apl-source:20
  for و2 in ن.split():
    # apl-source:21
    ك = ك + [chr(ord(و2[0]) - 32) + و2[1:]]
  # apl-source:22
  return " ".join(ك)
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("hello world"), "Hello World", "حالة 1")
# apl-source:25
تأكد_يساوي(ف("a b"), "A B", "حالة 2")
# apl-source:26
تأكد_يساوي(ف("python is fun"), "Python Is Fun", "حالة 3")
# apl-source:27
