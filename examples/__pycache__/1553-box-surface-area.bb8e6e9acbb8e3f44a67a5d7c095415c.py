
# apl-source:1
# مثال 1553 — المساحة الكلية لصندوق
# apl-source:2
# Rectangular box surface area
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1553-box-surface-area.apl
# apl-source:6

# apl-source:7
# كل زوج من الأوجه مساحته متساوية
# apl-source:8
# نجمع الأزواج الثلاثة ونضاعف
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
def مساحة_الصندوق(ط, ع, ر):
  # apl-source:19
  return 2 * (ط * ع + ط * ر + ع * ر)
# apl-source:20

# apl-source:21
تأكد_يساوي(مساحة_الصندوق(1, 1, 1), 6, "مكعب")
# apl-source:22
تأكد_يساوي(مساحة_الصندوق(2, 3, 4), 52, "صندوق")
# apl-source:23
تأكد_يساوي(مساحة_الصندوق(5, 5, 1), 70, "لوح")
# apl-source:24
