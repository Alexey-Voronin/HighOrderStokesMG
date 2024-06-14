import os
import subprocess
import numpy as np


refine_geo = lambda i : f"""
// Load an existing mesh file
Merge "coarse{i}.msh";
// Refine the mesh
RefineMesh;
// Save the refined mesh
Save "ref_coarse{i}.msh";
"""
cmd_gen = lambda h,i : f"gmsh -2 -format msh2 -clscale {h} backwards-facing-step.geo -algo front2d -o coarse{i}.msh -smooth 3"
h_scale = 1.6
Nmeshes = 10
Hs = [h_scale/1.5**i for i in range(0, Nmeshes)]
nE = []


for i, h in enumerate(Hs):
    h_label = str(i).zfill(2)

    proc = subprocess.Popen([cmd_gen(h, h_label)],
                              stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    gmsh_out = out.decode("utf-8")

    for line in gmsh_out.split('\n'):
        if 'nodes' in line and 'elements' in line:
            spl = line.split(' ')
            nElem, nNodes = int(spl[-4]), int(spl[-2])

    nE.append(nElem)

    # Refine the above mesh and save as a separate file
    with open("refined_mesh.geo", "w") as file:
        file.write(refine_geo(h_label))

    proc = subprocess.Popen(["gmsh - refined_mesh.geo"],
                              stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    gmsh_out = out.decode("utf-8")
    """
    """


tmp = np.round(Hs, 3)
nE  = np.array(nE)
print('Hs: ', tmp, np.round(1/(tmp[1:]/tmp[:-1]),2))
print('nE: ', nE, np.round(nE[1:]/nE[:-1],2))
