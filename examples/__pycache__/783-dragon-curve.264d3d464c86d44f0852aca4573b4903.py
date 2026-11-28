
# apl-source:1
# مثال 783 — منحنى التنين
# apl-source:2
# Dragon curve
# apl-source:3
# Demonstrates: طي ورقة، عكس وقلب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/783-dragon-curve.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# منحنى التنين: متتالية طي الورقة يمين/يسار
# apl-source:25
# Demonstrates: s(n+1) = s(n) + R + عكس(قلب(s(n))), طول 2^n - 1
# apl-source:26

# apl-source:27
def قلب(س):
  # apl-source:28
  ناتج = ""
  # apl-source:29
  for حرف in س:
    # apl-source:30
    if حرف == "R":
      # apl-source:31
      ناتج = ناتج + "L"
    # apl-source:32
    else:
      # apl-source:33
      ناتج = ناتج + "R"
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
def عكس(س):
  # apl-source:37
  ناتج = ""
  # apl-source:38
  for ي in range(len(س)):
    # apl-source:39
    ناتج = ناتج + س[len(س) - 1 - ي]
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def تنين(ن):
  # apl-source:43
  س = ""
  # apl-source:44
  for ي in range(ن):
    # apl-source:45
    س = س + "R" + عكس(قلب(س))
  # apl-source:46
  return س
# apl-source:47

# apl-source:48
تأكد_يساوي(تنين(1), "R", "طية 1")
# apl-source:49
تأكد_يساوي(تنين(2), "RRL", "طية 2")
# apl-source:50
تأكد_يساوي(تنين(3), "RRLRRLL", "طية 3")
# apl-source:51
تأكد_يساوي(تنين(4), "RRLRRLLRRRLLRLL", "طية 4")
# apl-source:52
تأكد_يساوي(len(تنين(10)), 1023, "طول 2^10 - 1")
# apl-source:53
تأكد_يساوي(عكس("RRL"), "LRR", "عكس")
# apl-source:54
تأكد_يساوي(قلب("RRL"), "LLR", "قلب")
# apl-source:55
