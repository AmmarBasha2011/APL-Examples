
# apl-source:1
# مثال 1540 — عكس القاموس
# apl-source:2
# Invert a dictionary
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1540-invert-dictionary.apl
# apl-source:6

# apl-source:7
# القيم المتكررة تتجمع في قائمة
# apl-source:8
# نبني قائمة لكل قيمة
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
def اعكس_القاموس(ق):
  # apl-source:19
  ناتج = {}
  # apl-source:20
  for ك in ق:
    # apl-source:21
    ف = ق[ك]
    # apl-source:22
    if ف in ناتج:
      # apl-source:23
      ناتج[ف].append(ك)
    # apl-source:24
    else:
      # apl-source:25
      ناتج[ف] = [ك]
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(اعكس_القاموس({"a": 1, "b": 2}), {1: ["a"], 2: ["b"]}, "مختلفة")
# apl-source:29
تأكد_يساوي(اعكس_القاموس({"a": 1, "b": 1}), {1: ["a", "b"]}, "مكررة")
# apl-source:30
تأكد_يساوي(اعكس_القاموس({}), {}, "فارغ")
# apl-source:31
