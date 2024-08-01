from dash import Dash, dcc
from . import ids






def render(app:Dash) -> dcc.Input:
    
    return dcc.Input(
        id=ids.TEXT_INPUT2, 
        className='input-custom',
        type="text", 
        placeholder="Input geneID: ej. Tb927.10.13280",
        #value='',
        )

