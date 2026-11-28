
# apl-source:1
# مثال 705 — داتالوج مصغر
# apl-source:2
# Datalog lite
# apl-source:3
# Demonstrates: حقائق، قاعدة عودية، نقطة ثابتة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/705-datalog-lite.apl
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
# داتالوج مصغر: حقائق وقواعد وإغلاق
# apl-source:25
# Demonstrates: إغلاق متعدي, قاعدة عودية, نقطة ثابتة
# apl-source:26
# القاعدة: سلف(س, ص) :- والد(س, ص). سلف(س, ص) :- والد(س, ز)، سلف(ز, ص).
# apl-source:27

# apl-source:28
def أغلق(حقائق_والد):
  # apl-source:29
  سلف = []
  # apl-source:30
  for ح in حقائق_والد:
    # apl-source:31
    سلف.append(ح)
  # apl-source:32
  تغير = True
  # apl-source:33
  while تغير:
    # apl-source:34
    تغير = False
    # apl-source:35
    for ح1 in حقائق_والد:
      # apl-source:36
      for ح2 in سلف:
        # apl-source:37
        if ح1[1] == ح2[0] and ([ح1[0], ح2[1]] in سلف) == False:
          # apl-source:38
          سلف.append([ح1[0], ح2[1]])
          # apl-source:39
          تغير = True
  # apl-source:40
  return سلف
# apl-source:41

# apl-source:42
def عدد_أحفاد(سلف, شخص):
  # apl-source:43
  نسل = []
  # apl-source:44
  for ح in سلف:
    # apl-source:45
    if ح[0] == شخص and (ح[1] in نسل) == False:
      # apl-source:46
      نسل.append(ح[1])
  # apl-source:47
  return len(نسل)
# apl-source:48

# apl-source:49
والد = [["آدم", "بكر"], ["بكر", "جاد"], ["جاد", "داني"], ["آدم", "هشام"], ["هشام", "وليد"]]
# apl-source:50
سلف = أغلق(والد)
# apl-source:51
تأكد_يساوي(["آدم", "داني"] in سلف, True, "آدم سلف داني")
# apl-source:52
تأكد_يساوي(["بكر", "داني"] in سلف, True, "بكر سلف داني")
# apl-source:53
تأكد_يساوي(["هشام", "جاد"] in سلف, False, "هشام ليس سلف جاد")
# apl-source:54
تأكد_يساوي(عدد_أحفاد(سلف, "آدم"), 5, "لآدم خمسة أحفاد")
# apl-source:55
تأكد_يساوي(عدد_أحفاد(سلف, "بكر"), 2, "لبكر حفيدان")
# apl-source:56
تأكد_يساوي(عدد_أحفاد(سلف, "داني"), 0, "داني بلا أحفاد")
# apl-source:57
تأكد_يساوي(len(سلف), 9, "الإغلاق أضاف أربع علاقات")
# apl-source:58
print("علاقات السلف:", len(سلف))
# apl-source:59
