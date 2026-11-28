
# apl-source:1
# مثال 1213 — تسلسل شجرة
# apl-source:2
# Serialize and deserialize tree
# apl-source:3
# Demonstrates: ترميز نصي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1213-tree-serialize.apl
# apl-source:6

# apl-source:7
# نكتب الجذر ثم الفرعين مع علامة # للفارغ
# apl-source:8
# ونقرأ النص بنفس الترتيب
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
def رمّز(ش):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return "#"
  # apl-source:21
  return str(ش[0]) + "," + رمّز(ش[1]) + "," + رمّز(ش[2])
# apl-source:22

# apl-source:23
def فك_رمز(اجزاء, موقع):
  # apl-source:24
  if اجزاء[موقع[0]] == "#":
    # apl-source:25
    موقع[0] = موقع[0] + 1
    # apl-source:26
    return []
  # apl-source:27
  قيمة = int(اجزاء[موقع[0]])
  # apl-source:28
  موقع[0] = موقع[0] + 1
  # apl-source:29
  يسار = فك_رمز(اجزاء, موقع)
  # apl-source:30
  يمين = فك_رمز(اجزاء, موقع)
  # apl-source:31
  return [قيمة, يسار, يمين]
# apl-source:32

# apl-source:33
شجرة = [1, [2, [], []], [3, [4, [], []], [5, [], []]]]
# apl-source:34
نص_شجرة = رمّز(شجرة)
# apl-source:35
تأكد_يساوي(نص_شجرة, "1,2,#,#,3,4,#,#,5,#,#", "الترميز")
# apl-source:36
تأكد_يساوي(فك_رمز(نص_شجرة.split(","), [0]), شجرة, "الفك")
# apl-source:37
تأكد_يساوي(رمّز([]), "#", "فارغة")
# apl-source:38
