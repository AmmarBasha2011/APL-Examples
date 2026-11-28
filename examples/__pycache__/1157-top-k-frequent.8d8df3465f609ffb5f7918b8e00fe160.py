
# apl-source:1
# مثال 1157 — الأكثر تكراراً
# apl-source:2
# Top k frequent elements
# apl-source:3
# Demonstrates: عد وترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1157-top-k-frequent.apl
# apl-source:6

# apl-source:7
# نعد التكرارات
# apl-source:8
# ونأخذ k الأعلى مع كسر التعادل بالقيمة
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
def اكثر_تكرارا(أ, ك):
  # apl-source:19
  عد = {}
  # apl-source:20
  for س in أ:
    # apl-source:21
    عد[س] = عد.get(س, 0) + 1
  # apl-source:22
  ازواج = []
  # apl-source:23
  for س in عد:
    # apl-source:24
    ازواج = ازواج + [[-عد[س], س]]
  # apl-source:25
  ازواج = sorted(ازواج)
  # apl-source:26
  ناتج = []
  # apl-source:27
  for ع in range(ك):
    # apl-source:28
    ناتج = ناتج + [ازواج[ع][1]]
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(اكثر_تكرارا([1,1,1,2,2,3], 2), [1, 2], "مثال أول")
# apl-source:32
تأكد_يساوي(اكثر_تكرارا([1], 1), [1], "عنصر")
# apl-source:33
تأكد_يساوي(اكثر_تكرارا([4,4,5,5,6], 2), [4, 5], "تعادل")
# apl-source:34
