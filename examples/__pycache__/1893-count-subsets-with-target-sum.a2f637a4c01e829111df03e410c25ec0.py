
# apl-source:1
# مثال 1893 — عدد المجموعات الجزئية بمجموع معين
# apl-source:2
# Count subsets with target sum
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1893-count-subsets-with-target-sum.apl
# apl-source:6

# apl-source:7
# عند كل عنصر فرعان: نأخذه أو لا
# apl-source:8
# نعد الفروع التي تصل للهدف
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
def عد_مجموعات(ق, ك, هدف):
  # apl-source:19
  if ك == len(ق):
    # apl-source:20
    if هدف == 0:
      # apl-source:21
      return 1
    # apl-source:22
    return 0
  # apl-source:23
  أخذ = عد_مجموعات(ق, ك + 1, هدف - ق[ك])
  # apl-source:24
  ترك = عد_مجموعات(ق, ك + 1, هدف)
  # apl-source:25
  return أخذ + ترك
# apl-source:26

# apl-source:27
تأكد_يساوي(عد_مجموعات([1, 2, 3, 4, 5], 0, 5), 3, "ثلاث مجموعات")
# apl-source:28
تأكد_يساوي(عد_مجموعات([2, 4], 0, 3), 0, "لا توجد")
# apl-source:29
تأكد_يساوي(عد_مجموعات([], 0, 0), 1, "الفارغة")
# apl-source:30
