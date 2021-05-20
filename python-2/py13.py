from matplotlib import pyplot as plt

plt.xkcd()
x=[i for i in range(6)]
y=[i*i+5 for i in range(6)]
plt.plot(x,y,'k--',label='all countries',linewidth=3)
y=[i*i-5 for i in range(6)]
plt.plot(x,y,'b--',label='india')
plt.xlabel('women')
plt.ylabel('men per women')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig('C:/Users/Public/Pictures/Sample Pictures/pngs/plot.png')
plt.show()