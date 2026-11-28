import queue
# apl-source:1
# مثال 1451 — طابور بخادم واحد
# apl-source:2
# Single server queue average wait
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1451-single-server-queue.apl
# apl-source:6

# apl-source:7
# لكل عميل وقت وصول ومدة خدمة
# apl-source:8
# يبدأ العميل عند الأكبر بين وصوله وانتهاء السابق
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
def متوسط_الانتظار(وصول, خدمة):
  # apl-source:19
  حر = 0
  # apl-source:20
  كل = 0
  # apl-source:21
  for ع in range(len(وصول)):
    # apl-source:22
    بداية = max(وصول[ع], حر)
    # apl-source:23
    كل = كل + (بداية - وصول[ع])
    # apl-source:24
    حر = بداية + خدمة[ع]
  # apl-source:25
  return كل / len(وصول)
# apl-source:26

# apl-source:27
تأكد_يساوي(متوسط_الانتظار([0, 1, 2], [3, 3, 3]), 2.0, "ثلاثة عملاء")
# apl-source:28
تأكد_يساوي(متوسط_الانتظار([0, 10], [2, 2]), 0.0, "بلا انتظار")
# apl-source:29
