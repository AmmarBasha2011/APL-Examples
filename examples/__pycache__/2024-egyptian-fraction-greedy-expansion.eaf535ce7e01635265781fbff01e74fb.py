
# apl-source:1
# مثال 2024 — الكسور المصرية بالطريقة الجشعة
# apl-source:2
# Egyptian fraction greedy
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2024-egyptian-fraction-greedy-expansion.apl
# apl-source:6

# apl-source:7
# # المقام التالي هو سقف مقلوب الكسر
# apl-source:8
# # ونكرر حتى يصبح الباقي صفرا
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
def مصري(ب, م):
  # apl-source:19
  خرج = []
  # apl-source:20
  while ب != 0:
    # apl-source:21
    د = (م + ب - 1) // ب
    # apl-source:22
    خرج = خرج + [د]
    # apl-source:23
    ب = ب * د - م
    # apl-source:24
    م = م * د
  # apl-source:25
  return خرج
# apl-source:26

# apl-source:27
تأكد_يساوي(مصري(2, 3), [2, 6], "ثلثان")
# apl-source:28
تأكد_يساوي(مصري(4, 13), [4, 18, 468], "٤ على ١٣")
# apl-source:29
تأكد_يساوي(مصري(5, 6), [2, 3], "٥ على ٦")
# apl-source:30
