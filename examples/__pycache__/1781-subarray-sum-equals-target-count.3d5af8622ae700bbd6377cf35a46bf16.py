
# apl-source:1
# مثال 1781 — عدد المصفوفات الجزئية بمجموع معين
# apl-source:2
# Count subarrays with target sum
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1781-subarray-sum-equals-target-count.apl
# apl-source:6

# apl-source:7
# نخزن عدد مرات كل مجموع تراكمي
# apl-source:8
# نبحث عن المجموع ناقص الهدف
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
def عد_جزئية(ق, هدف):
  # apl-source:19
  رأينا = {"0": 1}
  # apl-source:20
  تراكمي = 0
  # apl-source:21
  عد = 0
  # apl-source:22
  for ع in ق:
    # apl-source:23
    تراكمي = تراكمي + ع
    # apl-source:24
    عد = عد + رأينا.get(str(تراكمي - هدف), 0)
    # apl-source:25
    رأينا[str(تراكمي)] = رأينا.get(str(تراكمي), 0) + 1
  # apl-source:26
  return عد
# apl-source:27

# apl-source:28
تأكد_يساوي(عد_جزئية([1, 1, 1], 2), 2, "اثنان")
# apl-source:29
تأكد_يساوي(عد_جزئية([1, 2, 3], 3), 2, "ثلاثة")
# apl-source:30
تأكد_يساوي(عد_جزئية([1, -1, 0], 0), 3, "أصفار")
# apl-source:31
