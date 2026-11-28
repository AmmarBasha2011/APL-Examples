
# apl-source:1
# مثال 1580 — رصيد دفتر الحساب
# apl-source:2
# Bank ledger balance
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1580-bank-ledger-balance.apl
# apl-source:6

# apl-source:7
# نقرأ العمليات بالترتيب
# apl-source:8
# السحب الأكبر من الرصيد يرفض ويستمر الباقي
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
def رصيد_نهائي(عمليات):
  # apl-source:19
  رصيد = 0
  # apl-source:20
  مرفوضة = 0
  # apl-source:21
  for ع in عمليات:
    # apl-source:22
    if ع[0] == "deposit":
      # apl-source:23
      رصيد = رصيد + ع[1]
    # apl-source:24
    elif ع[1] <= رصيد:
      # apl-source:25
      رصيد = رصيد - ع[1]
    # apl-source:26
    else:
      # apl-source:27
      مرفوضة = مرفوضة + 1
  # apl-source:28
  return [رصيد, مرفوضة]
# apl-source:29

# apl-source:30
تأكد_يساوي(رصيد_نهائي([["deposit", 100], ["withdraw", 30]]), [70, 0], "عادي")
# apl-source:31
تأكد_يساوي(رصيد_نهائي([["deposit", 50], ["withdraw", 80], ["withdraw", 20]]), [30, 1], "مرفوض")
# apl-source:32
تأكد_يساوي(رصيد_نهائي([]), [0, 0], "فارغ")
# apl-source:33
