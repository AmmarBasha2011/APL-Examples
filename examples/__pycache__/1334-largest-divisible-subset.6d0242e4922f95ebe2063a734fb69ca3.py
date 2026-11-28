
# apl-source:1
# مثال 1334 — أكبر مجموعة قابلة للقسمة
# apl-source:2
# Largest divisible subset
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1334-largest-divisible-subset.apl
# apl-source:6

# apl-source:7
# نرتب الأرقام ثم نبني سلسلة القسمة
# apl-source:8
# نتتبع السابق لاسترجاع المجموعة
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
def اكبر_قسمة(أرقام):
  # apl-source:19
  if len(أرقام) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ر = sorted(أرقام)
  # apl-source:22
  ن = len(ر)
  # apl-source:23
  طول_ = [1] * ن
  # apl-source:24
  سابق = [-1] * ن
  # apl-source:25
  افضل = 0
  # apl-source:26
  for ع in range(ن):
    # apl-source:27
    for ج in range(ع):
      # apl-source:28
      if (ر[ع] % ر[ج] == 0) and (طول_[ج] + 1 > طول_[ع]):
        # apl-source:29
        طول_[ع] = طول_[ج] + 1
        # apl-source:30
        سابق[ع] = ج
    # apl-source:31
    if طول_[ع] > طول_[افضل]:
      # apl-source:32
      افضل = ع
  # apl-source:33
  ناتج = []
  # apl-source:34
  ع = افضل
  # apl-source:35
  while ع != -1:
    # apl-source:36
    ناتج = ناتج + [ر[ع]]
    # apl-source:37
    ع = سابق[ع]
  # apl-source:38
  ناتج.reverse()
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
تأكد_يساوي(اكبر_قسمة([1,2,3]), [1,2], "ثلاثة")
# apl-source:42
تأكد_يساوي(اكبر_قسمة([1,2,4,8]), [1,2,4,8], "قوى اثنين")
# apl-source:43
تأكد_يساوي(اكبر_قسمة([]), [], "فارغة")
# apl-source:44
