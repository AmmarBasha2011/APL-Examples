
# apl-source:1
# مثال 1948 — دفتر حساب بنكي مع رسوم السحب الزائد
# apl-source:2
# Bank ledger with overdraft fees
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1948-bank-overdraft-ledger-fees.apl
# apl-source:6

# apl-source:7
# # كل عملية سحب تجعل الرصيد سالبا تضيف رسما ثابتا
# apl-source:8
# # نرجع الرصيد النهائي وعدد الرسوم
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
def دفتر(رصيد, عمليات):
  # apl-source:19
  رسوم = 0
  # apl-source:20
  for ع in عمليات:
    # apl-source:21
    رصيد = رصيد + ع
    # apl-source:22
    if ع < 0 and رصيد < 0:
      # apl-source:23
      رصيد = رصيد - 15
      # apl-source:24
      رسوم = رسوم + 1
  # apl-source:25
  return [رصيد, رسوم]
# apl-source:26

# apl-source:27
تأكد_يساوي(دفتر(100, [-30, -50]), [20, 0], "بلا رسوم")
# apl-source:28
تأكد_يساوي(دفتر(50, [-80, 40, -100]), [-120, 2], "رسمان")
# apl-source:29
تأكد_يساوي(دفتر(0, []), [0, 0], "فارغ")
# apl-source:30
