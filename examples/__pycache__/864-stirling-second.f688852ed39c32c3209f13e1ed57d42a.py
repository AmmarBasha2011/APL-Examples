
# apl-source:1
# مثال 864 — ستيرلينغ الثاني
# apl-source:2
# Stirling numbers 2nd kind
# apl-source:3
# Demonstrates: تقسيم n عنصراً لك مجموعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/864-stirling-second.apl
# apl-source:6

# apl-source:7
# أعداد ستيرلينغ من النوع الثاني: S(n,k) عدد تقسيم n عنصراً إلى k مجموعات
# apl-source:8
# S(n,k) = k*S(n-1,k) + S(n-1,k-1)
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
def ستيرلينغ2(ن, ك):
  # apl-source:19
  if ن == 0 and ك == 0:
    # apl-source:20
    return 1
  # apl-source:21
  if ن == 0 or ك == 0:
    # apl-source:22
    return 0
  # apl-source:23
  return ك * ستيرلينغ2(ن - 1, ك) + ستيرلينغ2(ن - 1, ك - 1)
# apl-source:24

# apl-source:25
print("S(5,2) =", ستيرلينغ2(5, 2))
# apl-source:26
print("S(6,3) =", ستيرلينغ2(6, 3))
# apl-source:27
print("S(7,4) =", ستيرلينغ2(7, 4))
# apl-source:28

# apl-source:29
تأكد_يساوي(ستيرلينغ2(5, 2), 15, "S(5,2) = 15")
# apl-source:30
تأكد_يساوي(ستيرلينغ2(6, 3), 90, "S(6,3) = 90")
# apl-source:31
تأكد_يساوي(ستيرلينغ2(7, 4), 350, "S(7,4) = 350")
# apl-source:32

# apl-source:33
# S(n,1) = 1 و S(n,n) = 1 و S(n,2) = 2^(n-1) - 1
# apl-source:34
تأكد_يساوي(ستيرلينغ2(8, 1), 1, "S(n,1) = 1")
# apl-source:35
تأكد_يساوي(ستيرلينغ2(8, 8), 1, "S(n,n) = 1")
# apl-source:36
تأكد_يساوي(ستيرلينغ2(8, 2), 127, "S(8,2) = 2^7 - 1")
# apl-source:37
