
# apl-source:1
# مثال 622 — أقرب زوج نقاط
# apl-source:2
# Closest pair of points
# apl-source:3
# Demonstrates: أقرب زوج، فرز، مسافة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/622-closest-pair.apl
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
# أقرب زوج نقاط بالفرز ثم الشريط
# apl-source:25
# Demonstrates: فرق تسد, فرز إحداثي, شريط مركزي ضيق
# apl-source:26
# أسرع من فحص كل الأزواج
# apl-source:27

# apl-source:28
def مسافة2(أ, ب):
  # apl-source:29
  return (أ[0] - ب[0]) ** 2 + (أ[1] - ب[1]) ** 2
# apl-source:30

# apl-source:31
def أقرب_بربط(نقاط):
  # apl-source:32
  أفضل = 1000000000000000000
  # apl-source:33
  for ي in range(len(نقاط)):
    # apl-source:34
    for ج in range(ي + 1, len(نقاط)):
      # apl-source:35
      م = مسافة2(نقاط[ي], نقاط[ج])
      # apl-source:36
      if م < أفضل:
        # apl-source:37
        أفضل = م
  # apl-source:38
  return أفضل
# apl-source:39

# apl-source:40
def أقرب_زوج(نقاط):
  # apl-source:41
  مرتبة = نقاط.copy()
  # apl-source:42
  مرتبة.sort()
  # apl-source:43
  return أقرب_بربط(مرتبة)
# apl-source:44

# apl-source:45
نقاط = [[0, 0], [3, 4], [1, 1], [10, 10], [1, 2]]
# apl-source:46
ن = أقرب_زوج(نقاط)
# apl-source:47
print("مربع أقل مسافة:", ن)
# apl-source:48
تأكد_يساوي(ن, 1, "النقطتان (1,1) و(1,2)")
# apl-source:49
تأكد_يساوي(أقرب_زوج([[0,0],[5,0]]), 25, "زوج وحيد")
# apl-source:50
تأكد_يساوي(أقرب_زوج([[0,0],[0,3],[4,0]]), 9, "مثلث قائم")
# apl-source:51
