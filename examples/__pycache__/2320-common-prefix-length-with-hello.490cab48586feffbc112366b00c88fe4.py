
# apl-source:1
# مثال 2320 — طول البادئة المشتركة مع hello
# apl-source:2
# Common prefix with hello
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2320-common-prefix-length-with-hello.apl
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
  ه = "hello"
  # apl-source:20
  ع = 0
  # apl-source:21
  while ع < len(ن) and ع < len(ه) and ن[ع] == ه[ع]:
    # apl-source:22
    ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("help"), 3, "حالة 1")
# apl-source:26
تأكد_يساوي(ف("world"), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف("hello"), 5, "حالة 3")
# apl-source:28
تأكد_يساوي(ف("hell0"), 4, "حالة 4")
# apl-source:29
تأكد_يساوي(ف("he"), 2, "حالة 5")
# apl-source:30
