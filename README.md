# School-Project
<h2>一、画图</h2>

1.变形vk图：画个跟这个一样的图，就是按这些不同分组的数据画

![2d461dee6820d9c78921dfe69c01ba9](https://github.com/lmq14159/Others-project/assets/82321147/a847f319-95db-4303-a824-fca46936540e)

2.kmd：用给的数据文件（1.csv）的数据画，D列数据为X轴，Z列数据为Y轴

<img width="357" alt="f57689c792cf6427ae4f2220e17e506" src="https://github.com/lmq14159/Others-project/assets/82321147/dfaf4e83-5522-4ae4-a1b5-d5c5b6087530">

3.百分比图：用给定的百分比的文件里的数据画，这个有五个柱

![8568cdde0968a3ae474e4268e9e663c](https://github.com/lmq14159/Others-project/assets/82321147/3e996159-945d-4a63-96f3-c1d1bddfbca0)+

![7b6ca7d10879ce5dabff5d1d53e03ac](https://github.com/lmq14159/Others-project/assets/82321147/ae717aa3-b555-4b10-9103-84416809943d)

4.dbc-c图：用给定的数据文件（1.csv）的相应数据画图

![image](https://github.com/lmq14159/Others-project/assets/82321147/1ba28827-ee94-4938-a6c2-715f3444989a)



===================================================================================================

<h2>二、非靶向质谱版(统计版)</h2>
在现在的基础上修改：</br>
1.分子量需要通过iupac文件换算后替换原来的分子量；</br>
2.最后的展示文件（count.csv）需要加上各自的强度（原始数据的strength这一列）；</br>
3.最后需要将相同的分子质量差的结果的个数由高到低排序后进行输出；</br>
4.需要能同时处理多个文件。



===================================================================================================



<h2>三、网络分析</h2>
使用igraph等网络分析工具创建网络并计算参数。</br>
使用节点和边文件创建网络，然后计算：网络的度（Degree，与某个分子有联系的分子数量）、 度中心性（Degree centrality， 体现分子核心性（重要性）， 该值越大说明该分子越重要，属于较活跃的分子，反之，该分子较不活跃）、 亲密中心性（Closeness centrality，体现分子影响力，该值越大说明该分子在整个样品中的辐射能力约强，即，除了与近端分子有直接联系，还可能与远端分子存在间接联系）、间接中心性（Betweenness centrality，体现分子作为中间过渡性分子的重要性，数值越大说明该分子在整个网络中具有较强的连接作用）、 特征向量中心性（Eigenvector centrality，体现分子与邻近核心分子的关系，数值较大说明该分子与很多核心分子存在关系，该分子属于核心分子的联系或过渡分子）。 </br>
参考资料：</br>
https://python.igraph.org/en/stable/generation.html</br>
https://cloud.tencent.com/developer/article/1625275</br>
https://zhuanlan.zhihu.com/p/426397948

