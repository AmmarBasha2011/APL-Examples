
# apl-source:1
# مثال 1174 — وسيط قائمتين
# apl-source:2
# Median of two sorted lists
# apl-source:3
# Demonstrates: دمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1174-median-two-sorted.apl
# apl-source:6

# apl-source:7
# ندمج القائمتين بترتيب
# apl-source:8
# ونأخذ الوسيط من الناتج
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
def وسيط_قائمتين(أ, ب):
  # apl-source:32
  م = ادمج(أ, ب)
  # apl-source:33
  ع = len(م)
  # apl-source:34
  if ع % 2 == 1:
    # apl-source:35
    return م[ع // 2] * 1.0
  # apl-source:36
  return (م[ع // 2 - 1] + م[ع // 2]) / 2
# apl-source:37

# apl-source:38
تأكد_يساوي(وسيط_قائمتين([1,3], [2]), 2.0, "فردي")
# apl-source:39
تأكد_يساوي(وسيط_قائمتين([1,2], [3,4]), 2.5, "زوجي")
# apl-source:40
تأكد_يساوي(وسيط_قائمتين([], [1]), 1.0, "فارغة")
# apl-source:41
تأكد_يساوي(وسيط_قائمتين([0,0], [0,0]), 0.0, "أصفار")
# apl-source:42
