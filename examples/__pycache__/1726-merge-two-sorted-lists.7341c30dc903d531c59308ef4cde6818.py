
# apl-source:1
# مثال 1726 — دمج قائمتين مرتبتين
# apl-source:2
# Merge two sorted lists
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1726-merge-two-sorted-lists.apl
# apl-source:6

# apl-source:7
# مؤشر لكل قائمة
# apl-source:8
# نضيف الباقي في النهاية
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
def ادمج(أ, ب):
  # apl-source:19
  ي = 0
  # apl-source:20
  ك = 0
  # apl-source:21
  ناتج = []
  # apl-source:22
  while ي < len(أ) and ك < len(ب):
    # apl-source:23
    if أ[ي] <= ب[ك]:
      # apl-source:24
      ناتج.append(أ[ي])
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    else:
      # apl-source:27
      ناتج.append(ب[ك])
      # apl-source:28
      ك = ك + 1
  # apl-source:29
  while ي < len(أ):
    # apl-source:30
    ناتج.append(أ[ي])
    # apl-source:31
    ي = ي + 1
  # apl-source:32
  while ك < len(ب):
    # apl-source:33
    ناتج.append(ب[ك])
    # apl-source:34
    ك = ك + 1
  # apl-source:35
  return ناتج
# apl-source:36

# apl-source:37
تأكد_يساوي(ادمج([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "متداخلة")
# apl-source:38
تأكد_يساوي(ادمج([], [1]), [1], "فارغة")
# apl-source:39
تأكد_يساوي(ادمج([1, 1], [1]), [1, 1, 1], "متساوية")
# apl-source:40
