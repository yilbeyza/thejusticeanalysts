from django.shortcuts import render
from django.views.generic import TemplateView
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


from django.views.generic import ListView
#from .models import Posts

from django.shortcuts import redirect


# Create your views here.

"""class HomepageView(TemplateView):
    template_name = 'home.html'"""
def index(request):


    df_shootings = pd.read_csv(
        'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv')

    state_count = df_shootings.groupby(['state', 'race']).size().reset_index(name='total')

    races = pd.DataFrame({'W': 'White, non-Hispanic',
                          'B': 'Black, non-Hispanic',
                          'A': 'Asian',
                          'N': 'Native American',
                          'H': 'Hispanic'}, index=[0])
    races
    fig = go.Figure()
    layout = dict(
        title_text="Fatal Police Shootings Data",
        geo_scope='usa',
    )

    for index, race in enumerate(races):
        result = state_count[['state', 'total']][state_count.race == race]
        geo_key = 'geo' + str(index + 1) if index != 0 else 'geo'
        fig.add_trace(
            go.Choropleth(
                locations=result.state,
                z=result.total,
                locationmode='USA-states',  # set of locations match entries in `locations`
                marker_line_color='white',
                colorbar_title="Shooting deaths",
                geo=geo_key,
                name=races[race].values[0],
                coloraxis='coloraxis',
            )
        )

        layout[geo_key] = dict(
            scope='usa',
            domain=dict(x=[], y=[]),
        )

    layout
    z = 0
    COLS = 3
    ROWS = 2
    for y in reversed(range(ROWS)):
        for x in range(COLS):
            geo_key = 'geo' + str(z + 1) if z != 0 else 'geo'
            layout[geo_key]['domain']['x'] = [float(x) / float(COLS), float(x + 1) / float(COLS)]
            layout[geo_key]['domain']['y'] = [float(y) / float(ROWS), float(y + 1) / float(ROWS)]
            z = z + 1
            if z > 4:
                break

    fig.update_layout(layout)

    usaMap = pio.to_html(fig,include_plotlyjs=False, full_html=False)

    return render(request, "home.html", {"usaMap": usaMap})


class ContactUsView(TemplateView):
    template_name = 'posts.html'
    #model = Posts
    #context_object_name='all_posts_list'

class AllDataView(TemplateView):
    template_name = 'alldata.html'