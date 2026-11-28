
# apl-source:1
# مثال 1156 — ترتيب بالتكرار
# apl-source:2
# Sort characters by frequency
# apl-source:3
# Demonstrates: عد وترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1156-sort-by-frequency.apl
# apl-source:6

# apl-source:7
# نعد تكرار كل حرف
# apl-source:8
# ونرتب تنازلياً بالتكرار ثم أبجدياً عند التساوي
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
def رتب_تكرار(س):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ح in س:
    # apl-source:21
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:22
  ازواج = []
  # apl-source:23
  for ح in عد:
    # apl-source:24
    ازواج = ازواج + [[-عد[ح], ح]]
  # apl-source:25
  ازواج = sorted(ازواج)
  # apl-source:26
  ناتج = ""
  # apl-source:27
  for ز in ازواج:
    # apl-source:28
    ناتج = ناتج + ز[1] * (-ز[0])
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(رتب_تكرار("tree"), "eert", "مثال أول")
# apl-source:32
تأكد_يساوي(رتب_تكرار("cccaaa"), "aaaccc", "تعادل")
# apl-source:33
تأكد_يساوي(رتب_تكرار("Aabb"), "bbAa", "حالة الأحرف")
# apl-source:34
تأكد_يساوي(رتب_تكرار(""), "", "فارغة")
# apl-source:35
