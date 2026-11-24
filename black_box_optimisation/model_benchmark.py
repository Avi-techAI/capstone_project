import sys, json, warnings, numpy as np
warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
from visualise_progress import rank_gauss, standardise, TRANSFORM
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel as C, Matern, WhiteKernel, RBF, RationalQuadratic
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from scipy.stats import spearmanr
sub=json.load(open('submissions.json'))
NOISE={'F1':1e-8,'F2':0.043,'F3':0.0015,'F4':1e-5,'F5':0.0015,'F6':0.0151,'F7':1e-6,'F8':1e-8}

def load(k):
    i=k[1]; X=np.load(f'initial_data/function_{i}/initial_inputs.npy'); Y=np.load(f'initial_data/function_{i}/initial_outputs.npy')
    for w in sorted(sub['functions'][k]['weeks'],key=int):
        d=sub['functions'][k]['weeks'][w]
        if d['output'] is not None:
            X=np.vstack([X,np.array(d['input']).reshape(1,-1)]); Y=np.append(Y,d['output'])
    return X,Y

def models(d,nz):
    return {
 'GP-Matern'  : GaussianProcessRegressor(kernel=C(1.,(1e-3,1e3))*Matern(np.ones(d),nu=2.5,length_scale_bounds=(.05,3.))+WhiteKernel(max(nz**2,1e-10),(1e-10,1.)),normalize_y=False,n_restarts_optimizer=2,random_state=0),
 'GP-RBF'     : GaussianProcessRegressor(kernel=C(1.,(1e-3,1e3))*RBF(np.ones(d),length_scale_bounds=(.05,3.))+WhiteKernel(max(nz**2,1e-10),(1e-10,1.)),normalize_y=False,n_restarts_optimizer=2,random_state=0),
 'GP-RatQuad' : GaussianProcessRegressor(kernel=C(1.,(1e-3,1e3))*RationalQuadratic(length_scale_bounds=(.05,3.))+WhiteKernel(max(nz**2,1e-10),(1e-10,1.)),normalize_y=False,n_restarts_optimizer=2,random_state=0),
 'RandomForest': RandomForestRegressor(n_estimators=150,random_state=0,n_jobs=-1),
 'ExtraTrees' : ExtraTreesRegressor(n_estimators=150,random_state=0,n_jobs=-1),
 'GradBoost'  : GradientBoostingRegressor(n_estimators=200,max_depth=3,learning_rate=.08,random_state=0),
 'SVR-RBF'    : make_pipeline(SVR(C=10.,gamma='scale',epsilon=.05)),
 'KNN-5'      : KNeighborsRegressor(n_neighbors=min(5,4),weights='distance'),
 'MLP-net'    : MLPRegressor(hidden_layer_sizes=(64,64),max_iter=1500,random_state=0,learning_rate_init=.01),
 'Poly2-Ridge': make_pipeline(PolynomialFeatures(2),RidgeCV(alphas=np.logspace(-4,3,30))),
}
names=list(models(2,0).keys())
print(f"{'Function':<10}" + ''.join(f'{n[:11]:>12}' for n in names))
print('-'*(10+12*len(names)))
best={}
for k in [f'F{i}' for i in range(1,9)]:
    X,Y=load(k); d=X.shape[1]
    z=rank_gauss(Y) if TRANSFORM[k]=='rank' else standardise(Y)
    nz=NOISE[k]/Y.std() if TRANSFORM[k]=='raw' else .05
    row=f'{k+" (n="+str(len(X))+")":<10}'; sc={}
    for n in names:
        p=np.empty(len(X))
        for i in range(len(X)):
            m=np.ones(len(X),bool); m[i]=False
            mdl=models(d,nz)[n]
            mdl.fit(X[m],z[m]); p[i]=mdl.predict(X[i:i+1])[0]
        r=spearmanr(Y,p).correlation
        r=0. if np.isnan(r) else r
        sc[n]=r; row+=f'{r:>12.3f}'
    best[k]=sorted(sc,key=lambda n:-sc[n])[:3]
    print(row)
print()
print('Top-3 surrogate per function (by Spearman on held-out points):')
for k,v in best.items(): print(f'  {k}: {v[0]}  |  {v[1]}  |  {v[2]}')
json.dump(best,open('/tmp/best_models.json','w'))
