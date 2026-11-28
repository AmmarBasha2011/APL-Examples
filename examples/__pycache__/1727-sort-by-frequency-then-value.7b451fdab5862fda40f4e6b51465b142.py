
# apl-source:1
# مثال 1727 — فرز حسب التكرار
# apl-source:2
# Sort numbers by frequency
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1727-sort-by-frequency-then-value.apl
# apl-source:6

# apl-source:7
# نعد التكرار بقاموس
# apl-source:8
# نبني مفتاح فرز من الزوج
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
def فرز_بالتكرار(ق):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    عد[str(ع)] = عد.get(str(ع), 0) + 1
  # apl-source:22
  أزواج = []
  # apl-source:23
  for ع in ق:
    # apl-source:24
    أزواج.append([1000 - عد[str(ع)], ع])
  # apl-source:25
  أزواج.sort()
  # apl-source:26
  ناتج = []
  # apl-source:27
  for ز in أزواج:
    # apl-source:28
    ناتج.append(ز[1])
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(فرز_بالتكرار([1, 1, 2, 2, 2, 3]), [2, 2, 2, 1, 1, 3], "ثلاثة")
# apl-source:32
تأكد_يساوي(فرز_بالتكرار([4, 5]), [4, 5], "تعادل")
# apl-source:33
