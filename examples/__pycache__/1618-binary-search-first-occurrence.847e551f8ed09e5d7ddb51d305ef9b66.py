
# apl-source:1
# مثال 1618 — أول ظهور بالبحث الثنائي
# apl-source:2
# First occurrence by binary search
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1618-binary-search-first-occurrence.apl
# apl-source:6

# apl-source:7
# عند الإيجاد نسجل الموضع
# apl-source:8
# ثم نواصل البحث في النصف الأيسر
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
def أول_ظهور(أ, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ) - 1
  # apl-source:21
  نتيجة = -1
  # apl-source:22
  while ي <= ج:
    # apl-source:23
    م = (ي + ج) // 2
    # apl-source:24
    if أ[م] == هدف:
      # apl-source:25
      نتيجة = م
      # apl-source:26
      ج = م - 1
    # apl-source:27
    elif أ[م] < هدف:
      # apl-source:28
      ي = م + 1
    # apl-source:29
    else:
      # apl-source:30
      ج = م - 1
  # apl-source:31
  return نتيجة
# apl-source:32

# apl-source:33
تأكد_يساوي(أول_ظهور([1, 2, 2, 2, 3], 2), 1, "مكرر")
# apl-source:34
تأكد_يساوي(أول_ظهور([1, 3, 5], 4), -1, "غائب")
# apl-source:35
تأكد_يساوي(أول_ظهور([], 1), -1, "فارغة")
# apl-source:36
