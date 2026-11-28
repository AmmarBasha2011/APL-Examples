
# apl-source:1
# مثال 1388 — مجموع أقطار اللولب
# apl-source:2
# Number spiral diagonals sum
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1388-spiral-diagonals-sum.apl
# apl-source:6

# apl-source:7
# كل حلقة أضلاعها 2k زائد واحد
# apl-source:8
# الأركان الأربعة تحسب بصيغة مباشرة
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
def مجموع_الأقطار(ن):
  # apl-source:19
  مجموع = 1
  # apl-source:20
  for ك in range(1, (ن - 1) // 2 + 1):
    # apl-source:21
    ض = 2 * ك + 1
    # apl-source:22
    مجموع = مجموع + 4 * ض * ض - 6 * (ض - 1)
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
تأكد_يساوي(مجموع_الأقطار(1), 1, "واحد")
# apl-source:26
تأكد_يساوي(مجموع_الأقطار(5), 101, "خمسة")
# apl-source:27
تأكد_يساوي(مجموع_الأقطار(1001), 669171001, "ألف وواحد")
# apl-source:28
