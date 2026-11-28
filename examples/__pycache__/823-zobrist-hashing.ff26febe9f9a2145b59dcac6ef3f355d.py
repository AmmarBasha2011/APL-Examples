
# apl-source:1
# مثال 823 — تجزئة زوبريست
# apl-source:2
# Zobrist hashing
# apl-source:3
# Demonstrates: مفاتيح مربعات، XOR تزايدي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/823-zobrist-hashing.apl
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
# تجزئة زوبريست للوحات: مفتاح عشوائي لكل مربع وقطعة ودمج بXOR
# apl-source:25
# Demonstrates: جدول عشوائي حتمي, تحديث تزايدي, كشف تكرار الوضعيات
# apl-source:26

# apl-source:27
م64 = 18446744073709551616
# apl-source:28

# apl-source:29
def مولد_سبليت(بذرة, عدد):
  # apl-source:30
  قيم = []
  # apl-source:31
  س = بذرة
  # apl-source:32
  for ي in range(عدد):
    # apl-source:33
    س = (س + 11400714819323198485) % م64
    # apl-source:34
    ز = س
    # apl-source:35
    ز = ((ز ^ (ز >> 30)) * 13787848793156543929) % م64
    # apl-source:36
    ز = ((ز ^ (ز >> 27)) * 10723151780598845931) % م64
    # apl-source:37
    قيم.append(ز ^ (ز >> 31))
  # apl-source:38
  return قيم
# apl-source:39

# apl-source:40
عشوائي = مولد_سبليت(7, 18)
# apl-source:41

# apl-source:42
def مفتاح(مربع, قطعة):
  # apl-source:43
  return عشوائي[مربع * 2 + قطعة - 1]
# apl-source:44

# apl-source:45
def احسب(لوحة):
  # apl-source:46
  ه = 0
  # apl-source:47
  for ي in range(9):
    # apl-source:48
    if لوحة[ي] > 0:
      # apl-source:49
      ه = ه ^ مفتاح(ي, لوحة[ي])
  # apl-source:50
  return ه
# apl-source:51

# apl-source:52
تأكد_يساوي(احسب([0, 0, 0, 0, 0, 0, 0, 0, 0]), 0, "لوحة فارغة")
# apl-source:53
لوحة1 = [1, 0, 0, 0, 2, 0, 0, 0, 0]
# apl-source:54
لوحة2 = [1, 0, 0, 0, 2, 0, 0, 0, 1]
# apl-source:55
ه1 = احسب(لوحة1)
# apl-source:56
ه2 = احسب(لوحة2)
# apl-source:57
تأكد_يساوي(ه1, 722902038048628414, "تجزئة أولى")
# apl-source:58
تأكد_يساوي(ه2, 16944264263623018513, "تجزئة ثانية")
# apl-source:59
تأكد_يساوي(ه1 ^ مفتاح(8, 1), ه2, "تحديث تزايدي بإضافة")
# apl-source:60
تأكد_يساوي(ه2 ^ مفتاح(8, 1), ه1, "إزالة تعكس الإضافة")
# apl-source:61
