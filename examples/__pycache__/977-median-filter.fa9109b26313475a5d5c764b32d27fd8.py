
# apl-source:1
# مثال 977 — مرشح الوسيط
# apl-source:2
# Median filter
# apl-source:3
# Demonstrates: وسيط نافذة محلية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/977-median-filter.apl
# apl-source:6

# apl-source:7
# مرشح الوسيط: إزالة الارتفاعات المفاجئة من إشارة
# apl-source:8
# كل قيمة تُستبدل بوسيط نافذتها المحلية
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
def رتب(عناصر):
  # apl-source:19
  مرتبة = []
  # apl-source:20
  for س in عناصر:
    # apl-source:21
    وضع = len(مرتبة)
    # apl-source:22
    for ف in range(len(مرتبة)):
      # apl-source:23
      if (س < مرتبة[ف]) and (وضع == len(مرتبة)):
        # apl-source:24
        وضع = ف
    # apl-source:25
    مرتبة = مرتبة + [س]
    # apl-source:26
    for ج in range(len(مرتبة) - 1, وضع, -1):
      # apl-source:27
      مرتبة[ج] = مرتبة[ج - 1]
    # apl-source:28
    مرتبة[وضع] = س
  # apl-source:29
  return مرتبة
# apl-source:30

# apl-source:31
def مرشح_وسيط(إشارة):
  # apl-source:32
  ناتج = []
  # apl-source:33
  for i in range(len(إشارة)):
    # apl-source:34
    بداية = i - 1
    # apl-source:35
    if بداية < 0:
      # apl-source:36
      بداية = 0
    # apl-source:37
    نهاية = i + 2
    # apl-source:38
    if نهاية > len(إشارة):
      # apl-source:39
      نهاية = len(إشارة)
    # apl-source:40
    نافذة = رتب(إشارة[بداية:نهاية])
    # apl-source:41
    ناتج = ناتج + [نافذة[len(نافذة) // 2]]
  # apl-source:42
  return ناتج
# apl-source:43

# apl-source:44
ناتج = مرشح_وسيط([2, 80, 6, 3, 1])
# apl-source:45
تأكد_يساوي(len(ناتج), 5, "طول الناتج")
# apl-source:46
تأكد_يساوي(ناتج[1], 6, "إزالة الارتفاع المفاجئ")
# apl-source:47
تأكد_يساوي(ناتج[2], 6, "الوسيط الأوسط")
# apl-source:48
تأكد_يساوي(ناتج[3], 3, "الوسيط الرابع")
# apl-source:49
تأكد_يساوي(ناتج[4], 3, "حافة النهاية")
# apl-source:50
