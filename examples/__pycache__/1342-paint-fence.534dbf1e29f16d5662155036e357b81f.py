
# apl-source:1
# مثال 1342 — طلاء السور
# apl-source:2
# Paint fence ways
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1342-paint-fence.apl
# apl-source:6

# apl-source:7
# نفرق بين نفس لون السابق ولون مختلف
# apl-source:8
# الجديد المختلف يساوي مجموع الحالتين في عدد الألوان ناقص واحد
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
def طرق_الطلاء(ن, ألوان):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return 0
  # apl-source:21
  if ن == 1:
    # apl-source:22
    return ألوان
  # apl-source:23
  نفس = ألوان
  # apl-source:24
  مختلف = ألوان * (ألوان - 1)
  # apl-source:25
  for ع in range(2, ن):
    # apl-source:26
    جديد_نفس = مختلف
    # apl-source:27
    جديد_مختلف = (نفس + مختلف) * (ألوان - 1)
    # apl-source:28
    نفس = جديد_نفس
    # apl-source:29
    مختلف = جديد_مختلف
  # apl-source:30
  return نفس + مختلف
# apl-source:31

# apl-source:32
تأكد_يساوي(طرق_الطلاء(3, 2), 6, "ثلاثة ألواح لونان")
# apl-source:33
تأكد_يساوي(طرق_الطلاء(1, 1), 1, "لوح")
# apl-source:34
تأكد_يساوي(طرق_الطلاء(7, 2), 42, "سبعة ألواح")
# apl-source:35
