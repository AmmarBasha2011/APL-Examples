
# apl-source:1
# مثال 1007 — دمج قائمتين مرتبتين
# apl-source:2
# Merge two sorted arrays
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1007-merge-sorted-arrays.apl
# apl-source:6

# apl-source:7
# نقارن رأسي القائمتين ونأخذ الأصغر
# apl-source:8
# ثم نلحق ما بقي من القائمة الأخرى
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
  ن = []
  # apl-source:20
  ي = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  while (ي < len(أ)) and (ك < len(ب)):
    # apl-source:23
    if أ[ي] <= ب[ك]:
      # apl-source:24
      ن = ن + [أ[ي]]
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    else:
      # apl-source:27
      ن = ن + [ب[ك]]
      # apl-source:28
      ك = ك + 1
  # apl-source:29
  return ن + أ[ي:] + ب[ك:]
# apl-source:30

# apl-source:31
تأكد_يساوي(ادمج([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "تبادل")
# apl-source:32
تأكد_يساوي(ادمج([], [1, 2]), [1, 2], "أولى فارغة")
# apl-source:33
تأكد_يساوي(ادمج([1, 1], [1]), [1, 1, 1], "مكرر")
# apl-source:34
