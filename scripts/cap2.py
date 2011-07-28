# -*- coding: utf-8 -*-

from matplotlib.backends.backend_ps import FigureCanvasPS as FigureCanvas
from matplotlib.figure import Figure

from pidsim.core.discretization import Euler
from pidsim.models.models import index as models_index

import os

plot_registry = {}


class Plot:

    blacklist_args = ['pade_order']

    def __init__(self, model, sample_time, total_time, nmethod=None, **kwargs):
        self.model = model
        self.sample_time = sample_time
        self.total_time = total_time
        self.nmethod = nmethod
        self.kwargs = kwargs
        if self.nmethod is None:
            self.nmethod = Euler
        if model in plot_registry:
            plot_registry[model] += 1
        else:
            plot_registry[model] = 1
        self.plot_id = plot_registry[model]

    def run(self, output_dir):
        model = models_index[self.model]('pt_BR')
        g = model.callback(**self.kwargs)
        t, y = self.nmethod(g, self.sample_time, self.total_time)
        fig = Figure(figsize=(8, 6), dpi=300)
        ax = fig.add_subplot(111, xlabel='Tempo (seg)', ylabel='Amplitude')
        ax.plot(t, y, label='Resposta ao Degrau')
        legend = []
        for arg in model.args:
            if arg in self.blacklist_args:
                continue
            legend.append('%s=%s' % (arg, self.kwargs[arg]))
        ax.legend(loc='best', prop={'size': 'x-small'}, title='; '.join(legend))
        canvas = FigureCanvas(fig)
        filename = 'cap2_model%i_%i.eps' % (self.model, self.plot_id)
        canvas.print_eps(os.path.join(output_dir, filename))


plots = [
    Plot(1, 0.01, 6, k=1, Tau=1),
    Plot(2, 0.01, 35, k=1, T1=2, T2=5),
    Plot(2, 0.01, 70, k=1, T1=8, T2=12),
    Plot(2, 0.01, 120, k=1, T1=12, T2=18),
    Plot(3, 0.01, 35, k=1, T1=2, T2=5),
    Plot(4, 0.01, 40, k=1, T1=2, T2=4, T3=5, T4=3, Tt=2, pade_order=5),
    Plot(5, 0.01, 6, n=1),
    Plot(5, 0.01, 8, n=2),
    Plot(5, 0.01, 10, n=3),
    Plot(5, 0.01, 14, n=4),
    Plot(6, 0.01, 16, Alpha=0.2),
    Plot(6, 0.01, 16, Alpha=0.5),
    Plot(7, 0.01, 12, Alpha=0.2),
    Plot(7, 0.01, 12, Alpha=0.5),
    Plot(7, 0.01, 12, Alpha=1),
    Plot(7, 0.01, 12, Alpha=5),
    Plot(8, 0.01, 6, Tau=0.5, pade_order=5),
    Plot(8, 0.01, 14, Tau=2, pade_order=5),
    Plot(8, 0.01, 60, Tau=10, pade_order=5),
    Plot(9, 0.01, 20, Tau=2, pade_order=5),
    Plot(9, 0.01, 40, Tau=5, pade_order=5),
    Plot(10, 0.01, 60),
    Plot(11, 0.01, 80),
    Plot(12, 0.01, 20, Zeta=1, Omega=1),
    Plot(12, 0.01, 60, Zeta=5, Omega=1),
    Plot(12, 0.01, 12, Zeta=1, Omega=2),
    Plot(12, 0.01, 20, Zeta=5, Omega=2),
    Plot(12, 0.01, 10, Zeta=1, Omega=10),
    Plot(12, 0.01, 10, Zeta=5, Omega=10),
    Plot(13, 0.01, 10),
    Plot(14, 0.01, 50, Tau=5, pade_order=5)
]


cwd = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.abspath(os.path.join(cwd, '..', 'imagens'))

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for plot in plots:
    plot.run(dest_dir)
