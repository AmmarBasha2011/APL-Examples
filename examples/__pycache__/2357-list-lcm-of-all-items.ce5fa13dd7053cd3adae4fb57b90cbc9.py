
# apl-source:1
# مثال 2357 — المضاعف المشترك الأصغر للقائمة
# apl-source:2
# LCM of list
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2357-list-lcm-of-all-items.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ق2(أ, ب):
  # apl-source:19
  أ0 = أ
  # apl-source:20
  ب0 = ب
  # apl-source:21
  while ب != 0:
    # apl-source:22
    أ, ب = ب, أ % ب
  # apl-source:23
  return أ0 * ب0 // أ
# apl-source:24

# apl-source:25
def ف(ق):
  # apl-source:26
  م = ق[0]
  # apl-source:27
  for ع in ق:
    # apl-source:28
    م = ق2(م, ع)
  # apl-source:29
  return م
# apl-source:30

# apl-source:31
تأكد_يساوي(ف([4, 6]), 12, "حالة 1")
# apl-source:32
تأكد_يساوي(ف([5]), 5, "حالة 2")
# apl-source:33
تأكد_يساوي(ف([2, 3, 4]), 12, "حالة 3")
# apl-source:34
تأكد_يساوي(ف([3, 5, 7]), 105, "حالة 4")
# apl-source:35
