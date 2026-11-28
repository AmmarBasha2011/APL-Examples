
# apl-source:1
# مثال 1023 — تعبئة الصناديق
# apl-source:2
# Bin packing first fit decreasing
# apl-source:3
# Demonstrates: ترتيب تنازلي وأول ملاءمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1023-bin-packing-ffd.apl
# apl-source:6

# apl-source:7
# نرتب الأغراض من الأكبر للأصغر
# apl-source:8
# ونضع كل غرض في أول صندوق يتسع له وإلا فتحنا صندوقاً
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
def عبئ(اغراض, سعة):
  # apl-source:19
  مرتبة = list(اغراض)
  # apl-source:20
  مرتبة.sort()
  # apl-source:21
  مرتبة.reverse()
  # apl-source:22
  صناديق = []
  # apl-source:23
  for غ in مرتبة:
    # apl-source:24
    وضع = False
    # apl-source:25
    for ع in range(len(صناديق)):
      # apl-source:26
      if (وضع == False) and ((صناديق[ع] + غ) <= سعة):
        # apl-source:27
        صناديق[ع] = صناديق[ع] + غ
        # apl-source:28
        وضع = True
    # apl-source:29
    if وضع == False:
      # apl-source:30
      صناديق = صناديق + [غ]
  # apl-source:31
  return صناديق
# apl-source:32

# apl-source:33
تأكد_يساوي(len(عبئ([4, 8, 1, 4, 2, 1], 10)), 2, "صندوقان")
# apl-source:34
تأكد_يساوي(عبئ([5, 5, 5], 10), [10, 5], "ثلاثة أغراض")
# apl-source:35
تأكد_يساوي(len(عبئ([9, 9, 9], 10)), 3, "كل غرض وحده")
# apl-source:36
