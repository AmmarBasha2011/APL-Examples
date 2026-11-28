
# apl-source:1
# مثال 4971 — عدد العناصر القابلة للقسمة على 2
# apl-source:2
# Count items divisible by 2
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4971-count-divisible-2.apl
# apl-source:6

# apl-source:7
# نعد العناصر التي باقيها صفر
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
def ف(ق):
  # apl-source:18
  ع = 0
  # apl-source:19
  for خ in ق:
    # apl-source:20
    if خ % 2 == 0:
      # apl-source:21
      ع = ع + 1
  # apl-source:22
  return ع
# apl-source:23

# apl-source:24
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 24, "حالة 1")
# apl-source:25
تأكد_يساوي(ف([2, 4, 1]), 2, "حالة 2")
# apl-source:26
تأكد_يساوي(ف([]), 0, "حالة 3")
# apl-source:27
