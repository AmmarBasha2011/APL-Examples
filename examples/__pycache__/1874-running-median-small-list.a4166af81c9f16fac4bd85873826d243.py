
# apl-source:1
# مثال 1874 — الوسيط المتتابع
# apl-source:2
# Running median of a stream
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1874-running-median-small-list.apl
# apl-source:6

# apl-source:7
# ندرج كل عنصر في موضعه
# apl-source:8
# نقرأ الوسيط من المنتصف
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
def وسيط_متتابع(ق):
  # apl-source:19
  مرتبة = []
  # apl-source:20
  نتائج = []
  # apl-source:21
  for ع in ق:
    # apl-source:22
    ي = 0
    # apl-source:23
    while ي < len(مرتبة) and مرتبة[ي] < ع:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    مرتبة.insert(ي, ع)
    # apl-source:26
    ن = len(مرتبة)
    # apl-source:27
    if ن % 2 == 1:
      # apl-source:28
      نتائج.append(مرتبة[ن // 2])
    # apl-source:29
    else:
      # apl-source:30
      نتائج.append((مرتبة[ن // 2 - 1] + مرتبة[ن // 2]) // 2)
  # apl-source:31
  return نتائج
# apl-source:32

# apl-source:33
تأكد_يساوي(وسيط_متتابع([5, 15, 1, 3]), [5, 10, 5, 4], "أربعة")
# apl-source:34
تأكد_يساوي(وسيط_متتابع([2]), [2], "واحد")
# apl-source:35
تأكد_يساوي(وسيط_متتابع([4, 4, 4]), [4, 4, 4], "متساوية")
# apl-source:36
