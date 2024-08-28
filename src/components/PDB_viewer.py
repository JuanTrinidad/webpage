import dash_bio as dashbio
from dash import Dash, html
from dash_bio.utils import PdbParser, create_mol3d_style
from . import ids





def render(app:Dash) -> html.Div:
    
    PDB_data = {
    "atoms": [],
    "bonds": []
    }

    PDB_structure = dashbio.Molecule3dViewer(
                                    id=ids.PDB_VIEWER,
                                    selectionType='chain',
                                    modelData=PDB_data,
                                    styles=[]
                                )
    
    return html.Div(
        children=[
            PDB_structure
            
            
        ]
        
    )

