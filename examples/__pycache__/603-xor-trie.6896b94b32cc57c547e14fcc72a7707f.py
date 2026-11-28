
# apl-source:1
# مثال 603 — شجرة XOR
# apl-source:2
# XOR trie
# apl-source:3
# Demonstrates: شجرة بتات، أو-حصري، أقصى زوج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/603-xor-trie.apl
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
# شجرة XOR: أكبر حصيلة أو-حصري بين زوج
# apl-source:25
# Demonstrates: شجرة ثنائية على البتات, بحث جشع عن المكمل
# apl-source:26
# أسرع من فحص كل الأزواج للمصفوفات الكبيرة
# apl-source:27

# apl-source:28
def أقصى_أو(أرقام):
  # apl-source:29
  أعلى_بت = 5
  # apl-source:30
  شجرة = {}
  # apl-source:31
  for عدد in أرقام:
    # apl-source:32
    عقدة = شجرة
    # apl-source:33
    for بت in range(أعلى_بت, -1, -1):
      # apl-source:34
      ب = (عدد // (2 ** بت)) % 2
      # apl-source:35
      if ب in عقدة:
        # apl-source:36
        عقدة = عقدة[ب]
      # apl-source:37
      else:
        # apl-source:38
        عقدة[ب] = {}
        # apl-source:39
        عقدة = عقدة[ب]
  # apl-source:40
  أقصى = 0
  # apl-source:41
  for عدد in أرقام:
    # apl-source:42
    عقدة = شجرة
    # apl-source:43
    مرشح = 0
    # apl-source:44
    for بت in range(أعلى_بت, -1, -1):
      # apl-source:45
      ب = (عدد // (2 ** بت)) % 2
      # apl-source:46
      مكمل = 1 - ب
      # apl-source:47
      if مكمل in عقدة:
        # apl-source:48
        مرشح = مرشح + 2 ** بت
        # apl-source:49
        عقدة = عقدة[مكمل]
      # apl-source:50
      else:
        # apl-source:51
        عقدة = عقدة[ب]
    # apl-source:52
    if مرشح > أقصى:
      # apl-source:53
      أقصى = مرشح
  # apl-source:54
  return أقصى
# apl-source:55

# apl-source:56
نتيجة = أقصى_أو([3, 10, 5, 25, 2, 8])
# apl-source:57
print("أقصى أو-حصري:", نتيجة)
# apl-source:58
تأكد_يساوي(نتيجة, 28, "خمسة XOR خمسة وعشرون")
# apl-source:59
تأكد_يساوي(5 ^ 25, 28, "تحقق مباشر")
# apl-source:60
