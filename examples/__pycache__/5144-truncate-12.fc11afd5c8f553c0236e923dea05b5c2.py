
# apl-source:1
# مثال 5144 — اقتطاع النص إلى 12 حروف مع نقاط
# apl-source:2
# Truncate to 12 chars with dots
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5144-truncate-12.apl
# apl-source:6

# apl-source:7
# إذا زاد الطول نقتطع ونضيف ...
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  if len(ن) <= 12:
    # apl-source:19
    return ن
  # apl-source:20
  return ن[:12] + "..."
# apl-source:21

# apl-source:22
تأكد_يساوي(ف("hi"), "hi", "حالة 1")
# apl-source:23
تأكد_يساوي(ف("hello world, this is long"), "hello world,...", "حالة 2")
# apl-source:24
تأكد_يساوي(ف("xxxxxxxxxxxx"), "xxxxxxxxxxxx", "حالة 3")
# apl-source:25
تأكد_يساوي(ف("yyyyyyyyyyyyy"), "yyyyyyyyyyyy...", "حالة 4")
# apl-source:26
