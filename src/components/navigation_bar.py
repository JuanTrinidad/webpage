from dash import Dash, html
import dash_bootstrap_components as dbc

from . import ids


def render(app:Dash) -> dbc.NavbarSimple:


    return dbc.NavbarSimple(
                        children=[
                            dbc.NavLink('Gene Functional Annotation Summary', href='/home', active='exact', id='home-navlink', className="tab-link"),
                            dbc.NavLink("Cluster information and SRBH results", href="/dashboard", active='exact', id='dashboard-navlink', className="tab-link"),
                        ],
                        dark=True,
                        brand=app.title,
                        brand_href='#',
                        className="bg-dark",
                        id= ids.NAVIGATION_BAR
                        
                    )




