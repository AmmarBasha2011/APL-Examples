
# apl-source:1
# مثال 1869 — أشهر سداد القرض
# apl-source:2
# Months to pay off a loan
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1869-loan-payoff-months-count.apl
# apl-source:6

# apl-source:7
# نضيف الفائدة ثم نخصم القسط
# apl-source:8
# نعد الأشهر حتى الصفر
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
def أشهر_السداد(مبلغ, فائدة_بالمئة, قسط):
  # apl-source:19
  أشهر = 0
  # apl-source:20
  while مبلغ > 0:
    # apl-source:21
    مبلغ = مبلغ + مبلغ * فائدة_بالمئة // 100
    # apl-source:22
    مبلغ = مبلغ - قسط
    # apl-source:23
    أشهر = أشهر + 1
  # apl-source:24
  return أشهر
# apl-source:25

# apl-source:26
تأكد_يساوي(أشهر_السداد(1000, 0, 100), 10, "بلا فائدة")
# apl-source:27
تأكد_يساوي(أشهر_السداد(100, 0, 100), 1, "شهر")
# apl-source:28
تأكد_يساوي(أشهر_السداد(1000, 10, 200), 8, "بفائدة")
# apl-source:29
