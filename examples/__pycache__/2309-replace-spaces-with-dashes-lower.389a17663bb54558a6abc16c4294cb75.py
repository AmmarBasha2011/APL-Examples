
# apl-source:1
# مثال 2309 — مسافات إلى شرطات
# apl-source:2
# Spaces to dashes
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2309-replace-spaces-with-dashes-lower.apl
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
  return ن.lower().replace(" ", "-")
# apl-source:20

# apl-source:21
تأكد_يساوي(ف("Hello World"), "hello-world", "حالة 1")
# apl-source:22
تأكد_يساوي(ف("A B C"), "a-b-c", "حالة 2")
# apl-source:23
تأكد_يساوي(ف("one"), "one", "حالة 3")
# apl-source:24
تأكد_يساوي(ف("Big Data Set"), "big-data-set", "حالة 4")
# apl-source:25
