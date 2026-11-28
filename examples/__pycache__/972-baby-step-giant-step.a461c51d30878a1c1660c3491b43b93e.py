
# apl-source:1
# مثال 972 — خطوة صغيرة وخطوة عملاقة
# apl-source:2
# Baby-step giant-step
# apl-source:3
# Demonstrates: جدول صغير وقفزات كبيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/972-baby-step-giant-step.apl
# apl-source:6

# apl-source:7
# خطوة صغيرة خطوة عملاقة: اللوغاريتم المنفصل في زمن جذر المرتبة
# apl-source:8
# نبحث عن س حيث ز^س تطابق هـ بترد ب
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
def جذر_صحيح(ن):
  # apl-source:19
  ك = 0
  # apl-source:20
  while ((ك + 1) * (ك + 1)) <= ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك
# apl-source:23

# apl-source:24
def قوة_مود(أ, هـ, م):
  # apl-source:25
  ناتج = 1
  # apl-source:26
  قاعدة = أ % م
  # apl-source:27
  باقي = هـ
  # apl-source:28
  while باقي > 0:
    # apl-source:29
    if (باقي % 2) == 1:
      # apl-source:30
      ناتج = (ناتج * قاعدة) % م
    # apl-source:31
    قاعدة = (قاعدة * قاعدة) % م
    # apl-source:32
    باقي = باقي // 2
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
def لوغاريتم_منفصل(ز, هـ, ب):
  # apl-source:36
  م = جذر_صحيح(ب) + 1
  # apl-source:37
  قيم = []
  # apl-source:38
  ط = 1
  # apl-source:39
  for ج in range(م):
    # apl-source:40
    قيم = قيم + [ط]
    # apl-source:41
    ط = (ط * ز) % ب
  # apl-source:42
  معامل = قوة_مود(ز, م * (ب - 2), ب)
  # apl-source:43
  ط = هـ
  # apl-source:44
  for i in range(م):
    # apl-source:45
    for ج in range(م):
      # apl-source:46
      if قيم[ج] == ط:
        # apl-source:47
        return (i * م) + ج
    # apl-source:48
    ط = (ط * معامل) % ب
  # apl-source:49
  return -1
# apl-source:50

# apl-source:51
س = لوغاريتم_منفصل(2, 28, 37)
# apl-source:52
تأكد_يساوي(س, 34, "الأس المطلوب")
# apl-source:53
تأكد_يساوي(قوة_مود(2, س, 37), 28, "التحقق بالرفع")
# apl-source:54
تأكد_يساوي(لوغاريتم_منفصل(2, 1, 37), 0, "الأس الصفري")
# apl-source:55
