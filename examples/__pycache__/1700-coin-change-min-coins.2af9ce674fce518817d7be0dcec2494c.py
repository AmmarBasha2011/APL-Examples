
# apl-source:1
# مثال 1700 — أقل عدد عملات للمبلغ
# apl-source:2
# Minimum coins to make amount
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1700-coin-change-min-coins.apl
# apl-source:6

# apl-source:7
# أقل عدد لكل مبلغ
# apl-source:8
# نجرب كل عملة
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
def أقل_عملات(عملات, مبلغ):
  # apl-source:19
  كبير = مبلغ + 1
  # apl-source:20
  جدول = [0]
  # apl-source:21
  for ك in range(مبلغ):
    # apl-source:22
    جدول.append(كبير)
  # apl-source:23
  for م in range(1, مبلغ + 1):
    # apl-source:24
    for ع in عملات:
      # apl-source:25
      if ع <= م:
        # apl-source:26
        جدول[م] = min(جدول[م], جدول[م - ع] + 1)
  # apl-source:27
  if جدول[مبلغ] > مبلغ:
    # apl-source:28
    return -1
  # apl-source:29
  return جدول[مبلغ]
# apl-source:30

# apl-source:31
تأكد_يساوي(أقل_عملات([1, 2, 5], 11), 3, "أحد عشر")
# apl-source:32
تأكد_يساوي(أقل_عملات([2], 3), -1, "مستحيل")
# apl-source:33
تأكد_يساوي(أقل_عملات([1], 0), 0, "صفر")
# apl-source:34
