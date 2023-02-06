N = list(map(int, input("Introduceti elementele listei N separate prin spatiu: ").split()))
K = int(input("Introduceti valoarea lui K: "))

def seturi(lst, k):
    seturi = []
    for i in range(len(lst) - k + 1):
        set_curent = []
        for j in range(k):
            set_curent.append(lst[i + j])
        if len(set(set_curent)) == k:
            seturi.append(set_curent)
    return seturi

seturi_unice = seturi(N, K)
print(f"Sunt {len(seturi_unice)} seturi fara numere asemanatoare:")
print(seturi_unice)
