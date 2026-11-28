
# apl-source:1
# مثال 1058 — طرق تجميع العملات
# apl-source:2
# Coin change number of ways
# apl-source:3
# Demonstrates: جدول طرق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1058-coin-change-ways.apl
# apl-source:6

# apl-source:7
# نمر على العملات واحدة واحدة فلا نعد الترتيب المختلف تركيبين
# apl-source:8
# طرق المبلغ تزيد بطرق المبلغ مطروحاً منه قيمة العملة
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
def طرق_المبلغ(مبلغ, عملات):
  # apl-source:19
  ط = [0] * (مبلغ + 1)
  # apl-source:20
  ط[0] = 1
  # apl-source:21
  for ع in عملات:
    # apl-source:22
    for م in range(ع, مبلغ + 1):
      # apl-source:23
      ط[م] = ط[م] + ط[م - ع]
  # apl-source:24
  return ط[مبلغ]
# apl-source:25

# apl-source:26
تأكد_يساوي(طرق_المبلغ(5, [1, 2, 5]), 4, "أربع طرق")
# apl-source:27
تأكد_يساوي(طرق_المبلغ(3, [2]), 0, "مستحيل")
# apl-source:28
تأكد_يساوي(طرق_المبلغ(10, [10]), 1, "عملة واحدة")
# apl-source:29
تأكد_يساوي(طرق_المبلغ(0, [7]), 1, "مبلغ صفر")
# apl-source:30
