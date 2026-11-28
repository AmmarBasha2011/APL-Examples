
# apl-source:1
# مثال 1609 — مسارات الجذر إلى الأوراق
# apl-source:2
# Root to leaf paths
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1609-tree-root-to-leaf-paths.apl
# apl-source:6

# apl-source:7
# نمرر المسار الحالي نزولاً
# apl-source:8
# عند الورقة نسجل المسار
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
def المسارات(ش, مسار, نتيجة):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return نتيجة
  # apl-source:21
  جديد = مسار + [ش[0]]
  # apl-source:22
  if ش[1] == [] and ش[2] == []:
    # apl-source:23
    نتيجة.append(جديد)
    # apl-source:24
    return نتيجة
  # apl-source:25
  المسارات(ش[1], جديد, نتيجة)
  # apl-source:26
  المسارات(ش[2], جديد, نتيجة)
  # apl-source:27
  return نتيجة
# apl-source:28

# apl-source:29
تأكد_يساوي(المسارات([1, [2, [], [5, [], []]], [3, [], []]], [], []), [[1, 2, 5], [1, 3]], "مساران")
# apl-source:30
تأكد_يساوي(المسارات([7, [], []], [], []), [[7]], "جذر")
# apl-source:31
تأكد_يساوي(المسارات([], [], []), [], "فارغة")
# apl-source:32
