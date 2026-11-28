
# apl-source:1
# مثال 1379 — أقل تكلفة تذاكر
# apl-source:2
# Minimum cost for tickets
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1379-min-cost-tickets.apl
# apl-source:6

# apl-source:7
# لكل يوم سفر نختار أرخص تذكرة تنتهي فيه
# apl-source:8
# وبقية الأيام تأخذ كلفة اليوم السابق
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
def اقل_تذاكر(ايام, اسعار):
  # apl-source:19
  سفر = {}
  # apl-source:20
  for ي in ايام:
    # apl-source:21
    سفر[ي] = True
  # apl-source:22
  اخر = ايام[len(ايام) - 1]
  # apl-source:23
  د = [0] * (اخر + 1)
  # apl-source:24
  for ي in range(1, اخر + 1):
    # apl-source:25
    if ي not in سفر:
      # apl-source:26
      د[ي] = د[ي - 1]
    # apl-source:27
    else:
      # apl-source:28
      خيار1 = د[ي - 1] + اسعار[0]
      # apl-source:29
      خيار2 = د[max(0, ي - 7)] + اسعار[1]
      # apl-source:30
      خيار3 = د[max(0, ي - 30)] + اسعار[2]
      # apl-source:31
      د[ي] = min(خيار1, خيار2, خيار3)
  # apl-source:32
  return د[اخر]
# apl-source:33

# apl-source:34
تأكد_يساوي(اقل_تذاكر([1,4,6,7,8,20], [2,7,15]), 11, "أحد عشر")
# apl-source:35
تأكد_يساوي(اقل_تذاكر([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]), 17, "سبعة عشر")
# apl-source:36
تأكد_يساوي(اقل_تذاكر([5], [3,8,20]), 3, "يوم واحد")
# apl-source:37
