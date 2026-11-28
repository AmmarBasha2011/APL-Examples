
# apl-source:1
# مثال 1746 — أقل عدد حلوى للأطفال
# apl-source:2
# Minimum candies by ratings
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1746-candy-distribution-min-total.apl
# apl-source:6

# apl-source:7
# مرور من اليسار ثم من اليمين
# apl-source:8
# نأخذ الأكبر من الشرطين
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
def حلوى(تقييم):
  # apl-source:19
  ن = len(تقييم)
  # apl-source:20
  ح = []
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    ح.append(1)
  # apl-source:23
  for ك in range(1, ن):
    # apl-source:24
    if تقييم[ك] > تقييم[ك - 1]:
      # apl-source:25
      ح[ك] = ح[ك - 1] + 1
  # apl-source:26
  for ك in range(ن - 2, -1, -1):
    # apl-source:27
    if تقييم[ك] > تقييم[ك + 1]:
      # apl-source:28
      ح[ك] = max(ح[ك], ح[ك + 1] + 1)
  # apl-source:29
  مجموع = 0
  # apl-source:30
  for ع in ح:
    # apl-source:31
    مجموع = مجموع + ع
  # apl-source:32
  return مجموع
# apl-source:33

# apl-source:34
تأكد_يساوي(حلوى([1, 0, 2]), 5, "ثلاثة")
# apl-source:35
تأكد_يساوي(حلوى([1, 2, 2]), 4, "متساوية")
# apl-source:36
تأكد_يساوي(حلوى([1]), 1, "طفل")
# apl-source:37
