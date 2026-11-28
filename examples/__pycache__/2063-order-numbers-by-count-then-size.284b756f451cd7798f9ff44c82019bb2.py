
# apl-source:1
# مثال 2063 — الفرز حسب التكرار ثم القيمة
# apl-source:2
# Sort by frequency then value
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2063-order-numbers-by-count-then-size.apl
# apl-source:6

# apl-source:7
# # نعد التكرار في قاموس
# apl-source:8
# # ونرتب أزواج التكرار والقيمة
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
def رتب(ق):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    عد[ع] = عد.get(ع, 0) + 1
  # apl-source:22
  ازواج = []
  # apl-source:23
  for ع in ق:
    # apl-source:24
    ازواج = ازواج + [[عد[ع], ع]]
  # apl-source:25
  ازواج = sorted(ازواج)
  # apl-source:26
  خرج = []
  # apl-source:27
  for ز in ازواج:
    # apl-source:28
    خرج = خرج + [ز[1]]
  # apl-source:29
  return خرج
# apl-source:30

# apl-source:31
تأكد_يساوي(رتب([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2], "ستة")
# apl-source:32
تأكد_يساوي(رتب([2, 3, 1, 3, 2]), [1, 2, 2, 3, 3], "خمسة")
# apl-source:33
تأكد_يساوي(رتب([]), [], "فارغة")
# apl-source:34
