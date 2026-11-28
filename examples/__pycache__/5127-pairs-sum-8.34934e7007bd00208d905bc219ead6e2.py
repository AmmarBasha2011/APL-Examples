
# apl-source:1
# مثال 5127 — عدد الأزواج التي مجموعها 8
# apl-source:2
# Count pairs summing to 8
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5127-pairs-sum-8.apl
# apl-source:6

# apl-source:7
# نجرب كل زوج مرة واحدة
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ق):
  # apl-source:18
  ع = 0
  # apl-source:19
  for ي in range(len(ق)):
    # apl-source:20
    for ك in range(ي + 1, len(ق)):
      # apl-source:21
      if ق[ي] + ق[ك] == 8:
        # apl-source:22
        ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([0, 1, 2, 3, 4, 5, 6, 7, 8]), 4, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([1, 2, 3]), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([8, 0, 8]), 2, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([]), 0, "حالة 4")
# apl-source:29
