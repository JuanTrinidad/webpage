from dash import Dash, html
import dash_bootstrap_components as dbc

from . import ids


def render(app:Dash) -> dbc.NavbarSimple:


    return dbc.NavbarSimple(
                        children=[
                        dbc.NavLink('Gene Funtional Annotation Summary', href='/home', active='exact', id='home-navlink'),
                        dbc.NavLink("Cluster information and SRBH results", href="/dashboard", active='exact', id='dashboard-'),
                        ],
                        dark=True,
                        #color='black',
                        brand=app.title,
                        brand_href='#',
                        className="bg-dark",
                        id= ids.NAVIGATION_BAR
                    )





