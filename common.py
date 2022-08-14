import random


############################################################
# ランダム値生成　重複なし
#   戻り値: int型のリスト
############################################################
def random_ints_nodup(min, max, num):
    ns = []
    while len(ns) < num:
        n = random.randint(min, max)
        if not n in ns:
            ns.append(n)
    return ns