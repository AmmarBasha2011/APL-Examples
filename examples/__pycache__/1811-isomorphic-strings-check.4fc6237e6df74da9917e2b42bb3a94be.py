
# apl-source:1
# مثال 1811 — نصان متماثلان في النمط
# apl-source:2
# Isomorphic strings
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1811-isomorphic-strings-check.apl
# apl-source:6

# apl-source:7
# نربط الحرف بمقابله
# apl-source:8
# نتحقق من الاتجاهين
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
def متماثلان(أ, ب):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  خريطة1 = {}
  # apl-source:22
  خريطة2 = {}
  # apl-source:23
  for ك in range(len(أ)):
    # apl-source:24
    if أ[ك] in خريطة1:
      # apl-source:25
      if خريطة1[أ[ك]] != ب[ك]:
        # apl-source:26
        return False
    # apl-source:27
    else:
      # apl-source:28
      خريطة1[أ[ك]] = ب[ك]
    # apl-source:29
    if ب[ك] in خريطة2:
      # apl-source:30
      if خريطة2[ب[ك]] != أ[ك]:
        # apl-source:31
        return False
    # apl-source:32
    else:
      # apl-source:33
      خريطة2[ب[ك]] = أ[ك]
  # apl-source:34
  return True
# apl-source:35

# apl-source:36
تأكد_يساوي(متماثلان("egg", "add"), True, "نمط")
# apl-source:37
تأكد_يساوي(متماثلان("foo", "bar"), False, "مختلفان")
# apl-source:38
تأكد_يساوي(متماثلان("ab", "aa"), False, "اتجاه")
# apl-source:39
