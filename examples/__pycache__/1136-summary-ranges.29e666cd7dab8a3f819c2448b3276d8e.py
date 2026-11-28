
# apl-source:1
# مثال 1136 — ملخص المجالات
# apl-source:2
# Summary ranges
# apl-source:3
# Demonstrates: مسح خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1136-summary-ranges.apl
# apl-source:6

# apl-source:7
# نمر على القائمة المرتبة
# apl-source:8
# ونغلق المجال حين ينقطع التتابع
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
def ملخص(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  ع = 0
  # apl-source:21
  while ع < len(أ):
    # apl-source:22
    بداية = أ[ع]
    # apl-source:23
    while (ع + 1 < len(أ)) and (أ[ع + 1] == أ[ع] + 1):
      # apl-source:24
      ع = ع + 1
    # apl-source:25
    if أ[ع] == بداية:
      # apl-source:26
      ناتج = ناتج + [str(بداية)]
    # apl-source:27
    else:
      # apl-source:28
      ناتج = ناتج + [str(بداية) + "->" + str(أ[ع])]
    # apl-source:29
    ع = ع + 1
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(ملخص([0,1,2,4,5,7]), ["0->2", "4->5", "7"], "مثال أول")
# apl-source:33
تأكد_يساوي(ملخص([0,2,3,4,6,8,9]), ["0", "2->4", "6", "8->9"], "مثال ثان")
# apl-source:34
تأكد_يساوي(ملخص([]), [], "فارغة")
# apl-source:35
تأكد_يساوي(ملخص([5]), ["5"], "عنصر")
# apl-source:36
