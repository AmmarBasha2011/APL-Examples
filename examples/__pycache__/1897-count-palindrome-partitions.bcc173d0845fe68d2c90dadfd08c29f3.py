
# apl-source:1
# مثال 1897 — عدد تقسيمات النص لمتماثلات
# apl-source:2
# Count palindrome partitions
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1897-count-palindrome-partitions.apl
# apl-source:6

# apl-source:7
# نجرب كل بداية جزء
# apl-source:8
# نكمل الباقي بالتراجع
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
def متماثل(س):
  # apl-source:19
  for ك in range(len(س) // 2):
    # apl-source:20
    if س[ك] != س[len(س) - 1 - ك]:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
def تقسيمات(س):
  # apl-source:25
  if len(س) == 0:
    # apl-source:26
    return 1
  # apl-source:27
  عد = 0
  # apl-source:28
  for ك in range(1, len(س) + 1):
    # apl-source:29
    if متماثل(س[0:ك]):
      # apl-source:30
      عد = عد + تقسيمات(س[ك:len(س)])
  # apl-source:31
  return عد
# apl-source:32

# apl-source:33
تأكد_يساوي(تقسيمات("aab"), 2, "aab")
# apl-source:34
تأكد_يساوي(تقسيمات("aaa"), 4, "aaa")
# apl-source:35
تأكد_يساوي(تقسيمات("abc"), 1, "abc")
# apl-source:36
