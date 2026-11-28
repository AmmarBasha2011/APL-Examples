
# apl-source:1
# مثال 1353 — أقرب نقاط
# apl-source:2
# K closest points to origin
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1353-k-closest-points.apl
# apl-source:6

# apl-source:7
# نحسب مربع المسافة لكل نقطة
# apl-source:8
# نرتب ونأخذ أول ك
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
def اقرب_نقاط(نقاط, ك):
  # apl-source:19
  مع_مسافة = []
  # apl-source:20
  for ن in نقاط:
    # apl-source:21
    مع_مسافة = مع_مسافة + [[ن[0] * ن[0] + ن[1] * ن[1], ن[0], ن[1]]]
  # apl-source:22
  مع_مسافة = sorted(مع_مسافة)
  # apl-source:23
  ناتج = []
  # apl-source:24
  for ع in range(ك):
    # apl-source:25
    ناتج = ناتج + [[مع_مسافة[ع][1], مع_مسافة[ع][2]]]
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(اقرب_نقاط([[1,3],[-2,2]], 1), [[-2,2]], "نقطة واحدة")
# apl-source:29
تأكد_يساوي(اقرب_نقاط([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]], "نقطتان")
# apl-source:30
تأكد_يساوي(اقرب_نقاط([[0,1],[1,0]], 2), [[0,1],[1,0]], "كلهما")
# apl-source:31
