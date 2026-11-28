
# apl-source:1
# مثال 1545 — مدى القائمة
# apl-source:2
# Range of a list
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1545-range-of-list.apl
# apl-source:6

# apl-source:7
# نبحث عن الأكبر والأصغر معاً
# apl-source:8
# المدى الفارق بينهما
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
def المدى(أ):
  # apl-source:19
  صغرى = أ[0]
  # apl-source:20
  كبرى = أ[0]
  # apl-source:21
  for ع in أ:
    # apl-source:22
    if ع < صغرى:
      # apl-source:23
      صغرى = ع
    # apl-source:24
    if ع > كبرى:
      # apl-source:25
      كبرى = ع
  # apl-source:26
  return كبرى - صغرى
# apl-source:27

# apl-source:28
تأكد_يساوي(المدى([3, 9, 1, 7]), 8, "أربعة")
# apl-source:29
تأكد_يساوي(المدى([5]), 0, "وحيد")
# apl-source:30
تأكد_يساوي(المدى([-4, 4]), 8, "سالب")
# apl-source:31
