
# apl-source:1
# مثال 1498 — عدد المجموعات الجزئية بمجموع
# apl-source:2
# Count subsets with given sum
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1498-subset-sum-count.apl
# apl-source:6

# apl-source:7
# لكل عنصر خياران: نأخذه أو نتركه
# apl-source:8
# نعد الفروع التي تصل إلى الصفر
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
def عد_المجموعات(أ, ي, هدف):
  # apl-source:19
  if ي == len(أ):
    # apl-source:20
    if هدف == 0:
      # apl-source:21
      return 1
    # apl-source:22
    return 0
  # apl-source:23
  return عد_المجموعات(أ, ي + 1, هدف - أ[ي]) + عد_المجموعات(أ, ي + 1, هدف)
# apl-source:24

# apl-source:25
تأكد_يساوي(عد_المجموعات([1, 2, 3], 0, 3), 2, "اثنتان")
# apl-source:26
تأكد_يساوي(عد_المجموعات([1, 1, 1], 0, 2), 3, "ثلاث")
# apl-source:27
تأكد_يساوي(عد_المجموعات([5], 0, 3), 0, "لا توجد")
# apl-source:28
