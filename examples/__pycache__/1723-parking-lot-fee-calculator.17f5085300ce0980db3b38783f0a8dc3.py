
# apl-source:1
# مثال 1723 — حساب أجرة الموقف
# apl-source:2
# Parking fee calculator
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1723-parking-lot-fee-calculator.apl
# apl-source:6

# apl-source:7
# نقرب الدقائق لأعلى ساعة
# apl-source:8
# الساعة الأولى لها سعر خاص
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
def أجرة(ساعات_دقيقة):
  # apl-source:19
  س = (ساعات_دقيقة + 59) // 60
  # apl-source:20
  if س <= 0:
    # apl-source:21
    return 0
  # apl-source:22
  if س == 1:
    # apl-source:23
    return 10
  # apl-source:24
  return 10 + (س - 1) * 6
# apl-source:25

# apl-source:26
تأكد_يساوي(أجرة(0), 0, "لا وقت")
# apl-source:27
تأكد_يساوي(أجرة(45), 10, "أقل من ساعة")
# apl-source:28
تأكد_يساوي(أجرة(61), 16, "ساعتان")
# apl-source:29
تأكد_يساوي(أجرة(180), 22, "ثلاث")
# apl-source:30
