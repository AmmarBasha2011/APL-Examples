
# apl-source:1
# مثال 1624 — الأرضية والسقف في قائمة مرتبة
# apl-source:2
# Floor and ceiling in a sorted list
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1624-floor-and-ceiling-sorted.apl
# apl-source:6

# apl-source:7
# الأرضية آخر عنصر أصغر أو يساوي
# apl-source:8
# السقف أول عنصر أكبر أو يساوي
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
def أرضية_وسقف(أ, هدف):
  # apl-source:19
  أرضية = -1
  # apl-source:20
  سقف = -1
  # apl-source:21
  ي = 0
  # apl-source:22
  ج = len(أ) - 1
  # apl-source:23
  while ي <= ج:
    # apl-source:24
    م = (ي + ج) // 2
    # apl-source:25
    if أ[م] <= هدف:
      # apl-source:26
      أرضية = أ[م]
      # apl-source:27
      ي = م + 1
    # apl-source:28
    else:
      # apl-source:29
      ج = م - 1
  # apl-source:30
  ي = 0
  # apl-source:31
  ج = len(أ) - 1
  # apl-source:32
  while ي <= ج:
    # apl-source:33
    م = (ي + ج) // 2
    # apl-source:34
    if أ[م] >= هدف:
      # apl-source:35
      سقف = أ[م]
      # apl-source:36
      ج = م - 1
    # apl-source:37
    else:
      # apl-source:38
      ي = م + 1
  # apl-source:39
  return [أرضية, سقف]
# apl-source:40

# apl-source:41
تأكد_يساوي(أرضية_وسقف([1, 3, 5, 7], 4), [3, 5], "بينهما")
# apl-source:42
تأكد_يساوي(أرضية_وسقف([1, 3, 5, 7], 5), [5, 5], "موجود")
# apl-source:43
تأكد_يساوي(أرضية_وسقف([1, 3], 0), [-1, 1], "قبل البداية")
# apl-source:44
