
# apl-source:1
# مثال 1636 — الرقم الموجب المفقود رقم ك
# apl-source:2
# Kth missing positive number
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1636-kth-missing-positive-number.apl
# apl-source:6

# apl-source:7
# عدد المفقود قبل الموضع = القيمة - الموضع - 1
# apl-source:8
# نبحث عن الموضع الذي يتجاوز ك
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
def المفقود_ك(أ, ك):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ)
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] - م - 1 < ك:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ج = م
  # apl-source:27
  return ي + ك
# apl-source:28

# apl-source:29
تأكد_يساوي(المفقود_ك([2, 3, 4, 7, 11], 5), 9, "خمسة")
# apl-source:30
تأكد_يساوي(المفقود_ك([1, 2, 3, 4], 2), 6, "بعد النهاية")
# apl-source:31
تأكد_يساوي(المفقود_ك([5], 1), 1, "قبل الأول")
# apl-source:32
