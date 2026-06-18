import matplotlib.pyplot as plt

# Données
sizes = [1000, 100000, 1000000]
m1 = [0.381, 38.536, 341.781]
m2 = [0.125, 12.008, 111.483]
m3 = [0.123, 11.76, 108.24]
m4 = [0.035, 3.313, 30.116]
m5 = [0.015, 1.289, 11.454]

plt.figure(figsize=(10, 6))
plt.plot(sizes, m1, marker='o', label='Boucle + commit')
plt.plot(sizes, m2, marker='o', label='Boucle + 1 commit')
plt.plot(sizes, m3, marker='o', label='executemany')
plt.plot(sizes, m4, marker='o', label='execute_batch')
plt.plot(sizes, m5, marker='o', label='execute_values')

plt.xscale('log')
plt.yscale('log') # Indispensable pour comparer les ordres de grandeur
plt.xlabel('Nombre de lignes')
plt.ylabel('Temps (secondes)')
plt.title('Performance des méthodes d\'insertion (Échelle log)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()