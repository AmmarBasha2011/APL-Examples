
# apl-source:1
# مثال 669 — أقصى تدفق بفورد-فولكرسون
# apl-source:2
# Max-flow Ford-Fulkerson
# apl-source:3
# Demonstrates: تدفق أقصى، مسارات معززة، شبكة متبقية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/669-max-flow-ford-fulkerson.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# التدفق الأقصى: فورد-فلكرسون
# apl-source:25
# Demonstrates: شبكة سعات, مسار زيادة ببحث عرضي, حواف عكسية
# apl-source:26
# أكبر تدفق من المصدر إلى المصب يساوي سعة أصغر قطع
# apl-source:27

# apl-source:28
ن = 6
# apl-source:29
طاقة = [
  # apl-source:30
  [0, 16, 13, 0, 0, 0],
  # apl-source:31
  [0, 0, 0, 12, 0, 0],
  # apl-source:32
  [0, 4, 0, 0, 14, 0],
  # apl-source:33
  [0, 0, 9, 0, 0, 20],
  # apl-source:34
  [0, 0, 0, 7, 0, 4],
  # apl-source:35
  [0, 0, 0, 0, 0, 0],
# apl-source:36
]
# apl-source:37

# apl-source:38
def مسار_زيادة(بقايا, مصدر, مصب):
  # apl-source:39
  أب = []
  # apl-source:40
  for ي in range(ن):
    # apl-source:41
    أب.append(-1)
  # apl-source:42
  أب[مصدر] = مصدر
  # apl-source:43
  طابور = [مصدر]
  # apl-source:44
  رأس = 0
  # apl-source:45
  while رأس < len(طابور):
    # apl-source:46
    حالي = طابور[رأس]
    # apl-source:47
    رأس = رأس + 1
    # apl-source:48
    for جار in range(ن):
      # apl-source:49
      if أب[جار] == -1 and بقايا[حالي][جار] > 0:
        # apl-source:50
        أب[جار] = حالي
        # apl-source:51
        if جار == مصب:
          # apl-source:52
          طريق = []
          # apl-source:53
          ع = مصب
          # apl-source:54
          while ع != مصدر:
            # apl-source:55
            طريق.append(ع)
            # apl-source:56
            ع = أب[ع]
          # apl-source:57
          طريق.append(مصدر)
          # apl-source:58
          return طريق
        # apl-source:59
        طابور.append(جار)
  # apl-source:60
  return []
# apl-source:61

# apl-source:62
def تدفق_أقصى():
  # apl-source:63
  بقايا = []
  # apl-source:64
  for صف in طاقة:
    # apl-source:65
    بقايا.append(صف.copy())
  # apl-source:66
  تدفق = 0
  # apl-source:67
  while True:
    # apl-source:68
    طريق = مسار_زيادة(بقايا, 0, 5)
    # apl-source:69
    if len(طريق) == 0:
      # apl-source:70
      return تدفق
    # apl-source:71
    زيادة = 9999
    # apl-source:72
    for ي in range(len(طريق) - 1):
      # apl-source:73
      حافة = بقايا[طريق[ي + 1]][طريق[ي]]
      # apl-source:74
      if حافة < زيادة:
        # apl-source:75
        زيادة = حافة
    # apl-source:76
    for ي in range(len(طريق) - 1):
      # apl-source:77
      بقايا[طريق[ي + 1]][طريق[ي]] = بقايا[طريق[ي + 1]][طريق[ي]] - زيادة
      # apl-source:78
      بقايا[طريق[ي]][طريق[ي + 1]] = بقايا[طريق[ي]][طريق[ي + 1]] + زيادة
    # apl-source:79
    تدفق = تدفق + زيادة
# apl-source:80

# apl-source:81
تأكد_يساوي(تدفق_أقصى(), 23, "تدفق أقصى للشبكة الكلاسيكية")
# apl-source:82
print("التدفق الأقصى:", تدفق_أقصى())
# apl-source:83
