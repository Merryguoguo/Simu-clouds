# Simu-Cloud :cloud:

This repository is creater for cloud simulation proposed in [paper](https://doi.org/10.1016/j.isprsjprs.2023.10.014).  
****  
####  :cloud:Generated Cloud
- Natural scene  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/22b24757-3bd1-425c-af39-485bcdad45b2)
- Fourier Transform Map  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/0806c01d-328b-4630-b95b-96ba793ed626)


#### 	:earth_americas:Underlying Clean Image (RSI, RGB)
- Natural scene  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/ca347841-341d-4a1a-83ee-4bde7265d60f)
- Fourier Transform Map  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/ecdfe81a-81c0-4a60-9c40-82d837c43845)


#### 	💫:Simulated Cloudy Image (RSI, RGB)
- Natural scene  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/1d5506ad-59d5-4cc8-be1e-84e65731a8cb)
- Fourier Transform Map  
![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/d991e938-6f88-42b6-aa83-d17096d085cc)


### :star2:Overall Transforming
<img width="500" height="300" src="https://github.com/Merryguoguo/Simu-clouds/assets/54757576/3d939061-1490-4a86-a0e5-f1e7ece9b968"/>

****  
### :label:Implementation
1. Cloud creation
   **********
   <img width="300" height="200" src="https://github.com/Merryguoguo/Simu-clouds/assets/54757576/6f706c83-23b1-43df-8b74-cb4d986e25b8"/>
   
    :petri_dish:Simplex noise  
     For N dimensions space,   
     pick the simplest and most compact shape  
     that can be repeated to fill the entire space.
     + One dimension  
       ![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/3d8889bf-4b3e-4de7-816f-15b2ae61094f)  
     + Two dimensions  
       ![image](https://github.com/Merryguoguo/Simu-clouds/assets/54757576/10a6d40f-e398-4e49-8dee-1ed70b75cff0)
     + Three dimensions    
       <img width="375" height="150" src="https://github.com/Merryguoguo/Simu-clouds/assets/54757576/c63f1e78-bc01-4088-9cab-99ef313afd82"/>
     + N dimensions...
   **********
3. Alpha Blending  
   ```
   R(cldy) = α*R(cld) + (1-α)*R(bg)
   G(cldy) = α*G(cld) + (1-α)*G(bg)
   B(cldy) = α*B(cld) + (1-α)*B(bg)
   ```     
****  
:crescent_moon: Auxiliary files for further understanding  
Perlin, K., 2001. Real-Time Shading SIGGRAPH Course Notes.

### Citing 
If you find this code/data useful in your research then please cite our [paper](https://doi.org/10.1016/j.isprsjprs.2023.10.014):
```
Guo, Y., He, W., Xia, Y., & Zhang, H. (2023). Blind single-image-based thin cloud removal using a cloud perception integrated fast Fourier convolutional network. ISPRS Journal of Photogrammetry and Remote Sensing, 206, 63–86. https://doi.org/10.1016/j.isprsjprs.2023.10.014
```



