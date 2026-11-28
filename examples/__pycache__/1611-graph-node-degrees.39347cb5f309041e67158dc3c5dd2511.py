
# apl-source:1
# مثال 1611 — درجات رؤوس الرسم
# apl-source:2
# Graph node degrees
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1611-graph-node-degrees.apl
# apl-source:6

# apl-source:7
# كل ضلع يزيد درجة طرفيه
# apl-source:8
# نخزن الدرجات في قاموس
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
def الدرجات(أضلاع):
  # apl-source:19
  د = {}
  # apl-source:20
  for ض in أضلاع:
    # apl-source:21
    د[ض[0]] = د.get(ض[0], 0) + 1
    # apl-source:22
    د[ض[1]] = د.get(ض[1], 0) + 1
  # apl-source:23
  return د
# apl-source:24

# apl-source:25
تأكد_يساوي(الدرجات([[1, 2], [2, 3], [3, 1]]), {1: 2, 2: 2, 3: 2}, "مثلث")
# apl-source:26
تأكد_يساوي(الدرجات([[1, 2], [1, 3], [1, 4]]), {1: 3, 2: 1, 3: 1, 4: 1}, "نجمة")
# apl-source:27
تأكد_يساوي(الدرجات([]), {}, "فارغ")
# apl-source:28
