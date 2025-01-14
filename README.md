# **Particle Cluster Analysis in LAMMPS Simulations**  

This project is a Python script designed to analyze particle clusters in **LAMMPS simulation files** using the **OVITO Python API**. It identifies clusters of particles based on their neighbor counts and extracts relevant information for further study.  

## **Features**  
- **Neighbor Counting**: Determines the number of neighbors for each particle using a customizable cutoff radius.  
- **Cluster Identification**: Uses a depth-first search (DFS) algorithm to find connected clusters of particles based on neighbor thresholds.  
- **Data Export**: Saves information (index, type, and position) of selected particles in clusters to a text file.  
- **Statistics**: Calculates and prints:  
  - The total number of particles with fewer than a lower threshold of neighbors.  
  - The total number of particles with more than an upper threshold of neighbors.  
  - The average number of neighbors for all particles in the system.  

## **Key Parameters**  
- **Cutoff Radius**: Defines the maximum distance to consider particles as neighbors (default: `1.3`).  
- **Neighbor Thresholds**:  
  - Lower threshold (`umbral_vecinos_1`): Default `3`.  
  - Upper threshold (`umbral_vecinos_2`): Default `7`.  

## **Input and Output**  
- **Input**: LAMMPS trajectory file (`.lammpstrj`).  
- **Output**: A text file (`selected_particles_info2.txt`) containing:  
  - Particle index.  
  - Particle type.  
  - Particle position (x, y, z).  

## **Requirements**  
- Python  
- OVITO Python API  
- NumPy  

## **How to Use**  
1. Place your LAMMPS `.lammpstrj` file in the appropriate directory.  
2. Modify the script to set custom parameters (if needed).  
3. Run the script to analyze particle clusters.  
4. Check the output file for cluster details and the terminal for statistical summaries.  

## **Applications**  
This tool is ideal for studying particle clustering, coordination, and connectivity in molecular dynamics simulations, especially in the context of condensed matter physics or material science.  
