# -*- coding: utf-8 -*-

from matplotlib.backends.backend_ps import FigureCanvasPS as FigureCanvas
from matplotlib.figure import Figure

from pidsim.core.discretization import Euler
from pidsim.models.models import index as models_index

from subprocess import call

import os


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

    def run(self, filename):
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
        canvas.print_eps(filename)


plots = [
    Plot(1, 0.01, 6, k=1, Tau=1),
    Plot(2, 0.01, 35, k=1, T1=2, T2=5),
    Plot(3, 0.01, 35, k=1, T1=2, T2=5),
    Plot(4, 0.01, 40, k=1, T1=2, T2=4, T3=5, T4=3, Tt=2, pade_order=5)
]


cwd = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.abspath(os.path.join(cwd, '..', 'imagens'))

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

cont = 1
for plot in plots:
    filename = 'cap2_%i_model%i.eps' % (cont, plot.model)
    plot.run(os.path.join(dest_dir, filename))
    cont += 1
