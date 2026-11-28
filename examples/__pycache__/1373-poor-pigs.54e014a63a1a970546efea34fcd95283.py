
# apl-source:1
# مثال 1373 — الخنازير الفقيرة
# apl-source:2
# Poor pigs buckets test
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1373-poor-pigs.apl
# apl-source:6

# apl-source:7
# كل خنزير له عدة حالات بحسب عدد الجولات
# apl-source:8
# عدد الحالات أس عدد الخنازير يجب أن يغطي الدلاء
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
def عدد_الخنازير(دلاء, دقائق_الموت, دقائق_الاختبار):
  # apl-source:19
  حالات = دقائق_الاختبار // دقائق_الموت + 1
  # apl-source:20
  خنازير = 0
  # apl-source:21
  قدرة = 1
  # apl-source:22
  while قدرة < دلاء:
    # apl-source:23
    قدرة = قدرة * حالات
    # apl-source:24
    خنازير = خنازير + 1
  # apl-source:25
  return خنازير
# apl-source:26

# apl-source:27
تأكد_يساوي(عدد_الخنازير(1000, 15, 60), 5, "ألف دلو")
# apl-source:28
تأكد_يساوي(عدد_الخنازير(4, 15, 15), 2, "أربعة دلاء")
# apl-source:29
تأكد_يساوي(عدد_الخنازير(1, 1, 1), 0, "دلو واحد")
# apl-source:30
