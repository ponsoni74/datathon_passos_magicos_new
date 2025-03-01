import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import plotly.graph_objs as go
import locale

def format_number(number, format="%0.0f"):
    return locale.format_string(format, number, grouping=True)

def plot_histograma(
    df: pd.DataFrame,
    col: str,
    titulo: str,
    bins: int = None,
    rug: bool = True,
):
    # faz o cálculo do KDE com o scipy
    data = df[col].values
    kde = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 1000)
    kde_vals = kde(x_vals)

    # faz o cálculo da quantidade "ótima" de bins (assim evitamos grupos de classificação desnecessários)
    bins = len(np.histogram_bin_edges(data, bins="auto")) if bins == None else bins

    # cria os plots separados (histograma + kde + rug)
    # 1. histograma
    histogram = go.Histogram(
        x=data, nbinsx=bins, histnorm="probability density", name=f"Percentual: {col}"
    )

    # 2. kde
    kde_line = go.Scatter(
        x=x_vals, y=kde_vals, mode="lines", name="Curva (KDE)", line=dict(color="magenta")
    )

    # 3. rug, mas apenas se ele tiver sido requisitado
    if rug:
        rug_plot = go.Scatter(
            x=data,
            y=[-0.01] * len(data),
            mode="markers",
            name="Observações individuais",
            marker=dict(color="orange", symbol="line-ns-open", size=10),
        )

    # 4. figura principal
    fig = go.Figure()
    fig.add_trace(histogram)
    fig.add_trace(kde_line)
    fig.update_traces(
        texttemplate="%{y:.0%}",
        textposition="outside",
        selector=dict(type="histogram"),
        marker=dict(color='pink')  # Set the color to pink
    )

    # 6. configs
    fig.update_layout(
        title=titulo,
        xaxis_title="Idade",
        yaxis_title="Percentual",
        yaxis=dict(range=[-0.02, None]),
        bargap=0.015,
        uniformtext_mode="hide",
    )

    # configs com rug
    if rug:
        fig.add_trace(rug_plot)
    # configs sem rug
    else:
        fig.update_layout(xaxis=dict(tickmode="linear"))

    return fig


