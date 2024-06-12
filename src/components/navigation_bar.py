from dash import Dash, html
import dash_bootstrap_components as dbc

from . import ids


def render(app:Dash) -> html.Div:


    return html.Div(
                    dbc.NavbarSimple(
                        children=[
                        dbc.NavLink('Gene Funtional Annotation Summary', href='/home', active='exact', id='home-navlink'),
                        dbc.NavLink("Cluster information and SRBH results", href="/dashboard", active='exact', id='dashboard-'
                                    ),
                    ],
                        dark=True,
                        color='primary',
                        brand=app.title,
                        brand_href='#',
                        className='py-lg-0',
                        id= ids.NAVIGATION_BAR
                    )
                )




