
# apl-source:1
# مثال 1355 — زنازين بعد أيام
# apl-source:2
# Prison cells after N days
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1355-prison-cells-days.apl
# apl-source:6

# apl-source:7
# الحالة تتكرر بدورة طولها 14
# apl-source:8
# نقلص عدد الأيام ثم نحاكي
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
def يوم_تالي(خلايا):
  # apl-source:19
  جديد = [0] * 8
  # apl-source:20
  for ع in range(1, 7):
    # apl-source:21
    if خلايا[ع - 1] == خلايا[ع + 1]:
      # apl-source:22
      جديد[ع] = 1
  # apl-source:23
  return جديد
# apl-source:24

# apl-source:25
def بعد_ايام(خلايا, ايام):
  # apl-source:26
  حالي = خلايا[:]
  # apl-source:27
  if ايام > 0:
    # apl-source:28
    حالي = يوم_تالي(حالي)
    # apl-source:29
    ايام = ايام - 1
  # apl-source:30
  if ايام > 0:
    # apl-source:31
    ايام = ايام % 14
    # apl-source:32
    for خطوة in range(ايام):
      # apl-source:33
      حالي = يوم_تالي(حالي)
  # apl-source:34
  return حالي
# apl-source:35

# apl-source:36
تأكد_يساوي(بعد_ايام([0,1,0,1,1,0,0,1], 7), [0,0,1,1,0,0,0,0], "سبعة أيام")
# apl-source:37
تأكد_يساوي(بعد_ايام([1,0,0,1,0,0,1,0], 1000000000), [0,0,1,1,1,1,1,0], "مليار يوم")
# apl-source:38
تأكد_يساوي(بعد_ايام([1,1,1,1,1,1,1,1], 1), [0,1,1,1,1,1,1,0], "يوم واحد")
# apl-source:39
