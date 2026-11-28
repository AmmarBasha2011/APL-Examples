
# apl-source:1
# مثال 1219 — رقم مفرد من ثلاثة
# apl-source:2
# Single number appearing once among triples
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1219-single-number-two.apl
# apl-source:6

# apl-source:7
# نعد البتات في كل موضع
# apl-source:8
# ونأخذ باقي القسمة على ثلاثة
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
def مفرد(أ):
  # apl-source:19
  ناتج = 0
  # apl-source:20
  for ب in range(32):
    # apl-source:21
    عدد_ = 0
    # apl-source:22
    for س in أ:
      # apl-source:23
      if (س >> ب) & 1:
        # apl-source:24
        عدد_ = عدد_ + 1
    # apl-source:25
    if عدد_ % 3 == 1:
      # apl-source:26
      ناتج = ناتج | (1 << ب)
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(مفرد([2,2,3,2]), 3, "مثال أول")
# apl-source:30
تأكد_يساوي(مفرد([0,1,0,1,0,1,99]), 99, "مثال ثان")
# apl-source:31
تأكد_يساوي(مفرد([7]), 7, "واحد")
# apl-source:32
