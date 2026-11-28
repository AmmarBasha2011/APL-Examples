
# apl-source:1
# مثال 955 — تقاطع القطع المستقيمة
# apl-source:2
# Segment intersection
# apl-source:3
# Demonstrates: توجهات نسبية أربع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/955-segment-intersection.apl
# apl-source:6

# apl-source:7
# تقاطع القطع المستقيمة: فحص التوجهات النسبية للنقط الأربع
# apl-source:8
# تتقاطع إن تفرقت النهايات حول القطعة الأخرى
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
def توجه(أ, ب, ج):
  # apl-source:19
  # إشارة الجداء التبادلي: موجب يمين وسالب يسار وصفر استقامة
  # apl-source:20
  return (ب[0] - أ[0]) * (ج[1] - أ[1]) - (ب[1] - أ[1]) * (ج[0] - أ[0])
# apl-source:21

# apl-source:22
def تتقاطع(ن1, ن2, ن3, ن4):
  # apl-source:23
  ع1 = توجه(ن3, ن4, ن1)
  # apl-source:24
  ع2 = توجه(ن3, ن4, ن2)
  # apl-source:25
  ع3 = توجه(ن1, ن2, ن3)
  # apl-source:26
  ع4 = توجه(ن1, ن2, ن4)
  # apl-source:27
  if (ع1 > 0 and ع2 < 0) or (ع1 < 0 and ع2 > 0):
    # apl-source:28
    if (ع3 > 0 and ع4 < 0) or (ع3 < 0 and ع4 > 0):
      # apl-source:29
      return 1 == 1
  # apl-source:30
  return False
# apl-source:31

# apl-source:32
print("متقاطعتان:", تتقاطع([0, 0], [4, 4], [0, 4], [4, 0]))
# apl-source:33
print("متوازيتان:", تتقاطع([0, 0], [1, 1], [2, 2], [3, 3]))
# apl-source:34

# apl-source:35
تأكد_يساوي(تتقاطع([0, 0], [4, 4], [0, 4], [4, 0]), 1 == 1, "تقاطع X")
# apl-source:36
تأكد_يساوي(تتقاطع([0, 0], [1, 1], [2, 2], [3, 3]), False, "مستقيمتان متوازيتان")
# apl-source:37
تأكد_يساوي(تتقاطع([0, 0], [2, 0], [1, -1], [1, 1]), 1 == 1, "تقاطع T")
# apl-source:38
تأكد_يساوي(تتقاطع([0, 0], [1, 0], [2, 1], [3, 1]), False, "منفصلتان")
# apl-source:39
# إشارة التوجه
# apl-source:40
if توجه([0, 0], [1, 0], [1, 1]) <= 0:
  # apl-source:41
  print("فشل: إشارة التوجه")
  # apl-source:42
  قياسي_نظام_اخرج(1)
# apl-source:43
print("ناجح: إشارة التوجه")
# apl-source:44
