
# apl-source:1
# مثال 1486 — فرز ستوج
# apl-source:2
# Stooge sort
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1486-stooge-sort-recursive.apl
# apl-source:6

# apl-source:7
# نرتب الثلثين الأولين ثم الأخيرين
# apl-source:8
# ثم الأولين مرة أخرى
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
def ستوج(أ, ي, ن):
  # apl-source:19
  if أ[ي] > أ[ن]:
    # apl-source:20
    ت = أ[ي]
    # apl-source:21
    أ[ي] = أ[ن]
    # apl-source:22
    أ[ن] = ت
  # apl-source:23
  if ن - ي + 1 > 2:
    # apl-source:24
    ثلث = (ن - ي + 1) // 3
    # apl-source:25
    ستوج(أ, ي, ن - ثلث)
    # apl-source:26
    ستوج(أ, ي + ثلث, ن)
    # apl-source:27
    ستوج(أ, ي, ن - ثلث)
  # apl-source:28
  return أ
# apl-source:29

# apl-source:30
تأكد_يساوي(ستوج([5, 3, 1, 4, 2], 0, 4), [1, 2, 3, 4, 5], "خمسة")
# apl-source:31
تأكد_يساوي(ستوج([2, 1], 0, 1), [1, 2], "اثنان")
# apl-source:32
تأكد_يساوي(ستوج([9, 8, 7], 0, 2), [7, 8, 9], "ثلاثة")
# apl-source:33
