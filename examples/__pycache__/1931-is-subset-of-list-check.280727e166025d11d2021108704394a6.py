
# apl-source:1
# مثال 1931 — هل القائمة جزء من أخرى
# apl-source:2
# Check whether one list is a subset of another
# apl-source:3
# Demonstrates: مجموعات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1931-is-subset-of-list-check.apl
# apl-source:6

# apl-source:7
# نمر على عناصر الصغرى
# apl-source:8
# نتوقف عند أول عنصر غائب
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
def جزء(صغرى, كبرى):
  # apl-source:19
  for ع in صغرى:
    # apl-source:20
    if (ع in كبرى) == False:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(جزء([1, 2], [1, 2, 3]), True, "جزء")
# apl-source:25
تأكد_يساوي(جزء([1, 4], [1, 2, 3]), False, "ليس جزءا")
# apl-source:26
تأكد_يساوي(جزء([], [1]), True, "فارغة")
# apl-source:27
