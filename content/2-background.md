# Background

## State Spaces

We define a *state space* as a tuple $$\mathcal{S}=\langle S,A,\mathrm{cost},T,s_{I},S_G\rangle,$$ with $S$ the set of states, $A$ the set of actions, $\mathrm{cost}:A\rightarrow\mathbb{R}_0^+$ the cost function, $T\subseteq S\times A\times S$ the transition relation, $s_I\in S$ the initial state, and $S_G\subseteq S$ the set of goal states.

- successor generator function $\mathrm{succ}$
- set of all $s$-plans (path to goal from $s$) $P(s)$
- paths between $s$ and $s'$ $P(s,s')$
- TV ignore transition costs
- "$s\in\mathcal{S}$" means $s\in S$

## Heuristics

We also define a *heuristic* as a function $h:S\rightarrow\mathbb{R}_0^+\cup\{\infty\}$.

- $h(S)=\min_{s\in S}h(s)$
- state space topology $\mathcal{T}=\langle\mathcal{S},h\rangle$
- open/closed lists, no reopening (satisficing)

## High-Water Mark

$$\mathit{hw}_h(s):=\begin{cases}\min_{p\in P(s)}(\max_{s'\in p}h(s')), & \text{if } P(s)\neq\emptyset; \\ \infty, & \text{otherwise}.\end{cases}$$

If the *maximum heuristic value* refers to the highest encountered heuristic value along some path, then $\mathit{hw}_h(s)$ selects the lowest such maximum heuristic value (of the heuristic $h$) among all paths from $s$ to a goal. Or intuitively, following the definition by \cite{}: the high-water mark shows how high $h$ must climb before a solution is found.

- check reference definition
- $\mathit{hw}_h(s)\geq h(s)$ (when is this used?)
- $\mathit{hw}_h(S):=\min_{s\in S}\mathit{hw}_h(s)$

We say GBFS *makes progress* when it encounters a state with a lower high-water mark among its successors: $\mathrm{hw}_h(\mathrm{succ}(s))<\mathrm{hw}_h(s)$.

- $\mathrm{succ}$ undefined

Such a state $s$ is called a *progress state*.

## Benches

Let $s$ be some state, and consider the lowest high-water mark among its successors, $\mathit{hw}_h(\mathrm{succ}(s))$.

Any state $s'\neq s$ reachable from $s$ where $h(s')$ is smaller than or equal to the bench level, but which is **not** a progress state, can be considered part of a "bench" induced by $s$. We call these states the *inner states*.

Naturally, a state $s'\neq s$ reachable from $s$ where $h(s')$ is smaller than or equal to the bench level but which **is** a progress state can thus be considered at the "edge" of the aforementioned "bench". These states are called the *exit states*.

Combining the two: for any state $s$, its *bench* is a tuple $\mathcal{B}(s)=\langle I,E\rangle$, with $I$ being the inner states and $E$ the exit states.

- check reference definition
- BTS
