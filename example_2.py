# Illustrate how to use DAPPER to benchmark multiple DA methods

from common import *

sd0 = seed(9)

##############################
# DA Configurations
##############################
cfgs  = List_of_Configs()

from mods.Lorenz63.sak12 import setup ##################### Expected RMSE_a:
#cfgs += Climatology()  # no tuning!                       # 7.6
#cfgs += OptInterp()    # no tuning!                       # 1.25
cfgs += Var3D(infl=0.9)# tuning not strictly required     # 1.03 
#cfgs += ExtKF(infl=90) # some inflation tuning needed     # 0.87
#cfgs += EnKF('Sqrt',   N=3 ,  infl=1.30)                  # 0.82
#cfgs += EnKF('Sqrt',   N=10,  infl=1.02,rot=True)         # 0.63
cfgs += EnKF('PertObs',N=50, infl=0.95,rot=False)        # 0.56
#cfgs += EnKF_N(        N=10,            rot=True)         # 0.54
#cfgs += iEnKS('Sqrt',  N=10,  infl=1.02,rot=True)         # 0.31
#cfgs += PartFilt(      N=100 ,reg=2.4  ,NER=0.3)          # 0.38
cfgs += PartFilt(N=50 ,NER=0.3 ,reg=5)          # 0.28
cfgs += OptPF(   N=50 ,NER=0.25,reg=1.4,Qs=0.4)    # 0.37
#cfgs += PartFilt(      N=4000,reg=0.7  ,NER=0.05)         # 0.27
#cfgs += PFxN(xN=1000,  N=30  ,Qs=2     ,NER=0.2)          # 0.56

#from mods.Lorenz95.sak08 import setup ##################### Expected RMSE_a:
#cfgs += ExtKF(infl=6)
#cfgs += EnKF(PertObs',N=40,infl=1.06)                     # 0.22
#cfgs += EnKF(DEnKF  ',N=40,infl=1.01)                     # 0.18
#cfgs += EnKF(PertObs',N=28,infl=1.08)                     # 0.24
#cfgs += EnKF(Sqrt   ',N=24,infl=1.02,rot=True)            # 0.18
#
#cfgs += EnKF_N(N=24,rot=True)                             # 0.18
#cfgs += iEnKS('Sqrt',N=40,infl=1.01,rot=True)             # 0.17
#
#cfgs += LETKF(         N=7,rot=True,infl=1.04,loc_rad=4)  # 0.22
#cfgs += LETKF(approx=1,N=8,rot=True,infl=1.25,loc_rad=4)  # 0.36
#cfgs += SL_EAKF(       N=7,rot=True,infl=1.07,loc_rad=6)  # 0.23


#from mods.LA.raanes2015 import setup
#from mods.Lorenz95.spectral_obs import setup
#from mods.Lorenz95.raanes2016 import setup
#from mods.LorenzUV.wilks05_full import setup
#from mods.Lorenz84.harder import setup
# -- Get suggested tuning from setup files --


##############################
# Generate synthetic truth/obs
##############################
# Adjust experiment duration
setup.t.T = 100

xx,yy = simulate(setup)


##############################
# Assimilate
##############################
stats = []
avrgs = []

for ic,config in enumerate(cfgs):
  #config.store_u = True
  #config.liveplotting = True
  seed(sd0+2)

  stats += [ config.assimilate(setup,xx,yy) ]
  avrgs += [ stats[ic].average_in_time() ]
  #print_averages(config, avrgs[-1])
print_averages(cfgs,avrgs)

# Note: if model is very large, you may want to
# discard the stats objects, keeping only the avrgs.

##############################
# Plot
##############################
plot_time_series   (stats[-1])
#plot_3D_trajectory (stats[-1])
#plot_err_components(stats[-1])
#plot_rank_histogram(stats[-1])
#plot_hovmoller     (xx,setup.t)



