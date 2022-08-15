import random
import string


############################################################
# ランダム値生成　重複なし
#   引数: min=最小値,max=最大値,num=取得するランダム値の個数
#   戻り値: int型のリスト
############################################################
def random_ints_nodup(min, max, num):
    ns = []
    while len(ns) < num:
        n = random.randint(min, max)
        if not n in ns:
            ns.append(n)
    return ns


############################################################
# ランダム文字列生成
#   引数: n=文字数
#   戻り値: str型
############################################################
def random_str(n):
   random_lst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(random_lst)