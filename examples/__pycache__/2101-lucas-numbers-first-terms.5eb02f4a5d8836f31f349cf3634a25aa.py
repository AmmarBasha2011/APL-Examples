
# apl-source:1
# مثال 2101 — أعداد لوكاس
# apl-source:2
# Lucas numbers
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2101-lucas-numbers-first-terms.apl
# apl-source:6

# apl-source:7
# # تشبه فيبوناتشي ببداية مختلفة
# apl-source:8
# # نولد أول ن حدا
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
def لوكاس(ن):
  # apl-source:19
  ق = [2, 1]
  # apl-source:20
  for ك in range(2, ن):
    # apl-source:21
    ق = ق + [ق[ك - 1] + ق[ك - 2]]
  # apl-source:22
  return ق[:ن]
# apl-source:23

# apl-source:24
تأكد_يساوي(لوكاس(10), [2, 1, 3, 4, 7, 11, 18, 29, 47, 76], "عشرة")
# apl-source:25
تأكد_يساوي(لوكاس(1), [2], "واحد")
# apl-source:26
تأكد_يساوي(لوكاس(0), [], "صفر")
# apl-source:27
