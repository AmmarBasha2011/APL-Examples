
# apl-source:1
# مثال 1797 — العدد الوحيد بالـ XOR
# apl-source:2
# Single number by XOR
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1797-single-number-xor-trick.apl
# apl-source:6

# apl-source:7
# x ^ x = 0
# apl-source:8
# x ^ 0 = x
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
def وحيد(ق):
  # apl-source:19
  ناتج = 0
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ناتج = ناتج ^ ع
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
تأكد_يساوي(وحيد([2, 2, 1]), 1, "ثلاثة")
# apl-source:25
تأكد_يساوي(وحيد([4, 1, 2, 1, 2]), 4, "خمسة")
# apl-source:26
تأكد_يساوي(وحيد([9]), 9, "واحد")
# apl-source:27
