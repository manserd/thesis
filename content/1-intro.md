# Introduction

Classical (automated) planning is an area in artifical intelligence research concerned with the automated solving of (static, deterministic, fully observable) problems: these problems are modeled as *state spaces* comprised of *states* and *transitions* between states, where the objective is finding a sequence of transitions starting at an *initial state* that results in a desired *goal state*.

A subset of the search algorithms used to explore such state spaces are the *heuristic algorithms*, which are defined by their ability to use a *heuristic function* to make *informed* decisions during exploration of a space. One such algorithm is *greedy best-first search* (GBFS).

GBFS is considered "greedy" because it always makes *locally* optimal decisions, without the privilege of a more holistic view of its progress. This results in a comparatively small memory footprint and great performance, which allows us to explore larger state spaces, but also makes GBFS vulnerable: if a heuristic advertises inaccurate goal distances for a given region in the state space, GBFS is forced to search these so-called *uninformed heuristic regions* (UHRs) exhaustively or until it manages to return to an informed region.

One method to mitigate this issue is *stochastic exploration*, where we allow GBFS to occasionally ignore the advice of the heuristic and instead select a successor stochastically. The effectiveness of this approach can be helped by tuning the probability distribution during these *exploratory expansions* such that it promotes higher diversity upon a stochastic selection; this is the idea of *type-based stochastic exploration*: instead of simply selecting a successor directly, states are first *bucketed* by shared qualities. We then start by stochastically selecting such a *bucket*, from which we then stochastically select an actual successor state.

One difficulty with type-based expansion is finding a suitable strategy by which to bucket states, called a *type system*. Traditionally, states are bucketed using features such as heuristic value or path length \cite{}. Tomasz and Valenzano \cite{} propose a new approach based on the concept of *benches*.

- advantages of the new type systems
- announce what this work aims to do
