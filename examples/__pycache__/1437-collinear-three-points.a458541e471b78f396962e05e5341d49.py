
# apl-source:1
# مثال 1437 — ثلاث نقاط على استقامة
# apl-source:2
# Three points collinear check
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1437-collinear-three-points.apl
# apl-source:6

# apl-source:7
# الجداء التقاطعي للفرقين صفر عند الاستقامة
# apl-source:8
# لا حاجة لقسمة أو جذر
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
def على_استقامة(أ, ب, ج):
  # apl-source:19
  return (ب[0] - أ[0]) * (ج[1] - أ[1]) - (ب[1] - أ[1]) * (ج[0] - أ[0]) == 0
# apl-source:20

# apl-source:21
تأكد_يساوي(على_استقامة([0,0], [1,1], [2,2]), True, "استقامة")
# apl-source:22
تأكد_يساوي(على_استقامة([0,0], [1,1], [2,3]), False, "ليست مستقيمة")
# apl-source:23
تأكد_يساوي(على_استقامة([1,1], [1,1], [5,7]), True, "نقطتان متطابقتان")
# apl-source:24
