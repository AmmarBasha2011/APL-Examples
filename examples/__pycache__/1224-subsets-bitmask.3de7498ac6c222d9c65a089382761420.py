
# apl-source:1
# مثال 1224 — مجموعات جزئية بالبتات
# apl-source:2
# Subsets using bitmask
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1224-subsets-bitmask.apl
# apl-source:6

# apl-source:7
# كل عدد من صفر إلى 2 أس n يمثل مجموعة
# apl-source:8
# البت المضبوط يعني أن العنصر موجود
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
def مجموعات(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for قناع in range(1 << len(أ)):
    # apl-source:21
    ق = []
    # apl-source:22
    for ع in range(len(أ)):
      # apl-source:23
      if (قناع >> ع) & 1:
        # apl-source:24
        ق = ق + [أ[ع]]
    # apl-source:25
    ناتج = ناتج + [ق]
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(مجموعات([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], "ثلاثة")
# apl-source:29
تأكد_يساوي(مجموعات([]), [[]], "فارغة")
# apl-source:30
تأكد_يساوي(len(مجموعات(list(range(10)))), 1024, "عشرة عناصر")
# apl-source:31
