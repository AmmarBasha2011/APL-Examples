
# apl-source:1
# مثال 666 — بحث 0-1
# apl-source:2
# 0-1 BFS
# apl-source:3
# Demonstrates: أوزان صفرية، طابور بطرفين، تكلفة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/666-zero-one-bfs.apl
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
# بحث 0-1: دايكسترا بتكاليف صفر وواحد
# apl-source:25
# Demonstrates: طابور بطرفين, دفع أمامي وخلفي, أقصر تكلفة
# apl-source:26
# أسرع من دايكسترا العام عندما الأوزان صفرية أو واحدة
# apl-source:27

# apl-source:28
حواف = {"أ": [["ب", 0], ["ج", 1]], "ب": [["د", 1], ["ه", 0]], "ج": [["و", 0]], "د": [["ز", 0]], "ه": [["ز", 1]], "و": [["ز", 1]], "ز": []}
# apl-source:29
عقد = ["أ", "ب", "ج", "د", "ه", "و", "ز"]
# apl-source:30

# apl-source:31
def أقصر_صفر_واحد(بداية):
  # apl-source:32
  تكلفة = {}
  # apl-source:33
  for ع in عقد:
    # apl-source:34
    تكلفة[ع] = 99
  # apl-source:35
  تكلفة[بداية] = 0
  # apl-source:36
  طابور = [بداية]
  # apl-source:37
  while len(طابور) > 0:
    # apl-source:38
    حالي = طابور[0]
    # apl-source:39
    طابور = طابور[1:]
    # apl-source:40
    for ح in حواف[حالي]:
      # apl-source:41
      جديدة = تكلفة[حالي] + ح[1]
      # apl-source:42
      if جديدة < تكلفة[ح[0]]:
        # apl-source:43
        تكلفة[ح[0]] = جديدة
        # apl-source:44
        if ح[1] == 0:
          # apl-source:45
          طابور.insert(0, ح[0])
        # apl-source:46
        else:
          # apl-source:47
          طابور.append(ح[0])
  # apl-source:48
  return تكلفة
# apl-source:49

# apl-source:50
def أقصر_دايكسترا(بداية):
  # apl-source:51
  تكلفة = {}
  # apl-source:52
  محسومة = {}
  # apl-source:53
  for ع in عقد:
    # apl-source:54
    تكلفة[ع] = 99
  # apl-source:55
  تكلفة[بداية] = 0
  # apl-source:56
  while len(محسومة) < len(عقد):
    # apl-source:57
    أدنى = 99
    # apl-source:58
    عقدة_أدنى = ""
    # apl-source:59
    for ع in عقد:
      # apl-source:60
      if (ع in محسومة) == False and تكلفة[ع] < أدنى:
        # apl-source:61
        أدنى = تكلفة[ع]
        # apl-source:62
        عقدة_أدنى = ع
    # apl-source:63
    if عقدة_أدنى == "":
      # apl-source:64
      return تكلفة
    # apl-source:65
    محسومة[عقدة_أدنى] = True
    # apl-source:66
    for ح in حواف[عقدة_أدنى]:
      # apl-source:67
      if تكلفة[عقدة_أدنى] + ح[1] < تكلفة[ح[0]]:
        # apl-source:68
        تكلفة[ح[0]] = تكلفة[عقدة_أدنى] + ح[1]
  # apl-source:69
  return تكلفة
# apl-source:70

# apl-source:71
أ = أقصر_صفر_واحد("أ")
# apl-source:72
ب = أقصر_دايكسترا("أ")
# apl-source:73
for ع in عقد:
  # apl-source:74
  تأكد_يساوي(أ[ع], ب[ع], "تطابق مع دايكسترا")
# apl-source:75
تأكد_يساوي(أ["ز"], 1, "تكلفة الوصول إلى ز")
# apl-source:76
print("تكاليف من أ:", أ)
# apl-source:77
