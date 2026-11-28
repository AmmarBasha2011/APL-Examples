
# apl-source:1
# مثال 1187 — من وسطي إلى لاحق
# apl-source:2
# Infix to postfix converter
# apl-source:3
# Demonstrates: شنتنغ يارد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1187-infix-to-postfix.apl
# apl-source:6

# apl-source:7
# نرتب العمليات بحسب أولويتها
# apl-source:8
# ونفرغ المكدس عند ظهور عملية أقل أولوية
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
def اولوية(ع):
  # apl-source:19
  if ع in "*/":
    # apl-source:20
    return 2
  # apl-source:21
  if ع in "+-":
    # apl-source:22
    return 1
  # apl-source:23
  return 0
# apl-source:24

# apl-source:25
def الى_لاحق(رموز):
  # apl-source:26
  ناتج = []
  # apl-source:27
  مكدس = []
  # apl-source:28
  for ر in رموز:
    # apl-source:29
    if ر.isdigit():
      # apl-source:30
      ناتج = ناتج + [ر]
    # apl-source:31
    elif ر == "(":
      # apl-source:32
      مكدس = مكدس + [ر]
    # apl-source:33
    elif ر == ")":
      # apl-source:34
      while مكدس[-1] != "(":
        # apl-source:35
        ناتج = ناتج + [مكدس.pop()]
      # apl-source:36
      مكدس.pop()
    # apl-source:37
    else:
      # apl-source:38
      while (len(مكدس) > 0) and (اولوية(مكدس[-1]) >= اولوية(ر)):
        # apl-source:39
        ناتج = ناتج + [مكدس.pop()]
      # apl-source:40
      مكدس = مكدس + [ر]
  # apl-source:41
  while len(مكدس) > 0:
    # apl-source:42
    ناتج = ناتج + [مكدس.pop()]
  # apl-source:43
  return ناتج
# apl-source:44

# apl-source:45
تأكد_يساوي(الى_لاحق(["1","+","2","*","3"]), ["1","2","3","*","+"], "أولوية")
# apl-source:46
تأكد_يساوي(الى_لاحق(["(","1","+","2",")","*","3"]), ["1","2","+","3","*"], "قوس")
# apl-source:47
تأكد_يساوي(الى_لاحق(["8","-","3","-","2"]), ["8","3","-","2","-"], "ترابط يساري")
# apl-source:48
