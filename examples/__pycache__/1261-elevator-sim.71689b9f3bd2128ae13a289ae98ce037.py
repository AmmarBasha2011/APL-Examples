
# apl-source:1
# مثال 1261 — محاكاة مصعد
# apl-source:2
# Elevator simulation
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1261-elevator-sim.apl
# apl-source:6

# apl-source:7
# المصعد يتحرك إلى أقرب طلب
# apl-source:8
# ونحسب مجموع الطوابق المقطوعة
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
def تشغيل(بداية, طلبات):
  # apl-source:19
  موقع = بداية
  # apl-source:20
  متبقية = list(طلبات)
  # apl-source:21
  مجموع = 0
  # apl-source:22
  ترتيب = []
  # apl-source:23
  while len(متبقية) > 0:
    # apl-source:24
    اقرب = 0
    # apl-source:25
    for ع in range(len(متبقية)):
      # apl-source:26
      if (متبقية[ع] - موقع) ** 2 < (متبقية[اقرب] - موقع) ** 2:
        # apl-source:27
        اقرب = ع
    # apl-source:28
    هدف = متبقية.pop(اقرب)
    # apl-source:29
    فرق = هدف - موقع
    # apl-source:30
    if فرق < 0:
      # apl-source:31
      فرق = -فرق
    # apl-source:32
    مجموع = مجموع + فرق
    # apl-source:33
    موقع = هدف
    # apl-source:34
    ترتيب = ترتيب + [هدف]
  # apl-source:35
  return [ترتيب, مجموع]
# apl-source:36

# apl-source:37
تأكد_يساوي(تشغيل(5, [3, 8, 4]), [[4, 3, 8], 7], "ثلاثة طلبات")
# apl-source:38
تأكد_يساوي(تشغيل(0, []), [[], 0], "لا طلبات")
# apl-source:39
تأكد_يساوي(تشغيل(1, [1]), [[1], 0], "نفس الطابق")
# apl-source:40
