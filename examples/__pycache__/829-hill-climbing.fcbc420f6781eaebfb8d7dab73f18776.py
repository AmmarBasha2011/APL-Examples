
# apl-source:1
# مثال 829 — تسلق التل
# apl-source:2
# Hill climbing
# apl-source:3
# Demonstrates: أفضل جار، قمم محلية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/829-hill-climbing.apl
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
# تسلق التل: تحسين محلي بالانتقال لأفضل جار حتى القمة
# apl-source:25
# Demonstrates: جوار بخطوة ثابتة, قمة محلية, إعادة تشغيل من نقاط مختلفة
# apl-source:26

# apl-source:27
def دالة_هدف(س):
  # apl-source:28
  return 0 - (س - 3) * (س - 3) + 10
# apl-source:29

# apl-source:30
def تسلق(بداية):
  # apl-source:31
  س = بداية
  # apl-source:32
  while 1 == 1:
    # apl-source:33
    أفضل = س
    # apl-source:34
    قيمة = دالة_هدف(س)
    # apl-source:35
    for جار in [س - 1, س + 1]:
      # apl-source:36
      if دالة_هدف(جار) > قيمة:
        # apl-source:37
        أفضل = جار
        # apl-source:38
        قيمة = دالة_هدف(جار)
    # apl-source:39
    if أفضل == س:
      # apl-source:40
      return [س, قيمة]
    # apl-source:41
    س = أفضل
# apl-source:42

# apl-source:43
تأكد_يساوي(تسلق(0), [3, 10], "من الصفر")
# apl-source:44
تأكد_يساوي(تسلق(7), [3, 10], "من السبعة")
# apl-source:45
تأكد_يساوي(تسلق(3), [3, 10], "من القمة نفسها")
# apl-source:46

# apl-source:47
def منظر(س):
  # apl-source:48
  if س < 6:
    # apl-source:49
    return 0 - (س - 3) * (س - 3) + 10
  # apl-source:50
  return 0 - (س - 12) * (س - 12) + 5
# apl-source:51

# apl-source:52
def تسلق2(بداية):
  # apl-source:53
  س = بداية
  # apl-source:54
  while 1 == 1:
    # apl-source:55
    أفضل = س
    # apl-source:56
    قيمة = منظر(س)
    # apl-source:57
    for جار in [س - 1, س + 1]:
      # apl-source:58
      if منظر(جار) > قيمة:
        # apl-source:59
        أفضل = جار
        # apl-source:60
        قيمة = منظر(جار)
    # apl-source:61
    if أفضل == س:
      # apl-source:62
      return [س, قيمة]
    # apl-source:63
    س = أفضل
# apl-source:64

# apl-source:65
تأكد_يساوي(تسلق2(0), [3, 10], "قمة أولى")
# apl-source:66
تأكد_يساوي(تسلق2(15), [12, 5], "قمة ثانية أدنى")
# apl-source:67
تأكد_يساوي(منظر(3) > منظر(12) == False, False, "القمة الأولى أعلى")
# apl-source:68
