from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Posts
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from django.shortcuts import redirect
from . import forms
from .models import Messages

def messagevalidate(request):
    return render(request, "alldata.html")

def message(request):
    if request.method == " GET":
        return redirect('/')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        yourmessage = request.POST.get("yourmessage")

        newMessage=Messages(name=name,email=email,phone=phone,yourmessage=yourmessage)
        newMessage.save()
        return redirect('/')
        """if form.is_valid():
            form.save(commit=True)
            return messagevalidate(request)

        else:
            print('Invalid Message!')"""



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


class AllDataView(TemplateView):
    template_name = 'alldata.html'

def comment(request):
    return render(request, "posts.html")

def review(request):
   form = forms.FormName()

   if request.method == 'POST':
    form = forms.FormName(request.POST)

    if form.is_valid():

        print("VALIDATION SUCCESS!")
        print("E-MAİL"+form.cleaned_data['email'])
        print("NAME" + form.cleaned_data['name'])
        print("TEXT" + form.cleaned_data['text'])


   return render(request, "posts.html", {'form':form})



