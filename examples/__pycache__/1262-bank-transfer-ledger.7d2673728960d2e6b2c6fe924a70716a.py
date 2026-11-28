
# apl-source:1
# مثال 1262 — دفتر تحويلات
# apl-source:2
# Transfer ledger with rollback
# apl-source:3
# Demonstrates: معاملات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1262-bank-transfer-ledger.apl
# apl-source:6

# apl-source:7
# التحويل ينجح فقط لو كفى الرصيد
# apl-source:8
# وندون كل عملية في دفتر
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
class دفتر:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.ارصدة = {}
    # apl-source:21
    ذات.سجل = []
# apl-source:22

  # apl-source:23
  def افتح(ذات, اسم, مبلغ):
    # apl-source:24
    ذات.ارصدة[اسم] = مبلغ
# apl-source:25

  # apl-source:26
  def حول(ذات, من, الى, مبلغ):
    # apl-source:27
    if ذات.ارصدة[من] < مبلغ:
      # apl-source:28
      ذات.سجل = ذات.سجل + [["رفض", من, الى, مبلغ]]
      # apl-source:29
      return False
    # apl-source:30
    ذات.ارصدة[من] = ذات.ارصدة[من] - مبلغ
    # apl-source:31
    ذات.ارصدة[الى] = ذات.ارصدة[الى] + مبلغ
    # apl-source:32
    ذات.سجل = ذات.سجل + [["نجح", من, الى, مبلغ]]
    # apl-source:33
    return True
# apl-source:34

  # apl-source:35
  def تراجع(ذات):
    # apl-source:36
    if len(ذات.سجل) == 0:
      # apl-source:37
      return False
    # apl-source:38
    ع = ذات.سجل.pop()
    # apl-source:39
    if ع[0] == "نجح":
      # apl-source:40
      ذات.ارصدة[ع[1]] = ذات.ارصدة[ع[1]] + ع[3]
      # apl-source:41
      ذات.ارصدة[ع[2]] = ذات.ارصدة[ع[2]] - ع[3]
    # apl-source:42
    return True
# apl-source:43

# apl-source:44
د = دفتر()
# apl-source:45
د.افتح("a", 100)
# apl-source:46
د.افتح("b", 50)
# apl-source:47
تأكد_يساوي(د.حول("a", "b", 30), True, "نجح")
# apl-source:48
تأكد_يساوي(د.ارصدة["b"], 80, "رصيد b")
# apl-source:49
تأكد_يساوي(د.حول("b", "a", 500), False, "رُفض")
# apl-source:50
د.تراجع()
# apl-source:51
تأكد_يساوي(د.ارصدة["a"], 70, "الرفض لا يغير")
# apl-source:52
د.تراجع()
# apl-source:53
تأكد_يساوي(د.ارصدة["a"], 100, "تراجع عن التحويل")
# apl-source:54
تأكد_يساوي(د.ارصدة["b"], 50, "رصيد b أصلي")
# apl-source:55
