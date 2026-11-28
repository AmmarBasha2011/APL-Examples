
# apl-source:1
# مثال 621 — الغلاف المحدب
# apl-source:2
# Convex hull (Graham scan)
# apl-source:3
# Demonstrates: غلاف محدب، فرز قطبي، مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/621-convex-hull-graham.apl
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
# الغلاف المحدب بمسح جراهام
# apl-source:25
# Demonstrates: فرز قطبي, اختبار اتجاه, مكدس الغلاف
# apl-source:26
# أصغر مضلع محدب يحوي كل النقاط
# apl-source:27

# apl-source:28
def اتجاه(ن1, ن2, ن3):
  # apl-source:29
  return (ن2[0] - ن1[0]) * (ن3[1] - ن1[1]) - (ن2[1] - ن1[1]) * (ن3[0] - ن1[0])
# apl-source:30

# apl-source:31
def غلاف_محدب(نقاط):
  # apl-source:32
  مرتبة = نقاط.copy()
  # apl-source:33
  مرتبة.sort()
  # apl-source:34
  أسفل = []
  # apl-source:35
  for ن in مرتبة:
    # apl-source:36
    while len(أسفل) >= 2 and اتجاه(أسفل[-2], أسفل[-1], ن) <= 0:
      # apl-source:37
      أسفل.pop()
    # apl-source:38
    أسفل.append(ن)
  # apl-source:39
  أعلى = []
  # apl-source:40
  for ن in مرتبة:
    # apl-source:41
    while len(أعلى) >= 2 and اتجاه(أعلى[-2], أعلى[-1], ن) >= 0:
      # apl-source:42
      أعلى.pop()
    # apl-source:43
    أعلى.append(ن)
  # apl-source:44
  أسفل.pop()
  # apl-source:45
  أعلى.pop()
  # apl-source:46
  return len(أسفل) + len(أعلى)
# apl-source:47

# apl-source:48
نقاط = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
# apl-source:49
print("رؤوس الغلاف:", غلاف_محدب(نقاط))
# apl-source:50
تأكد_يساوي(غلاف_محدب(نقاط), 4, "شبكة 3x3 غلافها مربع")
# apl-source:51
تأكد_يساوي(غلاف_محدب([[0,0],[2,0],[1,1]]), 3, "مثلث")
# apl-source:52
تأكد_يساوي(غلاف_محدب([[0,0],[1,0],[2,0],[3,0]]), 2, "نقاط مستقيمة")
# apl-source:53
