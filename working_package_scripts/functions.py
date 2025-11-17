#load in necessary libraries and functions
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.AllChem import GetMorganGenerator

# MORGAN FINGERPRINTS
def generate_morgan_fps(df, smiles_col="smiles", radius=3, n_bits=2048):
    
    #Convert the existing SMILES strings into RDKit molecules in order to be used for fingerprint generation
    df["mol"] = df[smiles_col].apply(Chem.MolFromSmiles)

    # MORGAN FINGERPRINTS
    mfgen = GetMorganGenerator(radius=3, fpSize=2048)#Morgan fingerprint generator object

    #now, loop to generate morgan fingerprints
    morg_fps = [] #empty list to store the new fingerprints
    for mol in df["mol"]:
        if mol is not None:
            mfp = mfgen.GetFingerprint(mol) #generate fingerprint for all data
            morg_fps.append(mfp) #add it to the end of the fp list each time
        else:
            morg_fps.append(None)
    df["morgan_fp"] = morg_fps
    return df

# MACCS KEYS
#next, loop through in a similar fashion to generate MACCS keys
def generate_maccs_fps(df, smiles_col="smiles"):

    df["mol"] = df[smiles_col].apply(Chem.MolFromSmiles)

    maccs_fps = [] #empty list to store them
    for mol in df["mol"]:
        if mol is not None:
            mcfp = MACCSkeys.GenMACCSKeys(mol) #generate the key for all data
            maccs_fps.append(mcfp) #add it to the end of the list each time
        else:
            maccs_fps.append(None)
    df["maccs_fp"] = maccs_fps
    return df