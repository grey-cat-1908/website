# Elastic Collisions Simulation

## 1. Introduction

Recently, the recommendation system of a video hosting site suggested me to watch a video of several cubes colliding. It appeared to be an intriguing concept. After viewing the video, I was inspired to create a simulation of that process and explain its underlying principles.

## 2. Relevance

There are numerous reasons why this project is relevant, as well as a wide range of potential applications. The following will outline the primary reasons and applications:

- It can be used in the educational process. For instance, it can be used to illustrate some principles of mechanics to students and to visualize some physics problems.
  
- It can be used to simulate some physical experiments. For instance, it can be used to simulate the one described in _G. A. Galperin's work_.[^1] 

- It can be used as a basis for future projects.

## 3. The consequences of collisions

Firstly, it is essential to comprehend how the velocity of the body after collision is calculated. We will solve the problem in the elastic collision model (one-dimensional Newtonian).

### 3.1 Body-Body

Consider two bodies, designated as bodies `1` and `2`, with respective masses $m_1$ and $m_2$. Before the collision, the velocities of bodies 1 and 2 are $v_1$ and $v_2$, respectively. After the collision, the velocities of bodies 1 and 2 are $v_1'$ and $v_2'$, respectively. 

In any collision, momentum is conserved. A collision between to bodies is said to be elastic if it involves no change in their internal state. Accordingly, when the law of conservation of energy is applied to such a collision, the internal energy of the bodies may be neglected.[^2]

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

From this, we can derive the velocity of the bodies following the collision as follows:

$$
\begin{cases}
v'_1 = \frac{2m_2v_2 + v_1(m_1-m_2)}{m_1+m_2} \\
v'_2 = \frac{2m_1v_1 + v_2(m_2-m_1)}{m_1+m_2}
\end{cases}
$$

### 3.2 Body-Wall

Consider the body and the wall with respective masses $m$ and $m_w \rightarrow \infty$. Before the collision, the velocities of the body and the wall are $v$ and $v_w = 0$, respectively. After the collision, the velocities of the body and the wall are $v'$ and $v_w'$, respectively. 

In order to proceed, we will utilize the formulas derived in section **3.1**.

The velocity of the body will take the following form:

$$
v' = \lim\limits_{m_w \to \infty} \frac{2m_wv_w + v(m-m_w)}{m+m_w} = \lim\limits_{m_w \to \infty} \frac{v(m-m_w)}{m+m_w} = -v
$$

The velocity of the wall will take the following form:

$$
v_w' = \lim\limits_{m_w \to \infty} \frac{2mv + v_w(m_w-m)}{m+m_w} = \lim\limits_{m_w \to \infty} \frac{2mv}{m+m_w} = 0
$$

This leads to the conclusion that the wall will not change its position, but the body will change its velocity value to the opposite.

## 4. Technical implementation

### 4.1 Simulation

To create the simulation (animation), it was determined that `Processing` technology, specifically `p5.js`[^3], would be the most suitable.

We will assume that the bodies have the form of two squares of different sizes and colors. The smaller body will be placed to the left of the larger body.

The following variables should also be defined:

  - $v_1, v_2$ - Velocities of the bodies (respectively).
    
  - $w_1, w_2$ - Widths of the bodies (respectively).
    
  - $m_1, m_2$ - Masses of the bodies (respectively).
    
  - $x_1, x_2$ - Current coordinates of the bodies (respectively).
    
  - $c_1, c_2$ - Constraints of the bodies coordinates (respectively).

The initial step was to meticulously program the model of the bodies:

  1. For visual convenience, the width of the first body will be $w_1 = 50$ and the second's will be $w_2 = 100$.

  2. Furthermore, for the sake of visual clarity, the coordinates for the bodies will be as follows: $x_1 = 100$, $x_2 = 300$.

  3. The physical constraint (`p5.constrain`) of the first body's coordinate will be $c_1 = 0$, of the second body's coordinate $c_2 = 0 + w_1 = 50$  

  4. The initial velocity of the bodies and their mass are set by the user, so for the time being, we will leave them as constants.

Another step is to describe the algorithm of their movement:

  1. If the first smaller body makes contact with the wall ($x_1 <= 0$), adjust its velocity in accordance with the formula described in section **3.2**.

  2. If the bodies collide with each other, then set each of them velocity according to the formulas given in **3.1**.

The next step is to determine the best method for animating the object and moving it with a specified velocity. 

To enhance the smoothness of animations and reduce load times, the following steps were taken: 

  - It was decided to create a loop in the `move` function (`p5.js`) that will perform a given number of operations ($10^6$).

  - The user-specified initial velocity will also be divided by $10^6$.

### 4.2 User Options

For the convenience of users, the velocity and mass of each body can be set according to the user's preferences.

To streamline the user experience and avoid overwhelming the page of the simulator with unnecessary buttons and technical complexities, it was decided to use apply new settings and restart an animation when user reloads the browser page.

So, once the user has entered data into the designated fields, it is automatically saved to the localStorage. [^4]

## 5. Usage

### 5.1 Common problems

We recommend avoiding setting particularly large values for variables, because:

- Despite the use of optimization tools, there may be instances where the page will use a significant amount of your device's resources.

- Large values may result in animation crashes and premature stopping of counting.

### 5.2 Experience

The interface of the simulation UI is as follows:

![img](https://cdn.arbuz.icu/img/other/1d-col.png)

## 6. Conclusion (How To Try?)

You can try the simulator [here](https://od-collisions.arbuz.icu/).

---

## Notes

* If you decide to use this project as the basis of your project, it would be advisable to [contact me](https://arbuz.icu/mail) first.

* If you have any interesting projects that I could be involved in, or if you would like to contact me, you can do so [here](https://arbuz.icu/mail).

* You can find the project files in the [repository on Github](https://github.com/grey-cat-1908/collisions-fool-)

## Reference 

[^1]: Galperin, G. A., _[PLAYING POOL WITH π (THE NUMBER π FROM A BILLIARD POINT OF VIEW)](http://rcd.ics.org.ru/RD2003v008n04ABEH000252/)_, _Regular and Chaotic Dynamics_, 2003, vol. 8, no. 4, pp. 375-394.

[^2]: Landau, L.D. and Lifshitz, E.M., _Course of Theoretical Physics_, vol. 1: _Mechanics_, Elsevier Science, 1982.

[^3]: _p5.js_, Processing Foundation, accessed 30 April 2024, <https://p5js.org/>

[^4]: Mozilla Corporation, _Window: localStorage property_, accessed 30 April 2024, <https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage>
