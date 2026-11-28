
# apl-source:1
# مثال 1794 — اسم عمود إكسل من رقمه
# apl-source:2
# Excel column title from number
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1794-excel-column-title-number.apl
# apl-source:6

# apl-source:7
# نطرح واحداً قبل كل قسمة
# apl-source:8
# الأحرف من A إلى Z
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
def عنوان_العمود(ن):
  # apl-source:19
  أبجد = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # apl-source:20
  ناتج = ""
  # apl-source:21
  while ن > 0:
    # apl-source:22
    ن = ن - 1
    # apl-source:23
    ناتج = أبجد[ن % 26] + ناتج
    # apl-source:24
    ن = ن // 26
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(عنوان_العمود(1), "A", "الأول")
# apl-source:28
تأكد_يساوي(عنوان_العمود(26), "Z", "السادس والعشرون")
# apl-source:29
تأكد_يساوي(عنوان_العمود(27), "AA", "السابع والعشرون")
# apl-source:30
تأكد_يساوي(عنوان_العمود(703), "AAA", "703")
# apl-source:31
