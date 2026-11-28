
# apl-source:1
# مثال 1825 — المتوسط المتحرك الصحيح
# apl-source:2
# Moving average with integer division
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1825-running-average-window-list.apl
# apl-source:6

# apl-source:7
# نحدث المجموع بإضافة وحذف
# apl-source:8
# القسمة صحيحة
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
def متوسط_متحرك(ق, ك):
  # apl-source:19
  ناتج = []
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ي in range(len(ق)):
    # apl-source:22
    مجموع = مجموع + ق[ي]
    # apl-source:23
    if ي >= ك:
      # apl-source:24
      مجموع = مجموع - ق[ي - ك]
    # apl-source:25
    if ي >= ك - 1:
      # apl-source:26
      ناتج.append(مجموع // ك)
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(متوسط_متحرك([1, 2, 3, 4, 5], 2), [1, 2, 3, 4], "نافذتان")
# apl-source:30
تأكد_يساوي(متوسط_متحرك([6, 6, 6], 3), [6], "كاملة")
# apl-source:31
تأكد_يساوي(متوسط_متحرك([10, 20], 1), [10, 20], "واحد")
# apl-source:32
