
# apl-source:1
# مثال 1530 — XOR التراكمي
# apl-source:2
# Prefix XOR array
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1530-prefix-xor-array.apl
# apl-source:6

# apl-source:7
# XOR عملية تجميعية
# apl-source:8
# النتيجة السابقة تكفي لحساب الحالية
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
def تراكمي_اكسور(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  جار = 0
  # apl-source:21
  for ع in أ:
    # apl-source:22
    جار = جار ^ ع
    # apl-source:23
    ناتج.append(جار)
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(تراكمي_اكسور([5, 2, 0, 3, 1]), [5, 7, 7, 4, 5], "خمسة")
# apl-source:27
تأكد_يساوي(تراكمي_اكسور([1, 1]), [1, 0], "يلغي نفسه")
# apl-source:28
