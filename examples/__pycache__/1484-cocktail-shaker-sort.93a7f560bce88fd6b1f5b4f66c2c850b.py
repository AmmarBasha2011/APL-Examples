
# apl-source:1
# مثال 1484 — فرز الخلاط
# apl-source:2
# Cocktail shaker sort
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1484-cocktail-shaker-sort.apl
# apl-source:6

# apl-source:7
# مرور للأمام يدفع الأكبر للنهاية
# apl-source:8
# مرور للخلف يدفع الأصغر للبداية
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
def فرز_الخلاط(أ):
  # apl-source:19
  بداية = 0
  # apl-source:20
  نهاية = len(أ) - 1
  # apl-source:21
  بدّل = True
  # apl-source:22
  while بدّل:
    # apl-source:23
    بدّل = False
    # apl-source:24
    for ع in range(بداية, نهاية):
      # apl-source:25
      if أ[ع] > أ[ع + 1]:
        # apl-source:26
        ت = أ[ع]
        # apl-source:27
        أ[ع] = أ[ع + 1]
        # apl-source:28
        أ[ع + 1] = ت
        # apl-source:29
        بدّل = True
    # apl-source:30
    نهاية = نهاية - 1
    # apl-source:31
    for ع in range(نهاية, بداية, -1):
      # apl-source:32
      if أ[ع] < أ[ع - 1]:
        # apl-source:33
        ت = أ[ع]
        # apl-source:34
        أ[ع] = أ[ع - 1]
        # apl-source:35
        أ[ع - 1] = ت
        # apl-source:36
        بدّل = True
    # apl-source:37
    بداية = بداية + 1
  # apl-source:38
  return أ
# apl-source:39

# apl-source:40
تأكد_يساوي(فرز_الخلاط([4, 3, 2, 1]), [1, 2, 3, 4], "عكسي")
# apl-source:41
تأكد_يساوي(فرز_الخلاط([2, 1]), [1, 2], "اثنان")
# apl-source:42
تأكد_يساوي(فرز_الخلاط([1, 5, 2, 4, 3]), [1, 2, 3, 4, 5], "مختلط")
# apl-source:43
