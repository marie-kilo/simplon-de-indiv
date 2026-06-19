import matplotlib.pyplot as plt

# Données collectées (Méthodes 1 à 8 pour 1k, 100k, 1M lignes)
sizes = [1000, 100000, 1000000]

# Temps médians (en secondes)
m1 = [0.381, 38.536, 341.781]
m2 = [0.125, 12.008, 111.483]
m3 = [0.123, 11.76, 108.24]
m4 = [0.034, 3.303, 27.647]
m5 = [0.014, 1.271, 10.439]
m6 = [0.007, 0.499, 4.327]   # COPY
m7 = [0.024, 2.125, 17.538]  # Pandas to_sql default
m8 = [0.063, 6.431, 51.269]  # Pandas to_sql multi

plt.figure(figsize=(12, 7))

# Traçage des lignes AVEC points (marker='o')
plt.plot(sizes, m1, marker='o', markersize=6, label='1. Boucle + commit')
plt.plot(sizes, m2, marker='o', markersize=6, label='2. Boucle + 1 commit')
plt.plot(sizes, m3, marker='o', markersize=6, label='3. executemany')
plt.plot(sizes, m4, marker='o', markersize=6, label='4. execute_batch')
plt.plot(sizes, m5, marker='o', markersize=6, label='5. execute_values')
plt.plot(sizes, m6, marker='o', markersize=8, linestyle='--', label='6. COPY (expert)')
plt.plot(sizes, m7, marker='o', markersize=6, linestyle=':', label='7. Pandas default')
plt.plot(sizes, m8, marker='o', markersize=6, linestyle=':', label='8. Pandas multi')

# Configuration de l'échelle log
plt.xscale('log')
plt.yscale('log')

# Labels et titres
plt.xlabel('Nombre de lignes (échelle log)')
plt.ylabel('Temps (secondes) (échelle log)')
plt.title('Performance des 8 méthodes d\'insertion')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, which="both", ls="-", alpha=0.2)

plt.tight_layout()
plt.show()