<h1>The Intuition</h1>

The dot product mathematically measures how much two vectors "agree" with each other by projecting the shadow of one vector onto the other and multiplying their lengths.

<h1>The Geometry</h1>

Imagine standing at the origin (O) and shining a flashlight straight down onto vector $\mathbf{a}$. The shadow that vector $\mathbf{b}$ casts onto vector $\mathbf{a}$ is its projection.Plaintext      b (The vector you are projecting)
     ^
    /|
   / |
  /  | <-- The "flashlight" dropping down
 /   |
O----|---------> a (The reference vector)
  shadow

<ol>
<li>  
If they point the exact same way, the shadow is perfectly aligned (Max positive).</li>

If they are perpendicular ($90^\circ$), there is no shadow (Zero).</li>

If they point in opposite directions, the shadow falls backward (Negative).</li>
</ol>

<h1>The Math</h1>

Algebraically, you multiply matching dimensions and add them up. Geometrically, it's the product of their magnitudes scaled by the cosine of the angle $\theta$ between them.$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i = \|\mathbf{a}\| \|\mathbf{b}\| \cos(\theta)$$