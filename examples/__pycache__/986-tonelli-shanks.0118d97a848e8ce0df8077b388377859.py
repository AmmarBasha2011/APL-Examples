
# apl-source:1
# مثال 986 — جذر تونلي-شانكس
# apl-source:2
# Tonelli-Shanks
# apl-source:3
# Demonstrates: جذر تربيعي مودولو أولي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/986-tonelli-shanks.apl
# apl-source:6

# apl-source:7
# تونلي-شانكس: الجذر التربيعي في الحقول المنتهية بترد أولي
# apl-source:8
# يحل س^2 تطابق ن بترد ب حتى لو كان ب-1 زوجي البنية
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
def قوة_مود(أ, هـ, م):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  قاعدة = أ % م
  # apl-source:21
  باقي = هـ
  # apl-source:22
  while باقي > 0:
    # apl-source:23
    if (باقي % 2) == 1:
      # apl-source:24
      ناتج = (ناتج * قاعدة) % م
    # apl-source:25
    قاعدة = (قاعدة * قاعدة) % م
    # apl-source:26
    باقي = باقي // 2
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def جذر_مود(ن, ب):
  # apl-source:30
  if قوة_مود(ن, (ب - 1) // 2, ب) != 1:
    # apl-source:31
    return -1
  # apl-source:32
  ق = ب - 1
  # apl-source:33
  س = 0
  # apl-source:34
  while (ق % 2) == 0:
    # apl-source:35
    ق = ق // 2
    # apl-source:36
    س = س + 1
  # apl-source:37
  ز = 2
  # apl-source:38
  while قوة_مود(ز, (ب - 1) // 2, ب) != (ب - 1):
    # apl-source:39
    ز = ز + 1
  # apl-source:40
  ج = قوة_مود(ز, ق, ب)
  # apl-source:41
  س_حل = قوة_مود(ن, (ق + 1) // 2, ب)
  # apl-source:42
  ت = قوة_مود(ن, ق, ب)
  # apl-source:43
  م = س
  # apl-source:44
  while ت != 1:
    # apl-source:45
    i = 1
    # apl-source:46
    ت2 = (ت * ت) % ب
    # apl-source:47
    while ت2 != 1:
      # apl-source:48
      ت2 = (ت2 * ت2) % ب
      # apl-source:49
      i = i + 1
    # apl-source:50
    ب_م = قوة_مود(ج, 1 << ((م - i) - 1), ب)
    # apl-source:51
    ج = (ب_م * ب_م) % ب
    # apl-source:52
    س_حل = (س_حل * ب_م) % ب
    # apl-source:53
    ت = (ت * ج) % ب
    # apl-source:54
    م = i
  # apl-source:55
  return س_حل
# apl-source:56

# apl-source:57
حل1 = جذر_مود(10, 13)
# apl-source:58
تأكد_يساوي((حل1 * حل1) % 13, 10, "جذر العشرة بترد 13")
# apl-source:59
حل2 = جذر_مود(4, 13)
# apl-source:60
تأكد_يساوي((حل2 * حل2) % 13, 4, "جذر الأربعة بترد 13")
# apl-source:61
تأكد_يساوي(جذر_مود(5, 13), -1, "لا جذر للخمسة")
# apl-source:62
