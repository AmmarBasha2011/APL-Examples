
# apl-source:1
# مثال 635 — الساعات المتجهة
# apl-source:2
# Vector clocks
# apl-source:3
# Demonstrates: ساعة متجهة، تزامن، موزع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/635-vector-clock.apl
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
# الساعات المتجهة: ترتيب الأحداث في نظام موزع
# apl-source:25
# Demonstrates: عداد لكل عقدة, دمج بالأقصى, كشف التزامن
# apl-source:26
# حدثان متزامنان لا يسبق أحدهما الآخر
# apl-source:27

# apl-source:28
def ساعة_جديدة(عقد):
  # apl-source:29
  س = {}
  # apl-source:30
  for ع in عقد:
    # apl-source:31
    س[ع] = 0
  # apl-source:32
  return س
# apl-source:33

# apl-source:34
def حدث_محلي(س, عقدة):
  # apl-source:35
  س[عقدة] = س[عقدة] + 1
# apl-source:36

# apl-source:37
def ادمج(س1, س2):
  # apl-source:38
  for ع in س2:
    # apl-source:39
    if س2[ع] > س1[ع]:
      # apl-source:40
      س1[ع] = س2[ع]
# apl-source:41

# apl-source:42
def يسبق(س1, س2):
  # apl-source:43
  أصغر_أو_يساوي = True
  # apl-source:44
  أقل_مرة = False
  # apl-source:45
  for ع in س1:
    # apl-source:46
    if س1[ع] > س2[ع]:
      # apl-source:47
      أصغر_أو_يساوي = False
    # apl-source:48
    if س1[ع] < س2[ع]:
      # apl-source:49
      أقل_مرة = True
  # apl-source:50
  return أصغر_أو_يساوي and أقل_مرة
# apl-source:51

# apl-source:52
عقد = ["أ", "ب"]
# apl-source:53
سأ = ساعة_جديدة(عقد)
# apl-source:54
سب = ساعة_جديدة(عقد)
# apl-source:55
حدث_محلي(سأ, "أ")
# apl-source:56
حدث_محلي(سب, "ب")
# apl-source:57
تأكد_يساوي(يسبق(سأ, سب), False, "حدثان مستقلان متزامنان")
# apl-source:58
تأكد_يساوي(يسبق(سب, سأ), False, "لا أسبقية عكسية")
# apl-source:59
ادمج(سب, سأ)
# apl-source:60
حدث_محلي(سب, "ب")
# apl-source:61
تأكد_يساوي(يسبق(سأ, سب), True, "بعد الدمج أ يسبق ب")
# apl-source:62
print("ساعة ب:", سب)
# apl-source:63
