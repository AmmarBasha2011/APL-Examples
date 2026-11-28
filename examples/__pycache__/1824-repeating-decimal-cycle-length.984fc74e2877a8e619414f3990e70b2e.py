
# apl-source:1
# مثال 1824 — طول دورة الكسر العشري
# apl-source:2
# Repeating decimal cycle length
# apl-source:3
# Demonstrates: حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1824-repeating-decimal-cycle-length.apl
# apl-source:6

# apl-source:7
# القسمة الطويلة تكرر باقياً
# apl-source:8
# المسافة بين التكرارين هي الدورة
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
def طول_الدورة(ب):
  # apl-source:19
  رأينا = {}
  # apl-source:20
  باقي = 1
  # apl-source:21
  خطوة = 0
  # apl-source:22
  while باقي != 0 and (str(باقي) in رأينا) == False:
    # apl-source:23
    رأينا[str(باقي)] = خطوة
    # apl-source:24
    باقي = (باقي * 10) % ب
    # apl-source:25
    خطوة = خطوة + 1
  # apl-source:26
  if باقي == 0:
    # apl-source:27
    return 0
  # apl-source:28
  return خطوة - رأينا[str(باقي)]
# apl-source:29

# apl-source:30
تأكد_يساوي(طول_الدورة(3), 1, "ثلث")
# apl-source:31
تأكد_يساوي(طول_الدورة(7), 6, "سبع")
# apl-source:32
تأكد_يساوي(طول_الدورة(4), 0, "ربع")
# apl-source:33
تأكد_يساوي(طول_الدورة(11), 2, "جزء من أحد عشر")
# apl-source:34
