
# apl-source:1
# مثال 1961 — رقم اليوم في السنة
# apl-source:2
# Day of year with leap rule
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1961-day-of-year-with-leap-rule.apl
# apl-source:6

# apl-source:7
# # السنة كبيسة إن قبلت القسمة على 4 ولم تقبل على 100
# apl-source:8
# # إلا إذا قبلت القسمة على 400
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
def كبيسة(س):
  # apl-source:19
  return (س % 4 == 0 and س % 100 != 0) or س % 400 == 0
# apl-source:20

# apl-source:21
def يوم_السنة(س, ش, ي):
  # apl-source:22
  ايام = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:23
  if كبيسة(س):
    # apl-source:24
    ايام[1] = 29
  # apl-source:25
  مج = ي
  # apl-source:26
  for ك in range(ش - 1):
    # apl-source:27
    مج = مج + ايام[ك]
  # apl-source:28
  return مج
# apl-source:29

# apl-source:30
تأكد_يساوي(يوم_السنة(2023, 1, 1), 1, "أول يوم")
# apl-source:31
تأكد_يساوي(يوم_السنة(2023, 12, 31), 365, "آخر يوم")
# apl-source:32
تأكد_يساوي(يوم_السنة(2024, 12, 31), 366, "كبيسة")
# apl-source:33
تأكد_يساوي(يوم_السنة(1900, 3, 1), 60, "١٩٠٠ ليست كبيسة")
# apl-source:34
تأكد_يساوي(يوم_السنة(2000, 3, 1), 61, "٢٠٠٠ كبيسة")
# apl-source:35
