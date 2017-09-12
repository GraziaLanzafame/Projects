import numpy as np
import matplotlib.pyplot as plt


def initialphi(x):
	return np.where(x%1. <0.5, np.power(np.sin(2*x*np.pi), 2), 0)

#space setup
nx=20
nt=20
diff=0.00001
dx=1./nx
dt=1./nt
coeff=(diff*dt)/(dx**2)

#variables
x=np.linspace(0.0, 1.0, nx+1)
t=np.linspace(0.0, 1.0, nt+1)

#indipendent variable
phi=initialphi(x)
phiNew=phi.copy()
phiOld=phi.copy()

#FTCS
#loop over space
for j in xrange(1, nx):
	phi[j]=phiOld[j]+coeff*(phiOld[j+1]-2*phiOld[j]+phiOld[j-1])
#periodic boundary conditions
phi[0]=phiOld[0]+coeff*(phiOld[1]-2*phiOld[0]+phiOld[nx-1])
phi[nx]=phi[0]

#loop over time
for n in xrange(1,nt):
	#loop over space
	phiNew[j]=phiOld[j]-coeff*(phi[j+1]-2*phi[j]+phi[j-1])
	#periodic boundary conditions
	phiNew[0]=phiOld[0]-coeff*(phi[1]-2*phi[0]+phi[nx-1])
	phiNew[nx]=phiNew[0]
	
	#update phi for the next time step
	phiOld=phi.copy()
	phi=phiNew.copy()

#Plot solutions
#plt.plot(x, initialphi(x-t), 'k', label='analytic')
plt.plot(x, phi, 'b', label='CTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()
