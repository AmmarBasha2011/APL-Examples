
# apl-source:1
# مثال 1097 — زراعة الزهور
# apl-source:2
# Can place flowers
# apl-source:3
# Demonstrates: فحص الجيران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1097-can-place-flowers.apl
# apl-source:6

# apl-source:7
# نزرع في أي موضع فارغ جيرانه فارغان أو حدود
# apl-source:8
# وكل زرع يغير حالة الجار التالي
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
def يمكن_زرع(ارض, ن):
  # apl-source:19
  ق = list(ارض)
  # apl-source:20
  عدد_ = 0
  # apl-source:21
  for ع in range(len(ق)):
    # apl-source:22
    if ق[ع] == 0:
      # apl-source:23
      يسار_فارغ = (ع == 0) or (ق[ع - 1] == 0)
      # apl-source:24
      يمين_فارغ = (ع == (len(ق) - 1)) or (ق[ع + 1] == 0)
      # apl-source:25
      if يسار_فارغ and يمين_فارغ:
        # apl-source:26
        ق[ع] = 1
        # apl-source:27
        عدد_ = عدد_ + 1
  # apl-source:28
  return عدد_ >= ن
# apl-source:29

# apl-source:30
تأكد_يساوي(يمكن_زرع([1, 0, 0, 0, 1], 1), True, "زهرة واحدة")
# apl-source:31
تأكد_يساوي(يمكن_زرع([1, 0, 0, 0, 1], 2), False, "زهرتان")
# apl-source:32
تأكد_يساوي(يمكن_زرع([0, 0, 1, 0, 0], 2), True, "الطرفان")
# apl-source:33
تأكد_يساوي(يمكن_زرع([0], 1), True, "خانة واحدة")
# apl-source:34
