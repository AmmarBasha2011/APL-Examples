
# apl-source:1
# مثال 892 — أعداد نارايانا
# apl-source:2
# Narayana numbers
# apl-source:3
# Demonstrates: توافيق مقسمة على ن
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/892-narayana-numbers.apl
# apl-source:6

# apl-source:7
# أعداد نارايانا: تنعيم أعداد كاتالان بعدد القمم
# apl-source:8
# N(n,k) = C(n,k) * C(n,k-1) / n
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
def توافيق(ن, ك):
  # apl-source:19
  if ك > ن:
    # apl-source:20
    return 0
  # apl-source:21
  بسط = 1
  # apl-source:22
  مقام = 1
  # apl-source:23
  for i in range(ك):
    # apl-source:24
    بسط = بسط * (ن - i)
    # apl-source:25
    مقام = مقام * (i + 1)
  # apl-source:26
  return بسط // مقام
# apl-source:27

# apl-source:28
def نارايانا(ن, ك):
  # apl-source:29
  return توافيق(ن, ك) * توافيق(ن, ك - 1) // ن
# apl-source:30

# apl-source:31
print("N(5,3) =", نارايانا(5, 3))
# apl-source:32
print("N(6,2) =", نارايانا(6, 2))
# apl-source:33

# apl-source:34
تأكد_يساوي(نارايانا(5, 3), 20, "N(5,3) = 20")
# apl-source:35
تأكد_يساوي(نارايانا(6, 2), 15, "N(6,2) = 15")
# apl-source:36
تأكد_يساوي(نارايانا(4, 1), 1, "N(n,1) = 1")
# apl-source:37
تأكد_يساوي(نارايانا(4, 4), 1, "N(n,n) = 1")
# apl-source:38

# apl-source:39
# مجموع الصف n هو عدد كاتالان C(n)
# apl-source:40
مجموع = 0
# apl-source:41
for ك in range(1, 6):
  # apl-source:42
  مجموع = مجموع + نارايانا(5, ك)
# apl-source:43
تأكد_يساوي(مجموع, 42, "مجموع الصف 5 هو كاتالان 42")
# apl-source:44
