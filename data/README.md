# Paper Data and Visualization Files


## Data File Structure 
```
.
├── 2D                                      # 2D problem data
│   ├── sv                                  # Scott-Vogelius discretization
│   │   ├── iterators.py                    # problem size iterators
│   │   ├── phmg                            # Monolithic GMG, direct coarsening
│   │   │   ├── bfs2d                       # 2D Backward facing step problem
│   │   │   │   ├── parallel_p8             # Parallel execution with 8 MPI tasks
│   │   │   │   │   └── V1_p2_h2            # V-cycle config: V{h-cycles}_p{p-lvl rlx sweeps}_h{h-lvl rlx sweeps}
│   │   │   │   │       ├── ksp.log
│   │   │   │   │       ├── petsc_profiler.log
│   │   │   │   │       ├── results.log
│   │   │   │   │       ├── results.pkl
│   │   │   │   │       └── sanity_check.log
│   │   │   │   └── solver.py               # data collection driver script
│   │   │   └── ldc2d                       # Lid-driven cavity problem
│   │   ├── phmg_grad                       # GMG with gradual coarsening
│   │   ├── params.py                       # paramters generating-function specifying problem and solver types
│   │   └── run.sh                          # Script to run all 2D sv problems
│   └── th                                  # Taylor-Hood discretization
├── 3D                                      # 3D problem data
│   ├── sv
│   └── th
└── plotting_scripts                        # Scripts for visualization
    ├── bar_table.py
    ├── common.py
    ├── plotting_scripts.py
    ├── sv_2D.ipynb
    ├── sv_3D.ipynb
    ├── th_2D.ipynb
    └── th_3D.ipynb
```


### Directory Abbreviations

| Abbreviation | Description                                  |
|--------------|----------------------------------------------|
| th           | Taylor-Hood discretization results           |
| sv           | Scott-Vogelius discretization results        |
| phmg         | Monolithic GMG with direct coarsening        |
| phmg_grad    | Monolithic GMG with gradual coarsening       |
| afbf         | Approximate full-block factorization         |
| ldc*d        | Lid-driven cavity problem                    |
| bfs2d        | Backward facing step problem                 |

#### File Abbreviations

| Abbreviation         | Description                                           |
|----------------------|-------------------------------------------------------|
| ksp.log              | PETSc's KSPView output                                |
| petsc_profiler.log   | PETSc's profiler output, detailing setup and solve phases |
| results.log          | Summary of problem sizes and convergence results      |
| results.pkl          | Pickled data in dictionary format from runs           |
| sanity_check.log     | Printed solver parameter dictionary passed to PETSc   |


