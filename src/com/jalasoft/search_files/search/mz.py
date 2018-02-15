# import os
# # import getpass
# # # import win32pdh, string, win32api
# # # from win32com.server.exception import COMException
# # # import win32com.server.util
# # # import win32com.client.dynamic
# import win32security
# #
# # # import grp
# # # from stat import ST_UID
# # #
# # # import pwd
# # # import os.path
# # #
# work_dir = "D:\MauricioZ\Documments\Personal\\videos\\Franco Escamilla futbol y mujeres.mp4"
# # # new_dir = "path"
# # fp = open(work_dir)
# # st = os.fstat(fp.fileno())
# # userinfo = pwd.getpwuid(st[ST_UID])
# #
# (uid) = os.stat(work_dir)
#
# print(uid)
# # print(os.getlogin())
# # # print(os.environ["Administrator"])
# # username = getpass.getuser(uid)
# # print(username)
# desc = win32security.GetFileSecurity(uid)
# sid = desc.GetSecurityDescriptorOwner()
# account, domain, typecode = win32security.LookupAccountSid(None, sid)
# print(domain + u'\\' + account)
import win32api
import win32con
import win32security

FILENAME = "D:\MauricioZ\Documments\Personal\\videos\Franco Escamilla futbol y mujeres.mp4"
# open(FILENAME, "w").close()
#
# print("I am", win32api.GetUserNameEx (win32con.NameSamCompatible))

sd = win32security.GetFileSecurity(FILENAME, win32security.OWNER_SECURITY_INFORMATION)
owner_sid = sd.GetSecurityDescriptorOwner()
name, domain, type = win32security.LookupAccountSid(None, owner_sid)

print("File owned by %s\\%s" % (domain, name))
