
# apl-source:1
# مثال 2018 — التحليل إلى عوامل أولية بأسس
# apl-source:2
# Prime factorization pairs
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2018-prime-factorization-exponent-pairs.apl
# apl-source:6

# apl-source:7
# # نقسم على كل عامل ما أمكن
# apl-source:8
# # ويبقى عامل أولي أخير إن كان أكبر من 1
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
def تحليل(ن):
  # apl-source:19
  خرج = []
  # apl-source:20
  د = 2
  # apl-source:21
  while د * د <= ن:
    # apl-source:22
    if ن % د == 0:
      # apl-source:23
      أس = 0
      # apl-source:24
      while ن % د == 0:
        # apl-source:25
        ن = ن // د
        # apl-source:26
        أس = أس + 1
      # apl-source:27
      خرج = خرج + [[د, أس]]
    # apl-source:28
    د = د + 1
  # apl-source:29
  if ن > 1:
    # apl-source:30
    خرج = خرج + [[ن, 1]]
  # apl-source:31
  return خرج
# apl-source:32

# apl-source:33
تأكد_يساوي(تحليل(360), [[2, 3], [3, 2], [5, 1]], "٣٦٠")
# apl-source:34
تأكد_يساوي(تحليل(97), [[97, 1]], "أولي")
# apl-source:35
تأكد_يساوي(تحليل(1), [], "واحد")
# apl-source:36
تأكد_يساوي(تحليل(1001), [[7, 1], [11, 1], [13, 1]], "١٠٠١")
# apl-source:37
