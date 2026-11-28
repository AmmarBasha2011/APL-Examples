
# apl-source:1
# مثال 2060 — الفرز بالسلال حسب خانة العشرات
# apl-source:2
# Bucket sort by tens
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2060-bucket-sort-by-tens-group.apl
# apl-source:6

# apl-source:7
# # كل سلة تفرز على حدة
# apl-source:8
# # ثم تجمع السلال بالترتيب
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
def سلال(ق):
  # apl-source:19
  س = []
  # apl-source:20
  for ك in range(10):
    # apl-source:21
    س = س + [[]]
  # apl-source:22
  for ع in ق:
    # apl-source:23
    س[ع // 10].append(ع)
  # apl-source:24
  خرج = []
  # apl-source:25
  for سلة in س:
    # apl-source:26
    خرج = خرج + sorted(سلة)
  # apl-source:27
  return خرج
# apl-source:28

# apl-source:29
تأكد_يساوي(سلال([29, 25, 3, 49, 9, 37, 21, 43]), [3, 9, 21, 25, 29, 37, 43, 49], "ثمانية")
# apl-source:30
تأكد_يساوي(سلال([99, 0]), [0, 99], "حدان")
# apl-source:31
