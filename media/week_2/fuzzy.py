import matplotlib.pyplot as plt

a_few = {1:1,5:1,12:0,100:0}
many = {1:0,9:0,50:1,100:1}

plt.plot(a_few.keys(),a_few.values())
plt.plot(many.keys(),many.values())
plt.legend(['A few','Many'])
plt.savefig('fuzzy.png')
plt.show()
