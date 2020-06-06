# Location of raw data file
datafile = '../Davies_etal_NGeo_2019_Datasets/hoggard/spot_shiptrack.dat'

# Base location for outputs
# The code will create subdirectories under this for each data subset and
# for the resulting figures
outputdir = '.'

# Run analysis for the subset of 1160 high-accuracy spot points?
DO_HIGH_ACCURACY_SPOT = False

# Run analysis for the subset of all 2030 spot points?
DO_ALL_SPOT = True

# Run analysis for complete database?
# N.B. This requires significant computational resources
#      (~48 hours on quad-core 3.2GHz Intel i5 with 16Gb RAM)
#      Running this on a machine with less than 16Gb RAM is
#      not recommended.
DO_SPOT_SHIP = False

# When generating figures, should plt.show() be called?
# Note that this may cause the interpreter to block and
# wait for the figure to be closed
PLT_SHOW = False