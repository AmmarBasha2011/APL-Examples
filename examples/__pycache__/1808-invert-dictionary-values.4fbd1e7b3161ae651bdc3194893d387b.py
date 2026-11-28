
# apl-source:1
# مثال 1808 — عكس القاموس
# apl-source:2
# Invert a dictionary
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1808-invert-dictionary-values.apl
# apl-source:6

# apl-source:7
# كل قيمة تجمع مفاتيحها
# apl-source:8
# نرتب القوائم للمقارنة
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
def اعكس(ق):
  # apl-source:19
  ناتج = {}
  # apl-source:20
  for ك in ق:
    # apl-source:21
    م = str(ق[ك])
    # apl-source:22
    if (م in ناتج) == False:
      # apl-source:23
      ناتج[م] = []
    # apl-source:24
    ناتج[م].append(ك)
  # apl-source:25
  for م in ناتج:
    # apl-source:26
    ناتج[م].sort()
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
ن = اعكس({"a": 1, "b": 2, "c": 1})
# apl-source:30
تأكد_يساوي(ن["1"], ["a", "c"], "قيمة مشتركة")
# apl-source:31
تأكد_يساوي(ن["2"], ["b"], "قيمة وحيدة")
# apl-source:32
