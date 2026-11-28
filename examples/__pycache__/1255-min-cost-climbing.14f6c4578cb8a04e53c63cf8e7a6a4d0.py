
# apl-source:1
# مثال 1255 — كلفة الصعود
# apl-source:2
# Min cost climbing stairs
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1255-min-cost-climbing.apl
# apl-source:6

# apl-source:7
# نخطو درجة أو درجتين
# apl-source:8
# كلفة كل درجة ندفعها عند الدوس عليها
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
def اقل_كلفة(كلفة):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = 0
  # apl-source:21
  for ع in range(2, len(كلفة) + 1):
    # apl-source:22
    ج = min(ب + كلفة[ع - 1], أ + كلفة[ع - 2])
    # apl-source:23
    أ = ب
    # apl-source:24
    ب = ج
  # apl-source:25
  return ب
# apl-source:26

# apl-source:27
تأكد_يساوي(اقل_كلفة([10,15,20]), 15, "ثلاث درجات")
# apl-source:28
تأكد_يساوي(اقل_كلفة([1,100,1,1,1,100,1,1,100,1]), 6, "عشر درجات")
# apl-source:29
تأكد_يساوي(اقل_كلفة([5,5]), 5, "درجتان")
# apl-source:30
