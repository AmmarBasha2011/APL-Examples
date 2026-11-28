
# apl-source:1
# مثال 880 — شفرة ليمير
# apl-source:2
# Lehmer code
# apl-source:3
# Demonstrates: ترقيم عاملي للتبديلات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/880-lehmer-code.apl
# apl-source:6

# apl-source:7
# شفرة ليمير: ترقيم التبديلات بالترقيم العاملي
# apl-source:8
# كل تبديل لـ n عنصراً له شفرة فريدة ورتبة بين 0 و n!-1
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
def شفرة_ليمير(تبديل):
  # apl-source:19
  شفرة = []
  # apl-source:20
  for i in range(len(تبديل)):
    # apl-source:21
    عد = 0
    # apl-source:22
    for ج in range(i + 1, len(تبديل)):
      # apl-source:23
      if تبديل[ج] < تبديل[i]:
        # apl-source:24
        عد = عد + 1
    # apl-source:25
    شفرة = شفرة + [عد]
  # apl-source:26
  return شفرة
# apl-source:27

# apl-source:28
def فك_ليمير(شفرة):
  # apl-source:29
  متاح = []
  # apl-source:30
  for i in range(len(شفرة)):
    # apl-source:31
    متاح = متاح + [i]
  # apl-source:32
  تبديل = []
  # apl-source:33
  for رقم in شفرة:
    # apl-source:34
    تبديل = تبديل + [متاح[رقم]]
    # apl-source:35
    متاح = متاح[:رقم] + متاح[رقم + 1:]
  # apl-source:36
  return تبديل
# apl-source:37

# apl-source:38
def رتبة_عاملية(شفرة):
  # apl-source:39
  رتبة = 0
  # apl-source:40
  ن = len(شفرة)
  # apl-source:41
  for i in range(ن):
    # apl-source:42
    مضروب = 1
    # apl-source:43
    for ك in range(1, ن - i):
      # apl-source:44
      مضروب = مضروب * ك
    # apl-source:45
    رتبة = رتبة + شفرة[i] * مضروب
  # apl-source:46
  return رتبة
# apl-source:47

# apl-source:48
شفرة = شفرة_ليمير([2, 0, 3, 1])
# apl-source:49
print("شفرة [2,0,3,1]:", شفرة)
# apl-source:50

# apl-source:51
تأكد_يساوي(شفرة[0], 2, "عنصران أصغر بعد 2")
# apl-source:52
تأكد_يساوي(شفرة[1], 0, "لا أصغر بعد 0")
# apl-source:53
تأكد_يساوي(شفرة[2], 1, "واحد أصغر بعد 3")
# apl-source:54

# apl-source:55
تبديل = فك_ليمير([2, 0, 1, 0])
# apl-source:56
print("الفك:", تبديل)
# apl-source:57
تأكد_يساوي(تبديل[0], 2, "الفك يعيد الأول")
# apl-source:58
تأكد_يساوي(تبديل[3], 1, "الفك يعيد الأخير")
# apl-source:59

# apl-source:60
رتبة = رتبة_عاملية(شفرة)
# apl-source:61
print("الرتبة:", رتبة)
# apl-source:62
تأكد_يساوي(رتبة, 13, "التبديل 13 من 24")
# apl-source:63
