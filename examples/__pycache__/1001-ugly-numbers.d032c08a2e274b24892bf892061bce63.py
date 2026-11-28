
# apl-source:1
# مثال 1001 — الأعداد القبيحة
# apl-source:2
# Ugly numbers
# apl-source:3
# Demonstrates: ثلاثة مؤشرات تدمج متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1001-ugly-numbers.apl
# apl-source:6

# apl-source:7
# الأعداد القبيحة عواملها الأولية 2 و3 و5 فقط
# apl-source:8
# نولدها بالترتيب بثلاثة مؤشرات تدمج ضعف وثلاثة أضعاف وخمسة أضعاف
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
def قبيح(ن):
  # apl-source:19
  قائمة_ق = [1]
  # apl-source:20
  أ = 0
  # apl-source:21
  ب = 0
  # apl-source:22
  ج = 0
  # apl-source:23
  while len(قائمة_ق) < ن:
    # apl-source:24
    س2 = قائمة_ق[أ] * 2
    # apl-source:25
    س3 = قائمة_ق[ب] * 3
    # apl-source:26
    س5 = قائمة_ق[ج] * 5
    # apl-source:27
    ق = س2
    # apl-source:28
    if س3 < ق:
      # apl-source:29
      ق = س3
    # apl-source:30
    if س5 < ق:
      # apl-source:31
      ق = س5
    # apl-source:32
    if ق == س2:
      # apl-source:33
      أ = أ + 1
    # apl-source:34
    if ق == س3:
      # apl-source:35
      ب = ب + 1
    # apl-source:36
    if ق == س5:
      # apl-source:37
      ج = ج + 1
    # apl-source:38
    قائمة_ق = قائمة_ق + [ق]
  # apl-source:39
  return قائمة_ق
# apl-source:40

# apl-source:41
تأكد_يساوي(قبيح(10), [1, 2, 3, 4, 5, 6, 8, 9, 10, 12], "أول عشرة")
# apl-source:42
تأكد_يساوي(قبيح(15)[14], 24, "الخامس عشر")
# apl-source:43
تأكد_يساوي(قبيح(1), [1], "الأول فقط")
# apl-source:44
