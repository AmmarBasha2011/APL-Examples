
# apl-source:1
# مثال 1178 — إدراج مجال
# apl-source:2
# Insert interval
# apl-source:3
# Demonstrates: مسح خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1178-insert-interval.apl
# apl-source:6

# apl-source:7
# ننسخ ما قبله بلا تداخل
# apl-source:8
# وندمج المتداخل ثم ننسخ ما بعده
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
def ادرج(مجالات, جديد):
  # apl-source:19
  ناتج = []
  # apl-source:20
  ع = 0
  # apl-source:21
  ن = len(مجالات)
  # apl-source:22
  while (ع < ن) and (مجالات[ع][1] < جديد[0]):
    # apl-source:23
    ناتج = ناتج + [مجالات[ع]]
    # apl-source:24
    ع = ع + 1
  # apl-source:25
  ب = جديد[0]
  # apl-source:26
  ه = جديد[1]
  # apl-source:27
  while (ع < ن) and (مجالات[ع][0] <= ه):
    # apl-source:28
    ب = min(ب, مجالات[ع][0])
    # apl-source:29
    ه = max(ه, مجالات[ع][1])
    # apl-source:30
    ع = ع + 1
  # apl-source:31
  ناتج = ناتج + [[ب, ه]]
  # apl-source:32
  while ع < ن:
    # apl-source:33
    ناتج = ناتج + [مجالات[ع]]
    # apl-source:34
    ع = ع + 1
  # apl-source:35
  return ناتج
# apl-source:36

# apl-source:37
تأكد_يساوي(ادرج([[1,3],[6,9]], [2,5]), [[1,5],[6,9]], "مثال أول")
# apl-source:38
تأكد_يساوي(ادرج([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]], "مثال ثان")
# apl-source:39
تأكد_يساوي(ادرج([], [5,7]), [[5,7]], "فارغة")
# apl-source:40
تأكد_يساوي(ادرج([[1,5]], [6,8]), [[1,5],[6,8]], "بعدها")
# apl-source:41
