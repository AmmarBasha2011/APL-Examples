
# apl-source:1
# مثال 935 — مطابق تعابير مبسط
# apl-source:2
# Simple regex matcher
# apl-source:3
# Demonstrates: نقطة ونجمة بديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/935-regex-matcher.apl
# apl-source:6

# apl-source:7
# مطابق تعابير نمطية مبسط: نقطة (أي حرف) ونجمة (صفر أو أكثر)
# apl-source:8
# برمجة ديناميكية على النص والنمط
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
def يطابق(نص, نمط):
  # apl-source:19
  ن = len(نص)
  # apl-source:20
  م = len(نمط)
  # apl-source:21
  ع = []
  # apl-source:22
  for _ in range(ن + 1):
    # apl-source:23
    صف = []
    # apl-source:24
    for __ in range(م + 1):
      # apl-source:25
      صف = صف + [False]
    # apl-source:26
    ع = ع + [صف]
  # apl-source:27
  ع[0][0] = 1 == 1
  # apl-source:28
  for ج in range(1, م + 1):
    # apl-source:29
    if نمط[ج - 1] == "*":
      # apl-source:30
      ع[0][ج] = ع[0][ج - 2]
  # apl-source:31
  for i in range(1, ن + 1):
    # apl-source:32
    for ج in range(1, م + 1):
      # apl-source:33
      if نمط[ج - 1] == "*":
        # apl-source:34
        ع[i][ج] = ع[i][ج - 2]
        # apl-source:35
        if نمط[ج - 2] == "." or نمط[ج - 2] == نص[i - 1]:
          # apl-source:36
          if ع[i - 1][ج]:
            # apl-source:37
            ع[i][ج] = 1 == 1
      # apl-source:38
      else:
        # apl-source:39
        if نمط[ج - 1] == "." or نمط[ج - 1] == نص[i - 1]:
          # apl-source:40
          ع[i][ج] = ع[i - 1][ج - 1]
  # apl-source:41
  return ع[ن][م]
# apl-source:42

# apl-source:43
print("aab ~ c*a*b:", يطابق("aab", "c*a*b"))
# apl-source:44
print("ab ~ .*:", يطابق("ab", ".*"))
# apl-source:45

# apl-source:46
تأكد_يساوي(يطابق("aab", "c*a*b"), 1 == 1, "نجمة صفر c")
# apl-source:47
تأكد_يساوي(يطابق("ab", ".*"), 1 == 1, "نقطة نجمة تطابق الكل")
# apl-source:48
تأكد_يساوي(يطابق("mississippi", "mis*is*p*."), False, "مثال سالب")
# apl-source:49
تأكد_يساوي(يطابق("aa", "a"), False, "أطول من النمط")
# apl-source:50
تأكد_يساوي(يطابق("aa", "a*"), 1 == 1, "نجمة تكرار")
# apl-source:51
تأكد_يساوي(يطابق("", "a*b*"), 1 == 1, "فارغ مع نجوم")
# apl-source:52
