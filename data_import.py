import numpy as np
import json
import scipy
from scipy.spatial.transform import Rotation as R

with open('humanoid3d_walk.json', 'r') as f:
    data = json.load(f)
    # print(data.get('Frames'))   
    # print(data['Frames'][0])    
    # print(data['Frames'][0][0])    
print(len(data['Frames']))
print(data['Frames'][24][15])

A = np.empty([12,len(data['Frames'])])
for i in [0,len(data['Frames'])-1]:
    #right hip
    r = R.from_quat([data['Frames'][i][16], data['Frames'][i][17], data['Frames'][i][18], data['Frames'][i][19]])
    A[8, i] = r.as_euler('xyz')[0] #right hip pitch
    A[6, i] = r.as_euler('xyz')[1] #right hip yaw
    A[7, i] = r.as_euler('xyz')[2] #right hip roll
    # print(r.as_euler('xyz')[0])

    #right knee
    A[9, i] = r2 = data['Frames'][i][20]
    
    #right ankle
    r3 = R.from_quat([data['Frames'][i][21], data['Frames'][i][22], data['Frames'][i][23], data['Frames'][i][24]])
    A[10, i] = r3.as_euler('xyz')[0] #right ankle pitch
    A[11, i] = r3.as_euler('xyz')[1] #right ankle roll
    r3.as_euler('xyz')[2] #right ankle yaw

    #left hip
    r4 = R.from_quat([data['Frames'][i][30], data['Frames'][i][31], data['Frames'][i][32], data['Frames'][i][33]])
    A[2, i] = r4.as_euler('xyz')[0] #left hip pitch
    A[0, i] = r4.as_euler('xyz')[1] #left hip yaw
    A[1, i] = r4.as_euler('xyz')[2] #letf hip roll

    #left knee
    A[3, i] = r5 = data['Frames'][i][34]

    #left ankle
    r6 = R.from_quat([data['Frames'][i][35], data['Frames'][i][36], data['Frames'][i][37], data['Frames'][i][38]])
    A[4, i] = r6.as_euler('xyz')[0] #left ankle pitch
    A[5, i] = r6.as_euler('xyz')[2] #left ankle roll  
    r6.as_euler('xyz')[1] #left ankle yaw
print(A)
print(A.shape)
np.savetxt('walk_data.csv', A, delimiter=",")