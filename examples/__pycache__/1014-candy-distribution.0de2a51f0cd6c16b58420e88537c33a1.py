
# apl-source:1
# مثال 1014 — توزيع الحلوى
# apl-source:2
# Candy distribution
# apl-source:3
# Demonstrates: مرورتان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1014-candy-distribution.apl
# apl-source:6

# apl-source:7
# لكل طفل تقييم ومن تقييمه أعلى من جاره يأخذ حلوى أكثر
# apl-source:8
# مرور من اليسار ثم من اليمين يحقق الشرطين
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
def اقل_حلوى(تقييم):
  # apl-source:19
  ن = len(تقييم)
  # apl-source:20
  حلوى = [1] * ن
  # apl-source:21
  for ع in range(1, ن):
    # apl-source:22
    if تقييم[ع] > تقييم[ع - 1]:
      # apl-source:23
      حلوى[ع] = حلوى[ع - 1] + 1
  # apl-source:24
  for ع in range(ن - 2, -1, -1):
    # apl-source:25
    if (تقييم[ع] > تقييم[ع + 1]) and (حلوى[ع] <= حلوى[ع + 1]):
      # apl-source:26
      حلوى[ع] = حلوى[ع + 1] + 1
  # apl-source:27
  مجموع = 0
  # apl-source:28
  for ح in حلوى:
    # apl-source:29
    مجموع = مجموع + ح
  # apl-source:30
  return مجموع
# apl-source:31

# apl-source:32
تأكد_يساوي(اقل_حلوى([1, 0, 2]), 5, "ثلاثة أطفال")
# apl-source:33
تأكد_يساوي(اقل_حلوى([1, 2, 2]), 4, "تساوٍ")
# apl-source:34
تأكد_يساوي(اقل_حلوى([1, 2, 3, 4]), 10, "تصاعد")
# apl-source:35
