
import ssl


import certifi
import urllib.request
from  rdkit import Chem   #rdkit is a chemical informatic libary
from rdkit.Chem import  Draw   #chemicainformatic libary part is rdkit which work in molecule and drow  is used for draw the molecule

import pubchempy as pcp
import os



ssl_context=ssl.create_default_context(cafile=certifi.where())
opener=urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_context))
urllib.request.install_opener(opener)

Chemical_name=input("Enter the name of the Chemocal_Name : ").strip()


try:
    compound=pcp.get_compounds(Chemical_name,'name')[0]




    print(f"The IUPAC name is {compound.iupac_name}")
    if compound.synonyms:
        print(f"The synoyms is {compound.synonyms[0]}")
    else:
        print(f"The chemicla is invalid")

    print(f"the molecular weight is {compound.molecular_weight}")
    print(f"The molecular function is {compound.molecular_formula}")

    #the structure of this chemical
    smiles=compound.canonical_smiles  # this is used for understanding chemical language like water(0)
    mol=Chem.MolFromSmiles(smiles)
    img=Draw.MolToImage(mol,size=(400,400))
    img_path= "molecule_structure.png"
    img.save(img_path)
    print(f"The structure of this chemical is :  ")
    os.startfile(img_path)






except IndexError:
    print("The Cheimacal name is invalid")
except Exception as e:
    print(e)






