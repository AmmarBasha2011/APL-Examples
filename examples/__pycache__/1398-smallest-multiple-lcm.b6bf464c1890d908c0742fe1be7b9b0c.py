
# apl-source:1
# مثال 1398 — أصغر مضاعف مشترك
# apl-source:2
# Smallest multiple of 1 to n
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1398-smallest-multiple-lcm.apl
# apl-source:6

# apl-source:7
# نحسب المضاعف المشترك الأصغر تراكمياً
# apl-source:8
# بالقاسم المشترك الأكبر
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
def قاسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = أ % ب
    # apl-source:21
    أ = ب
    # apl-source:22
    ب = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def اصغر_مضاعف(ن):
  # apl-source:26
  م = 1
  # apl-source:27
  for ع in range(2, ن + 1):
    # apl-source:28
    م = م * ع // قاسم(م, ع)
  # apl-source:29
  return م
# apl-source:30

# apl-source:31
تأكد_يساوي(اصغر_مضاعف(1), 1, "واحد")
# apl-source:32
تأكد_يساوي(اصغر_مضاعف(10), 2520, "عشرة")
# apl-source:33
تأكد_يساوي(اصغر_مضاعف(20), 232792560, "عشرون")
# apl-source:34
