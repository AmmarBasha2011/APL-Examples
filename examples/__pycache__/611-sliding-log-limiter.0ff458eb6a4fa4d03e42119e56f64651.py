
# apl-source:1
# مثال 611 — تحديد معدل بسجل منزلق
# apl-source:2
# Sliding log rate limiter
# apl-source:3
# Demonstrates: معدل، سجل منزلق، طوابع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/611-sliding-log-limiter.apl
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
# تحديد المعدل بسجل منزلق: ن طلبات في نافذة زمنية
# apl-source:25
# Demonstrates: طوابع زمنية, إسقاط القديم, قرار سماح
# apl-source:26
# أدق من النافذة الثابتة لأنه يتذكر كل طلب
# apl-source:27

# apl-source:28
def أنشئ_محدد(سقف, نافذة):
  # apl-source:29
  return {"سقف": سقف, "نافذة": نافذة, "طوابع": []}
# apl-source:30

# apl-source:31
def اسمح(م, الآن):
  # apl-source:32
  قديم = الآن - م["نافذة"]
  # apl-source:33
  جديدة = []
  # apl-source:34
  for ط in م["طوابع"]:
    # apl-source:35
    if ط > قديم:
      # apl-source:36
      جديدة.append(ط)
  # apl-source:37
  م["طوابع"] = جديدة
  # apl-source:38
  if len(م["طوابع"]) < م["سقف"]:
    # apl-source:39
    م["طوابع"].append(الآن)
    # apl-source:40
    return True
  # apl-source:41
  return False
# apl-source:42

# apl-source:43
م = أنشئ_محدد(3, 10)
# apl-source:44
تأكد_يساوي(اسمح(م, 0), True, "طلب 1")
# apl-source:45
تأكد_يساوي(اسمح(م, 1), True, "طلب 2")
# apl-source:46
تأكد_يساوي(اسمح(م, 2), True, "طلب 3")
# apl-source:47
تأكد_يساوي(اسمح(م, 3), False, "طلب 4 مرفوض")
# apl-source:48
تأكد_يساوي(اسمح(م, 10), True, "سقوط أول طلب يسمح")
# apl-source:49
تأكد_يساوي(اسمح(م, 10), False, "الثالثة في النافذة مرفوضة")
# apl-source:50
print("طوابع مسجلة:", م["طوابع"])
# apl-source:51
