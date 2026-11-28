
# apl-source:1
# مثال 2038 — نص متماثل بحذف حرف واحد على الأكثر
# apl-source:2
# Palindrome with one deletion
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2038-palindrome-allow-one-deletion.apl
# apl-source:6

# apl-source:7
# # نمشي من الطرفين
# apl-source:8
# # ونجرب حذف اليسار أو اليمين مرة واحدة
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
def متماثل(س, ي, ل):
  # apl-source:19
  while ي < ل:
    # apl-source:20
    if س[ي] != س[ل]:
      # apl-source:21
      return False
    # apl-source:22
    ي = ي + 1
    # apl-source:23
    ل = ل - 1
  # apl-source:24
  return True
# apl-source:25

# apl-source:26
def بحذف_واحد(س):
  # apl-source:27
  ي = 0
  # apl-source:28
  ل = len(س) - 1
  # apl-source:29
  while ي < ل:
    # apl-source:30
    if س[ي] != س[ل]:
      # apl-source:31
      return متماثل(س, ي + 1, ل) or متماثل(س, ي, ل - 1)
    # apl-source:32
    ي = ي + 1
    # apl-source:33
    ل = ل - 1
  # apl-source:34
  return True
# apl-source:35

# apl-source:36
تأكد_يساوي(بحذف_واحد("aba"), True, "متماثل")
# apl-source:37
تأكد_يساوي(بحذف_واحد("abca"), True, "حذف حرف")
# apl-source:38
تأكد_يساوي(بحذف_واحد("abc"), False, "لا يكفي")
# apl-source:39
تأكد_يساوي(بحذف_واحد(""), True, "فارغ")
# apl-source:40
