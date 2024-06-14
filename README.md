# Monolithic Multigrid Preconditioners for High-Order Discretizations of Stokes Equations

## Abstract

This work introduces and assesses the efficiency of a novel monolithic $ph\text{MG}$ multigrid method, specifically designed for high-order discretizations of stationary Stokes systems using Taylor-Hood and Scott-Vogelius elements. The $ph\text{MG}$ approach integrates approximation order ($p$) and spatial ($h$) coarsening to address the computational and memory efficiency challenges that are often encountered in conventional high-order numerical simulations. Our comparative analysis reveals that $ph\text{MG}$ offers significant improvements over traditional spatial-coarsening-only multigrid ($h\text{MG}$) techniques for problems discretized with Taylor-Hood elements across a variety of problem sizes and discretization orders. In particular, the $ph\text{MG}$ method exhibits superior performance in reducing setup and solve times, particularly when dealing with higher discretization orders and unstructured problem domains. For Scott-Vogelius discretizations, while monolithic $ph\text{MG}$ delivers low
    iteration counts and competitive solve phase timings, it exhibits a
    discernibly slower setup phase when compared to a multilevel
    (non-monolithic) full-block-factorization ($\text{FBF}$) preconditioner where
    $ph\text{MG}$ is employed only for the velocity unknowns. This is primarily due to
    the setup costs of the larger mixed-field relaxation patches with monolithic
    $ph\text{MG}$ versus the patch setup costs with a single unknown type for $\text{FBF}$.

## Authors

- Alexey Voronin (voronin2 [at] illinois.edu)
- Graham Harper
- Scott MacLachlan
- Luke N. Olson
- Raymond Tuminaro

The published paper can be found at:
- [arxiv (To be released at the end of June 2024)](https://arxiv.org/)

This GitHub repository houses the code and data referenced in the aforementioned publications.

# How to Run the Example Problems

The primary code is located in the [phmg](./phmg/) directory. The scripts required for data collection are stored in the [data](./data/) directory.

## Dependencies

To effectively utilize this code, the following dependencies are needed:
- [Firedrake](https://www.firedrakeproject.org/) (Compatibility tested with version 0.13.0)
