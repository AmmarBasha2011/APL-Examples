
# apl-source:1
# مثال 1971 — طرق صعود الدرج بخطوات ١ و٢ و٣
# apl-source:2
# Stair climbing with 1, 2 or 3 steps
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1971-stair-climb-ways-one-two-three.apl
# apl-source:6

# apl-source:7
# # نبدأ بـ 1 طريقة للصفر
# apl-source:8
# # ونجمع آخر ثلاث قيم في كل خطوة
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
def طرق(ن):
  # apl-source:19
  ط = [1]
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    مج = 0
    # apl-source:22
    for خ in [1, 2, 3]:
      # apl-source:23
      if ك - خ >= 0:
        # apl-source:24
        مج = مج + ط[ك - خ]
    # apl-source:25
    ط = ط + [مج]
  # apl-source:26
  return ط[ن]
# apl-source:27

# apl-source:28
تأكد_يساوي(طرق(0), 1, "صفر")
# apl-source:29
تأكد_يساوي(طرق(3), 4, "ثلاث")
# apl-source:30
تأكد_يساوي(طرق(5), 13, "خمس")
# apl-source:31
تأكد_يساوي(طرق(10), 274, "عشر")
# apl-source:32
