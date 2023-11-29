import numpy as np
from matplotlib import pyplot as plt
n=100
bound_left=600
bound_right=273
bound_top=273
bound_down=273
omega=0.25
omega_1=1-omega
m=n-2
TEMP_field=np.zeros((n,n))
TEMP_FREQ_0=np.zeros((n,n))
TEMP_FREQ_1=np.zeros((n,n))
TEMP_FREQ_2=np.zeros((n,n))
TEMP_FREQ_3=np.zeros((n,n))
TEMP_FREQ_4=np.zeros((n,n))
TEMP_FREQ_5=np.zeros((n,n))
TEMP_FREQ_6=np.zeros((n,n))
TEMP_FREQ_7=np.zeros((n,n))
TEMP_FREQ_8=np.zeros((n,n))
TEMP_FREQ_9=np.zeros((n,n))

TEMP_FREQ_0e=np.zeros((n,n))
TEMP_FREQ_1e=np.zeros((n,n))
TEMP_FREQ_2e=np.zeros((n,n))
TEMP_FREQ_3e=np.zeros((n,n))
TEMP_FREQ_4e=np.zeros((n,n))
TEMP_FREQ_5e=np.zeros((n,n))
TEMP_FREQ_6e=np.zeros((n,n))
TEMP_FREQ_7e=np.zeros((n,n))
TEMP_FREQ_8e=np.zeros((n,n))
TEMP_FREQ_9e=np.zeros((n,n))

TEMP_FREQ_0a=np.zeros((n,n))
TEMP_FREQ_1a=np.zeros((n,n))
TEMP_FREQ_2a=np.zeros((n,n))
TEMP_FREQ_3a=np.zeros((n,n))
TEMP_FREQ_4a=np.zeros((n,n))
TEMP_FREQ_5a=np.zeros((n,n))
TEMP_FREQ_6a=np.zeros((n,n))
TEMP_FREQ_7a=np.zeros((n,n))
TEMP_FREQ_8a=np.zeros((n,n))
TEMP_FREQ_9a=np.zeros((n,n))

FREQ_0=np.zeros((n,n))
FREQ_1=np.zeros((n,n))
FREQ_2=np.zeros((n,n))
FREQ_3=np.zeros((n,n))
FREQ_4=np.zeros((n,n))
FREQ_5=np.zeros((n,n))
FREQ_6=np.zeros((n,n))
FREQ_7=np.zeros((n,n))
FREQ_8=np.zeros((n,n))
            
for i1 in range(0,n-1):
    TEMP_field[0,i1]=bound_top
    TEMP_field[i1,0]=bound_left
    TEMP_field[i1,n-1]=bound_right
    TEMP_field[n-1,i1]=bound_down
TEMP_field[n-1,n-1]=bound_right
TEMP_field[n-1,0]=bound_left

for i in range(1,n-1):
    for j in range(1,n-1):
        TEMP_field[i,j]=273;
print(TEMP_field)
for i in range(0,n):
        for j in range(0,n):
            TEMP_FREQ_0[i,j]=(TEMP_field[i,j])/9
            TEMP_FREQ_1[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_2[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_3[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_4[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_5[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_6[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_7[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_8[i,j]=TEMP_field[i,j]/9
            TEMP_FREQ_9[i,j]=TEMP_field[i,j]/9

for t in range(4000 ):
    


    for i in range(0,n):
        for j in range(0,n):
            FREQ_0[i,j]=(TEMP_field[i,j]*4)/9

            FREQ_1[i,j]=(TEMP_field[i,j])/9
            FREQ_3[i,j]=(TEMP_field[i,j])/9
            FREQ_5[i,j]=(TEMP_field[i,j])/9
            FREQ_7[i,j]=(TEMP_field[i,j])/9
        
            FREQ_2[i,j]=(TEMP_field[i,j])/36
            FREQ_4[i,j]=(TEMP_field[i,j])/36
            FREQ_6[i,j]=(TEMP_field[i,j])/36
            FREQ_8[i,j]=(TEMP_field[i,j])/36



    for i in range(0,n):
        for j in range(0,n):
            TEMP_FREQ_0a[i,j]=omega_1*TEMP_FREQ_0[i,j]+omega*FREQ_0[i,j]
            TEMP_FREQ_1a[i,j]=omega_1*TEMP_FREQ_1[i,j]+omega*FREQ_1[i,j]
            TEMP_FREQ_2a[i,j]=omega_1*TEMP_FREQ_2[i,j]+omega*FREQ_2[i,j]
            TEMP_FREQ_3a[i,j]=omega_1*TEMP_FREQ_3[i,j]+omega*FREQ_3[i,j]
            TEMP_FREQ_4a[i,j]=omega_1*TEMP_FREQ_4[i,j]+omega*FREQ_4[i,j]
            TEMP_FREQ_5a[i,j]=omega_1*TEMP_FREQ_5[i,j]+omega*FREQ_5[i,j]
            TEMP_FREQ_6a[i,j]=omega_1*TEMP_FREQ_6[i,j]+omega*FREQ_6[i,j]
            TEMP_FREQ_7a[i,j]=omega_1*TEMP_FREQ_7[i,j]+omega*FREQ_7[i,j]
            TEMP_FREQ_8a[i,j]=omega_1*TEMP_FREQ_8[i,j]+omega*FREQ_8[i,j]
    TEMP_FREQ_1=TEMP_FREQ_1a
    TEMP_FREQ_2=TEMP_FREQ_2a
    TEMP_FREQ_3=TEMP_FREQ_3a
    TEMP_FREQ_4=TEMP_FREQ_4a
    TEMP_FREQ_5=TEMP_FREQ_5a
    TEMP_FREQ_6=TEMP_FREQ_6a
    TEMP_FREQ_7=TEMP_FREQ_7a
    TEMP_FREQ_8=TEMP_FREQ_8a
    TEMP_FREQ_0=TEMP_FREQ_0a


    for i in range(0,n):
        for j in range(0,n):
            if(i==0):
                if (j>0 and j<n-1):
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_3[i,j]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_2[i,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_4[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_2[i+1,j-1]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_4[i+1,j+1]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]

                elif(j==0):
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_4[i,j]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_3[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_5[i,j]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_6[i,j]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_2[i,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_4[i+1,j+1]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                elif(j==n-1):
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_8[i,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_4[i,j]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_2[i,j]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_3[i,j]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_1[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_2[i+1,j-1]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                
                
                 
            elif(i==n-1):
                if (j>0 and j<n-1):
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_6[i,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_8[i,j]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_7[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_6[i-1,j+1]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_8[i-1,j-1]
                elif (j==0):
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_5[i,j]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_6[i,j]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_7[i,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_8[i,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_4[i,j]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_6[i-1,j+1]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                elif(j==n-1):
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_6[i,j]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_2[i,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_8[i-1,j-1]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_7[i,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_8[i,j]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_1[i,j]
                                      
                
                
            elif(j==0):
                if (i>0 and i<n-1):
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_4[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_5[i,j]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_6[i,j]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_4[i+1,j+1]
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_6[i-1,j+1]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                
            elif (j==n-1):
                if(i>0 and i<n-1):
                    TEMP_FREQ_5e[i,j]=TEMP_FREQ_1[i,j]
                    TEMP_FREQ_6e[i,j]=TEMP_FREQ_2[i,j]
                    TEMP_FREQ_4e[i,j]=TEMP_FREQ_8[i,j]
                    TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                    TEMP_FREQ_2e[i,j]=TEMP_FREQ_2[i+1,j-1]
                    TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                    TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                    TEMP_FREQ_8e[i,j]=TEMP_FREQ_8[i-1,j-1]

            else:
                TEMP_FREQ_1e[i,j]=TEMP_FREQ_1[i,j-1]
                TEMP_FREQ_2e[i,j]=TEMP_FREQ_2[i+1,j-1]
                TEMP_FREQ_3e[i,j]=TEMP_FREQ_3[i+1,j]
                TEMP_FREQ_4e[i,j]=TEMP_FREQ_4[i+1,j+1]
                TEMP_FREQ_5e[i,j]=TEMP_FREQ_5[i,j+1]
                TEMP_FREQ_6e[i,j]=TEMP_FREQ_6[i-1,j+1]
                TEMP_FREQ_7e[i,j]=TEMP_FREQ_7[i-1,j]
                TEMP_FREQ_8e[i,j]=TEMP_FREQ_8[i-1,j-1]
        
    TEMP_FREQ_1=TEMP_FREQ_1e
    TEMP_FREQ_2=TEMP_FREQ_2e
    TEMP_FREQ_3=TEMP_FREQ_3e
    TEMP_FREQ_4=TEMP_FREQ_4e
    TEMP_FREQ_5=TEMP_FREQ_5e
    TEMP_FREQ_6=TEMP_FREQ_6e
    TEMP_FREQ_7=TEMP_FREQ_7e
    TEMP_FREQ_8=TEMP_FREQ_8e
    for i in range(0,n):
        for j in range(0,n):
            TEMP_field[i,j]=TEMP_FREQ_0[i,j]+TEMP_FREQ_1[i,j]+TEMP_FREQ_2[i,j]+TEMP_FREQ_3[i,j]+TEMP_FREQ_4[i,j]+TEMP_FREQ_5[i,j]+TEMP_FREQ_6[i,j]+TEMP_FREQ_7[i,j]+TEMP_FREQ_8[i,j]
    for i in range(0,n):
        TEMP_field[i,0]=600
        TEMP_field[0,i]=273
        TEMP_field[n-1,i]=273
        TEMP_field[i,n-1]=273
    print(TEMP_field)
    plt.rcParams["figure.figsize"] = [4,4]
    plt.rcParams["figure.autolayout"] = True
    data2D = np.random.random((30,30))
    im = plt.imshow(TEMP_field, cmap='jet')
    plt.colorbar(im)
    plt.show()
                
        
        
        
    print(t)
    plt.rcParams["figure.figsize"] = [4,4]
    plt.rcParams["figure.autolayout"] = True
    data2D = np.random.random((30,30))
    im = plt.imshow(TEMP_field, cmap='jet')
    plt.colorbar(im)
    plt.show()
    
        
    

                                          
            
            

        
        
       
























