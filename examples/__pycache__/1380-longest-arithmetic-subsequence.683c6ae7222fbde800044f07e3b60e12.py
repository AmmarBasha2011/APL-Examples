
# apl-source:1
# مثال 1380 — أطول متتالية حسابية
# apl-source:2
# Longest arithmetic subsequence
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1380-longest-arithmetic-subsequence.apl
# apl-source:6

# apl-source:7
# نخزن لكل موضع طول المتتالية لكل فارق
# apl-source:8
# نمد المتتاليات من المواضع السابقة
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
def اطول_حسابية(أرقام):
  # apl-source:19
  ن = len(أرقام)
  # apl-source:20
  if ن <= 2:
    # apl-source:21
    return ن
  # apl-source:22
  جداول = []
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    جداول = جداول + [{}]
  # apl-source:25
  اقصى = 2
  # apl-source:26
  for ي in range(ن):
    # apl-source:27
    for ك in range(ي):
      # apl-source:28
      فارق = أرقام[ي] - أرقام[ك]
      # apl-source:29
      طول_ = جداول[ك].get(فارق, 1) + 1
      # apl-source:30
      جداول[ي][فارق] = طول_
      # apl-source:31
      if طول_ > اقصى:
        # apl-source:32
        اقصى = طول_
  # apl-source:33
  return اقصى
# apl-source:34

# apl-source:35
تأكد_يساوي(اطول_حسابية([3,6,9,12]), 4, "أربعة")
# apl-source:36
تأكد_يساوي(اطول_حسابية([9,4,7,2,10]), 3, "ثلاثة")
# apl-source:37
تأكد_يساوي(اطول_حسابية([20,1,15,3,10,5,8]), 4, "أربعة ثانية")
# apl-source:38
