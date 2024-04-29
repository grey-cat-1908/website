
## 3.

Firstly, it is essential to comprehend how the velocity of the particles after collision is calculated. We will solve the problem in the elastic collision model (one-dimensional Newtonian).

### 3.1

Consider two particles, designated as particles `1` and `2`, with respective masses $m_1$ and $m_2$. Before the collision, the velocities of particles 1 and 2 are $v_1$ and $v_2$, respectively. After the collision, the velocities of particles 1 and 2 are $v_1'$ and $v_2'$, respectively. 

In any collision, momentum is conserved. An elastic collision is an collision, as a result of which the total kinetic energy of the colliding particles is conserved.


$$
m_{1}\vec{v}_{1} + m_{2}\vec{v}_{2} = m_{1}\vec{v'}_{1} + m_{2}\vec{v'}_{2}
$$

$$
\frac{m_{1}{v_{1}}^2}{2} + \frac{m_{2}{v_{2}}^2}{2} = \frac{m_{1}{v'_{1}}^2}{2} + \frac{m_{2}{v'_{2}}^2}{2}
$$

$$
\begin{cases}
m_{1}({v_{1}} - {v'_{1}}) = m_{2}({v'_{2}} - {v_{2}}) \\
m_{1}({v_{1}}^2 - {v'_{1}}^2) = m_{2}({v'_{2}}^2 - {v_{2}}^2)
\end{cases}
$$

$$
\frac{v_{1} - v'_{1}}{{v_{1}^2} - {v'_{1}}^2} = \frac{v'_{2} - v_{2}}{{{v'_{2}}^2} - {v_{2}}^2}
$$

$$
\frac{v_{1} - v'_{1}}{(v_1 + v'_1)(v_1 - v'_1)} = \frac{v'_{2} - v_{2}}{(v'_2 - v_2)(v'_2 + v_2)}
$$

$$
\frac{1}{v_1 + v'_1} = \frac{1}{v'_2 + v_2}
$$

$$
v_1 + v'_1 = v'_2 + v_2
$$

$$
\begin{cases}
v'_1 = v_2 + v'_2 - v_1 \\
v'_2 = v_1 + v'_1 - v_2
\end{cases}
$$

$$
\begin{cases}
m_1v_1 + m_2v_2 = m_1{v'}_1 + m_2(v_1 + {v'}_1 - v_2) \\
m_1v_1 + m_2v_2 = m_1(v_2 + v'_2 - v_1) + m_2v'_2
\end{cases}
$$

$$
\begin{cases}
v'_1 = \frac{2m_2v_2 + v_1(m_1-m_2)}{m_1+m_2} \\
v'_2 = \frac{2m_1v_1 + v_2(m_2-m_1)}{m_1+m_2}
\end{cases}
$$
