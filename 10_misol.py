import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

plt.plot(kunlar, daromad, label="Daromad", marker="o")

plt.title("Haftalik daromad")
plt.xlabel("Kunlar")
plt.ylabel("Daromad")

plt.legend()
plt.grid()

plt.savefig("daromad.png")
plt.show()