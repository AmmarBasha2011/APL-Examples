
# apl-source:1
# مثال 980 — توافق زيلر
# apl-source:2
# Zeller congruence
# apl-source:3
# Demonstrates: معادلة على اليوم والقرن
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/980-zeller.apl
# apl-source:6

# apl-source:7
# توافق زيلر: حساب يوم الأسبوع لأي تاريخ ميلادي
# apl-source:8
# 0 سبت و1 أحد و2 اثنين حتى 6 جمعة
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
def يوم_أسبوع(يوم, شهر, سنة):
  # apl-source:19
  ش = شهر
  # apl-source:20
  س = سنة
  # apl-source:21
  if ش < 3:
    # apl-source:22
    ش = ش + 12
    # apl-source:23
    س = س - 1
  # apl-source:24
  ك = س % 100
  # apl-source:25
  قرن = س // 100
  # apl-source:26
  ح = (يوم + ((13 * (ش + 1)) // 5) + ك + (ك // 4) + (قرن // 4) + (5 * قرن)) % 7
  # apl-source:27
  return ح
# apl-source:28

# apl-source:29
تأكد_يساوي(يوم_أسبوع(1, 1, 2000), 0, "أول يناير 2000 سبت")
# apl-source:30
تأكد_يساوي(يوم_أسبوع(25, 11, 2026), 4, "25 نوفمبر 2026 أربعاء")
# apl-source:31
تأكد_يساوي(يوم_أسبوع(9, 9, 2000), 0, "9 سبتمبر 2000 سبت")
# apl-source:32
