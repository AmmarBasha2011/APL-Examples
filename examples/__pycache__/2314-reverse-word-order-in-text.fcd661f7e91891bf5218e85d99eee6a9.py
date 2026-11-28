
# apl-source:1
# مثال 2314 — عكس ترتيب الكلمات
# apl-source:2
# Reverse word order
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2314-reverse-word-order-in-text.apl
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
  ك = ن.split()
  # apl-source:20
  ك.reverse()
  # apl-source:21
  return " ".join(ك)
# apl-source:22

# apl-source:23
تأكد_يساوي(ف("hello world"), "world hello", "حالة 1")
# apl-source:24
تأكد_يساوي(ف("abc"), "abc", "حالة 2")
# apl-source:25
تأكد_يساوي(ف("a b c"), "c b a", "حالة 3")
# apl-source:26
تأكد_يساوي(ف("one two three four"), "four three two one", "حالة 4")
# apl-source:27
