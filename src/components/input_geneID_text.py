from dash import Dash, dcc
from . import ids






def render(app:Dash) -> dcc.Input:
    
    return dcc.Input(
        id=ids.TEXT_INPUT1, 
        className='input-group, mb-3',
        type="text", 
        placeholder="Input geneID: ej. Tb927.10.13280",
        #value='Tb927.3.1760',
        )




