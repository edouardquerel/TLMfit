# TLMfit
Fit impedance data of battery electrodes using a transmission line model with current collector contact resistance and calculate tortuosity factor

The attached Jupyter notebook can be used to extract the electrode tortuosity factor from impedance data collected in symmetrical cells with non-intercalating electrolyte.
The equivalent circuit model used to fit the data contains: 
- a resistor R0 accounting for ohmic resistances in the cell (e.g. separator)
- a current collector contact impedances Zcc, modelled by a parallel R-CPE element 
- a Z-type TLM, neglecting electronic contributions in the electrode phase. The TLM expression is taken from Siroma et al. Electrochimica Acta 2015, https://doi.org/10.1016/j.electacta.2015.02.065 

The equivalent cell impedance Zcell=R0+2.Z_cc+2.Z_TLM

Care was taken to normalize the expression of the TLM from Siroma's paper by the apparent electrode area to enable fitting of the raw data in [Ohms] 

1. Copy the TLM_fitting folder on your local drive
2. Copy the impedance file (in .mpr file format) you would like to fit in the "data" folder. The file should contain a single impedance spectrum, the current script doesn't handle loops. 
3. Open the notebook "tortuosity_notebook_mprfile.ipynb" and run the cells. 
