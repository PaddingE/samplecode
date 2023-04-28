#%%
list_kakao = ["다현", "정연", "쯔위", "사나", "지효"]
print(list_kakao)
# %%
print(list_kakao[0])
print(list_kakao[4])
# %%
list_kakao.append(None)
print(list_kakao)
# %%
list_kakao[5] = "모모"
print(list_kakao)
# %%
list_kakao.append(None)
print(list_kakao)
# %%
list_kakao[6] = list_kakao[5]
list_kakao[5] = None
print(list_kakao)
# %%
list_kakao[5] = list_kakao[4]
list_kakao[4] = None
list_kakao[4] = list_kakao[3]
list_kakao[3] = None
print(list_kakao)
# %%
list_kakao[3] = "미나"
print(list_kakao)
# %%
list_kakao[4] = None
print(list_kakao)
# %%
list_kakao[4] = list_kakao[5]
list_kakao[5] = None
list_kakao[5] = list_kakao[6]
list_kakao[6] = None
print(list_kakao)
# %%
del(list_kakao[6])
print(list_kakao)
# %%
