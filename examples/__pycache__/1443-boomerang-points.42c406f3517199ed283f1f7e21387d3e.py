
# apl-source:1
# مثال 1443 — نقاط البومرانغ
# apl-source:2
# Valid boomerang three points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1443-boomerang-points.apl
# apl-source:6

# apl-source:7
# لا تتطابق نقطتان
# apl-source:8
# والجداء التقاطعي غير صفر
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
def بومرانغ(ن):
  # apl-source:19
  if (ن[0] == ن[1]) or (ن[1] == ن[2]) or (ن[0] == ن[2]):
    # apl-source:20
    return False
  # apl-source:21
  ض = (ن[1][0] - ن[0][0]) * (ن[2][1] - ن[0][1]) - (ن[1][1] - ن[0][1]) * (ن[2][0] - ن[0][0])
  # apl-source:22
  return ض != 0
# apl-source:23

# apl-source:24
تأكد_يساوي(بومرانغ([[1,1],[2,3],[3,2]]), True, "صالحة")
# apl-source:25
تأكد_يساوي(بومرانغ([[1,1],[2,2],[3,3]]), False, "مستقيمة")
# apl-source:26
تأكد_يساوي(بومرانغ([[0,0],[0,0],[1,2]]), False, "متطابقتان")
# apl-source:27
