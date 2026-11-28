
# apl-source:1
# مثال 1720 — محاكاة رصيد الحساب
# apl-source:2
# Bank account balance simulation
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1720-bank-account-balance-simulation.apl
# apl-source:6

# apl-source:7
# السحب الأكبر من الرصيد يُرفض
# apl-source:8
# نعد العمليات المرفوضة
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
def نفذ(عمليات):
  # apl-source:19
  رصيد = 0
  # apl-source:20
  مرفوض = 0
  # apl-source:21
  for ع in عمليات:
    # apl-source:22
    if ع[0] == "ايداع":
      # apl-source:23
      رصيد = رصيد + ع[1]
    # apl-source:24
    else:
      # apl-source:25
      if ع[1] > رصيد:
        # apl-source:26
        مرفوض = مرفوض + 1
      # apl-source:27
      else:
        # apl-source:28
        رصيد = رصيد - ع[1]
  # apl-source:29
  return [رصيد, مرفوض]
# apl-source:30

# apl-source:31
تأكد_يساوي(نفذ([["ايداع", 100], ["سحب", 30], ["سحب", 100]]), [70, 1], "رفض")
# apl-source:32
تأكد_يساوي(نفذ([]), [0, 0], "فارغ")
# apl-source:33
تأكد_يساوي(نفذ([["ايداع", 5], ["سحب", 5]]), [0, 0], "صفر")
# apl-source:34
