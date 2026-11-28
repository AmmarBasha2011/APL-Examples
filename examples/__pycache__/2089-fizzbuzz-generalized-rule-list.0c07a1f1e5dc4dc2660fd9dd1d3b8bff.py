
# apl-source:1
# مثال 2089 — فيزباز بقواعد عامة
# apl-source:2
# Generalized FizzBuzz
# apl-source:3
# Demonstrates: حلقات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2089-fizzbuzz-generalized-rule-list.apl
# apl-source:6

# apl-source:7
# # نلصق الكلمات التي ينطبق قاسمها
# apl-source:8
# # وإن لم تنطبق قاعدة نرجع العدد
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
def فيزباز(ن, قواعد):
  # apl-source:19
  خرج = ""
  # apl-source:20
  for ق in قواعد:
    # apl-source:21
    if ن % ق[0] == 0:
      # apl-source:22
      خرج = خرج + ق[1]
  # apl-source:23
  if خرج == "":
    # apl-source:24
    return str(ن)
  # apl-source:25
  return خرج
# apl-source:26

# apl-source:27
ر = [[3, "Fizz"], [5, "Buzz"], [7, "Baz"]]
# apl-source:28
تأكد_يساوي(فيزباز(105, ر), "FizzBuzzBaz", "كلها")
# apl-source:29
تأكد_يساوي(فيزباز(14, ر), "Baz", "٧ فقط")
# apl-source:30
تأكد_يساوي(فيزباز(11, ر), "11", "لا شيء")
# apl-source:31
تأكد_يساوي(فيزباز(15, ر), "FizzBuzz", "٣ و٥")
# apl-source:32
