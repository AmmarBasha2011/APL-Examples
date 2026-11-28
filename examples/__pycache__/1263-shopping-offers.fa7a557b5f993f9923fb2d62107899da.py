
# apl-source:1
# مثال 1263 — عروض التسوق
# apl-source:2
# Shopping offers best price
# apl-source:3
# Demonstrates: استرجاع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1263-shopping-offers.apl
# apl-source:6

# apl-source:7
# الحالة هي كميات الأصناف المتبقية
# apl-source:8
# نجرب كل عرض يمكن تطبيقه ونحتفظ بالأقل
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
def اقل_سعر(اسعار, عروض, حاجات, ذاكرة):
  # apl-source:19
  مفتاح = str(حاجات)
  # apl-source:20
  if مفتاح in ذاكرة:
    # apl-source:21
    return ذاكرة[مفتاح]
  # apl-source:22
  افضل = 0
  # apl-source:23
  for ع in range(len(حاجات)):
    # apl-source:24
    افضل = افضل + اسعار[ع] * حاجات[ع]
  # apl-source:25
  for عرض in عروض:
    # apl-source:26
    جديد = list(حاجات)
    # apl-source:27
    ممكن = True
    # apl-source:28
    for ع in range(len(حاجات)):
      # apl-source:29
      جديد[ع] = جديد[ع] - عرض[ع]
      # apl-source:30
      if جديد[ع] < 0:
        # apl-source:31
        ممكن = False
    # apl-source:32
    if ممكن:
      # apl-source:33
      ق = عرض[-1] + اقل_سعر(اسعار, عروض, جديد, ذاكرة)
      # apl-source:34
      if ق < افضل:
        # apl-source:35
        افضل = ق
  # apl-source:36
  ذاكرة[مفتاح] = افضل
  # apl-source:37
  return افضل
# apl-source:38

# apl-source:39
تأكد_يساوي(اقل_سعر([2,5], [[3,0,5],[1,2,10]], [3,2], {}), 14, "مثال أول")
# apl-source:40
تأكد_يساوي(اقل_سعر([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1], {}), 11, "مثال ثان")
# apl-source:41
تأكد_يساوي(اقل_سعر([5], [], [2], {}), 10, "بلا عروض")
# apl-source:42
