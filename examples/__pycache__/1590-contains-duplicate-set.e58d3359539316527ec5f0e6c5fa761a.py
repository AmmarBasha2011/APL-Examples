
# apl-source:1
# مثال 1590 — هل فيها مكرر
# apl-source:2
# Contains duplicate
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1590-contains-duplicate-set.apl
# apl-source:6

# apl-source:7
# نخزن ما رأيناه
# apl-source:8
# إن رأينا العنصر مرتين نرجع صواباً
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
def فيها_مكرر(أ):
  # apl-source:19
  رأينا = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if ع in رأينا:
      # apl-source:22
      return True
    # apl-source:23
    رأينا[ع] = True
  # apl-source:24
  return False
# apl-source:25

# apl-source:26
تأكد_يساوي(فيها_مكرر([1, 2, 3, 1]), True, "مكرر")
# apl-source:27
تأكد_يساوي(فيها_مكرر([1, 2, 3]), False, "لا مكرر")
# apl-source:28
تأكد_يساوي(فيها_مكرر([]), False, "فارغة")
# apl-source:29
