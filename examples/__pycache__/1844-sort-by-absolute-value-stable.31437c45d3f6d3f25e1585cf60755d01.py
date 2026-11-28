
# apl-source:1
# مثال 1844 — فرز بالقيمة المطلقة
# apl-source:2
# Sort by absolute value
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1844-sort-by-absolute-value-stable.apl
# apl-source:6

# apl-source:7
# نبني مفتاحاً من القيمة المطلقة
# apl-source:8
# نعيد القيم الأصلية
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
def abs(ن):
  # apl-source:19
  if ن < 0:
    # apl-source:20
    return -ن
  # apl-source:21
  return ن
# apl-source:22

# apl-source:23
def افرز_مطلق(ق):
  # apl-source:24
  أزواج = []
  # apl-source:25
  for ع in ق:
    # apl-source:26
    أزواج.append([abs(ع), ع])
  # apl-source:27
  أزواج.sort()
  # apl-source:28
  ناتج = []
  # apl-source:29
  for ز in أزواج:
    # apl-source:30
    ناتج.append(ز[1])
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(افرز_مطلق([-4, 1, -2, 3]), [1, -2, 3, -4], "مختلط")
# apl-source:34
تأكد_يساوي(افرز_مطلق([2, -2]), [-2, 2], "تعادل")
# apl-source:35
تأكد_يساوي(افرز_مطلق([]), [], "فارغة")
# apl-source:36
