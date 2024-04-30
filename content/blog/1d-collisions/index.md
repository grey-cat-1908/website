## 2. Relevance

There are numerous reasons why this project is relevant, as well as a wide range of potential applications. The following will outline the primary reasons and applications:

- It can be used in the educational process. For instance, it can be used to illustrate some principles of mechanics to students and to visualize some physics problems.
  
- It can be used to simulate some physical experiments. For instance, it can be used to simulate the one described in _G. A. Galperin's work_[^1]. 

- It can be used as a basis for future projects.

## 3. The consequences of collisions

Firstly, it is essential to comprehend how the velocity of the particles after collision is calculated. We will solve the problem in the elastic collision model (one-dimensional Newtonian).

### 3.1 With particle

Consider two particles, designated as particles `1` and `2`, with respective masses $m_1$ and $m_2$. Before the collision, the velocities of particles 1 and 2 are $v_1$ and $v_2$, respectively. After the collision, the velocities of particles 1 and 2 are $v_1'$ and $v_2'$, respectively. 

In any collision, momentum is conserved. An elastic collision is an collision, as a result of which the total kinetic energy of the colliding particles is conserved.

The conservation of momentum before and after the collision is expressed by the following equation:

$$
m_{1}\vec{v}_{1} + m_{2}\vec{v}_{2} = m_{1}\vec{v'}_{1} + m_{2}\vec{v'}_{2}
$$

And the conservation of the total kinetic energy before and after the collision is expressed by the following equation:

$$
\frac{m_{1}{v_{1}}^2}{2} + \frac{m_{2}{v_{2}}^2}{2} = \frac{m_{1}{v'_{1}}^2}{2} + \frac{m_{2}{v'_{2}}^2}{2}
$$

If we consider the law of conservation of momentum in projection on the X-axis, we can transform the previous equations into the following system:

$$
\begin{cases}
m_{1}({v_{1}} - {v'_{1}}) = m_{2}({v'_{2}} - {v_{2}}) \\
m_{1}({v_{1}}^2 - {v'_{1}}^2) = m_{2}({v'_{2}}^2 - {v_{2}}^2)
\end{cases}
$$

The division of each side of the top equation by each side of the bottom equation yields:

$$
\frac{v_{1} - v'_{1}}{{v_{1}^2} - {v'_{1}}^2} = \frac{v'_{2} - v_{2}}{{{v'_{2}}^2} - {v_{2}}^2}
$$

The preceding equation may be transformed using the difference of two squares formula to obtain the following:

$$
\frac{v_{1} - v'_{1}}{(v_1 + v'_1)(v_1 - v'_1)} = \frac{v'_{2} - v_{2}}{(v'_2 - v_2)(v'_2 + v_2)}
$$

This expression can be transformed as follows:

$$
\frac{1}{v_1 + v'_1} = \frac{1}{v'_2 + v_2}
$$

From this expression follows:

$$
v_1 + v'_1 = v'_2 + v_2
$$

From this equation, the following system can be derived:

$$
\begin{cases}
v'_1 = v_2 + v'_2 - v_1 \\
v'_2 = v_1 + v'_1 - v_2
\end{cases}
$$

The law of conservation of momentum then yields the following:

$$
\begin{cases}
m_1v_1 + m_2v_2 = m_1{v'}_1 + m_2(v_1 + {v'}_1 - v_2) \\
m_1v_1 + m_2v_2 = m_1(v_2 + v'_2 - v_1) + m_2v'_2
\end{cases}
$$

From this, we can derive the velocity of the particles following the collision as follows:

$$
\begin{cases}
v'_1 = \frac{2m_2v_2 + v_1(m_1-m_2)}{m_1+m_2} \\
v'_2 = \frac{2m_1v_1 + v_2(m_2-m_1)}{m_1+m_2}
\end{cases}
$$

### 3.2 With wall

Consider particle and a wall with respective masses $m$ and $m_w \rightarrow \infty$. Before the collision, the velocities of the particle and the wall are $v$ and $v_w = 0$, respectively. After the collision, the velocities of the particle and the wall are $v'$ and $v_w'$, respectively. 

In order to proceed, we will utilize the formulas derived in section **3.1**.

The velocity of the particle will take the following form:

$$
v' = \lim\limits_{m_w \to \infty} \frac{2m_wv_w + v(m-m_w)}{m+m_w} = \lim\limits_{m_w \to \infty} \frac{v(m-m_w)}{m+m_w} = -v
$$

The velocity of the wall will take the following form:

$$
v_w' = \lim\limits_{m_w \to \infty} \frac{2mv + v_w(m_w-m)}{m+m_w} = \lim\limits_{m_w \to \infty} \frac{2mv}{m+m_w} = 0
$$

This leads to the conclusion that the wall will not change its position, but the particle will change its velocity value to the opposite.

---

## Note

* If you decide to use this project as the basis of your project, it would be advisable to [contact me](https://arbuz.icu/mail) first.

* If you have any interesting projects that I could be involved in, or if you would like to contact me, you can do so [here](https://arbuz.icu/mail).

- - - 

## Reference 

[^1]: Galperin G. A., ["PLAYING POOL WITH π (THE NUMBER π FROM A BILLIARD POINT OF VIEW)"](http://rcd.ics.org.ru/RD2003v008n04ABEH000252/), Regular and Chaotic Dynamics, 2003, Volume 8, Number 4, pp. 375-394 DOI: [10.1070/RD2003v008n04ABEH000252](http://rcd.ics.org.ru/RD2003v008n04ABEH000252/)
