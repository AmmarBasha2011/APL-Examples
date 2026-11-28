
# apl-source:1
# مثال 1927 — أطول نص متماثل بالتوسع من المركز
# apl-source:2
# Longest palindromic substring by center expansion
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1927-longest-palindrome-expand-center.apl
# apl-source:6

# apl-source:7
# لكل مركز نوسع طالما تطابق الطرفان
# apl-source:8
# نحفظ الأطول
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
def وسع(س, ي, ك):
  # apl-source:19
  while ي >= 0 and ك < len(س) and س[ي] == س[ك]:
    # apl-source:20
    ي = ي - 1
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return س[ي + 1:ك]
# apl-source:23

# apl-source:24
def أطول_متماثل(س):
  # apl-source:25
  أفضل = ""
  # apl-source:26
  for م in range(len(س)):
    # apl-source:27
    فردي = وسع(س, م, م)
    # apl-source:28
    زوجي = وسع(س, م, م + 1)
    # apl-source:29
    if len(فردي) > len(أفضل):
      # apl-source:30
      أفضل = فردي
    # apl-source:31
    if len(زوجي) > len(أفضل):
      # apl-source:32
      أفضل = زوجي
  # apl-source:33
  return أفضل
# apl-source:34

# apl-source:35
تأكد_يساوي(أطول_متماثل("babad"), "bab", "babad")
# apl-source:36
تأكد_يساوي(أطول_متماثل("cbbd"), "bb", "زوجي")
# apl-source:37
تأكد_يساوي(أطول_متماثل("a"), "a", "حرف")
# apl-source:38
