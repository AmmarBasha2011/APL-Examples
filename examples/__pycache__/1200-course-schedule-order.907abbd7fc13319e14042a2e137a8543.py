
# apl-source:1
# مثال 1200 — ترتيب المقررات
# apl-source:2
# Course schedule ordering
# apl-source:3
# Demonstrates: فرز طوبولوجي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1200-course-schedule-order.apl
# apl-source:6

# apl-source:7
# ندرس المقرر حين تنتهي متطلباته
# apl-source:8
# ونكتشف الحلقة لو بقي مقرر بلا ترتيب
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
def ترتيب_المقررات(ن, متطلبات):
  # apl-source:19
  داخل = [0] * ن
  # apl-source:20
  جيران = []
  # apl-source:21
  for ع in range(ن):
    # apl-source:22
    جيران = جيران + [[]]
  # apl-source:23
  for م in متطلبات:
    # apl-source:24
    جيران[م[1]] = جيران[م[1]] + [م[0]]
    # apl-source:25
    داخل[م[0]] = داخل[م[0]] + 1
  # apl-source:26
  طابور = []
  # apl-source:27
  for ع in range(ن):
    # apl-source:28
    if داخل[ع] == 0:
      # apl-source:29
      طابور = طابور + [ع]
  # apl-source:30
  ناتج = []
  # apl-source:31
  ك = 0
  # apl-source:32
  while ك < len(طابور):
    # apl-source:33
    س = طابور[ك]
    # apl-source:34
    ك = ك + 1
    # apl-source:35
    ناتج = ناتج + [س]
    # apl-source:36
    for ج in جيران[س]:
      # apl-source:37
      داخل[ج] = داخل[ج] - 1
      # apl-source:38
      if داخل[ج] == 0:
        # apl-source:39
        طابور = طابور + [ج]
  # apl-source:40
  if len(ناتج) == ن:
    # apl-source:41
    return ناتج
  # apl-source:42
  return []
# apl-source:43

# apl-source:44
تأكد_يساوي(ترتيب_المقررات(2, [[1,0]]), [0, 1], "مقرران")
# apl-source:45
تأكد_يساوي(ترتيب_المقررات(4, [[1,0],[2,0],[3,1],[3,2]]), [0, 1, 2, 3], "أربعة")
# apl-source:46
تأكد_يساوي(ترتيب_المقررات(2, [[1,0],[0,1]]), [], "حلقة")
# apl-source:47
تأكد_يساوي(ترتيب_المقررات(3, []), [0, 1, 2], "بلا متطلبات")
# apl-source:48
