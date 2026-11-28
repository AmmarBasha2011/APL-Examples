
# apl-source:1
# مثال 1285 — متتالية جبلية
# apl-source:2
# Longest bitonic subsequence
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1285-bitonic-subsequence.apl
# apl-source:6

# apl-source:7
# نحسب أطول متزايدة تنتهي بكل موضع
# apl-source:8
# وأطول متناقصة تبدأ منه ونجمعهما
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
def اطول_جبلية(أ):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return 0
  # apl-source:22
  ز = [1] * ن
  # apl-source:23
  ن_ = [1] * ن
  # apl-source:24
  for ع in range(ن):
    # apl-source:25
    for ج in range(ع):
      # apl-source:26
      if (أ[ج] < أ[ع]) and (ز[ج] + 1 > ز[ع]):
        # apl-source:27
        ز[ع] = ز[ج] + 1
  # apl-source:28
  for ع in range(ن - 1, -1, -1):
    # apl-source:29
    for ج in range(ع + 1, ن):
      # apl-source:30
      if (أ[ج] < أ[ع]) and (ن_[ج] + 1 > ن_[ع]):
        # apl-source:31
        ن_[ع] = ن_[ج] + 1
  # apl-source:32
  اقصى = 0
  # apl-source:33
  for ع in range(ن):
    # apl-source:34
    if ز[ع] + ن_[ع] - 1 > اقصى:
      # apl-source:35
      اقصى = ز[ع] + ن_[ع] - 1
  # apl-source:36
  return اقصى
# apl-source:37

# apl-source:38
تأكد_يساوي(اطول_جبلية([1,11,2,10,4,5,2,1]), 6, "مثال أول")
# apl-source:39
تأكد_يساوي(اطول_جبلية([12,11,40,5,3,1]), 5, "مثال ثان")
# apl-source:40
تأكد_يساوي(اطول_جبلية([1,2,3]), 3, "تصاعدي")
# apl-source:41
