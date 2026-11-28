
# apl-source:1
# مثال 1133 — تقسيم متساوٍ
# apl-source:2
# Partition equal subset sum
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1133-partition-equal-subset.apl
# apl-source:6

# apl-source:7
# لو كان المجموع فردياً فلا حل
# apl-source:8
# وإلا نبحث عن مجموعة جزئية مجموعها النصف
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
def يقسم(أ):
  # apl-source:19
  مج = 0
  # apl-source:20
  for س in أ:
    # apl-source:21
    مج = مج + س
  # apl-source:22
  if مج % 2 == 1:
    # apl-source:23
    return False
  # apl-source:24
  هدف = مج // 2
  # apl-source:25
  ممكن = [False] * (هدف + 1)
  # apl-source:26
  ممكن[0] = True
  # apl-source:27
  for س in أ:
    # apl-source:28
    for ك in range(هدف, س - 1, -1):
      # apl-source:29
      if ممكن[ك - س]:
        # apl-source:30
        ممكن[ك] = True
  # apl-source:31
  return ممكن[هدف]
# apl-source:32

# apl-source:33
تأكد_يساوي(يقسم([1,5,11,5]), True, "ممكن")
# apl-source:34
تأكد_يساوي(يقسم([1,2,3,5]), False, "غير ممكن")
# apl-source:35
تأكد_يساوي(يقسم([2,2]), True, "متساويان")
# apl-source:36
تأكد_يساوي(يقسم([1]), False, "واحد")
# apl-source:37
تأكد_يساوي(يقسم([3,3,3,4,5]), True, "خمسة")
# apl-source:38
