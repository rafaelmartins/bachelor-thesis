# -*- coding: utf-8 -*-

from matplotlib.backends.backend_ps import FigureCanvasPS as FigureCanvas
from matplotlib.figure import Figure

from pidsim.core.discretization import Euler, RungeKutta4
from pidsim.core.pid.identification import Smith
from pidsim.core.pid.tuning import ZieglerNichols
from pidsim.core.types import tf
from pidsim.models.models import index as models_index

import os

plot_registry = {}


class Plot:

    blacklist_args = ['pade_order', 'simulate']

    def __init__(self, model, sample_time, total_time, nmethod=None, simulate=False,
                 kp=None, ki=None, kd=None, **kwargs):
        self.model = model
        self.sample_time = sample_time
        self.total_time = total_time
        self.nmethod = nmethod
        self.kwargs = kwargs
        self.simulate = simulate
        self.kp = kp
        self.ki = ki
        self.kd = kd
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

        if self.kp is None or self.ki is None or self.kd is None:
            kp, ki, kd = ZieglerNichols(t, y, Smith).gains
        else:
            kp, ki, kd = self.kp, self.ki, self.kd

        if self.simulate:
            # transfer function of the PID controller
            g_ = tf([kd, kp, ki], [1, 0])
            my_g = (g_ * g).feedback_unit()

            # discretize the controlled system
            t1, y1 = self.nmethod(my_g, self.sample_time, self.total_time)
            ax.plot(t1, y1, label='Resposta ao Degrau Controlada')
        else:
            # generate the tuning line
            ident = Smith(t, y)
            t1, y1 = ident.tuning_line
            ax.plot(t1, y1, label='Reta de Sintonia')
            ax.annotate(
                '%.1f%%' % ident.point1, xy=(t1[1], y1[1]), xycoords='data',
                xytext=(t1[1]+(self.total_time/15.0), y1[1]),
                arrowprops=dict(facecolor='black', shrink=0.05),
            )
            ax.annotate(
                '%.1f%%' % ident.point2, xy=(t1[2], y1[2]), xycoords='data',
                xytext=(t1[2]+(self.total_time/15.0), y1[2]),
                arrowprops=dict(facecolor='black', shrink=0.05),
            )
        legend = []
        for arg in model.args:
            if arg in self.blacklist_args:
                continue
            legend.append('%s=%s' % (arg, self.kwargs[arg]))
        ax.legend(
            loc = 'best',
            prop = {'size': 'x-small'},
            title = 'kp=%.1f; ki=%.1f; kd=%.1f;' % (kp, ki, kd),
        )
        canvas = FigureCanvas(fig)
        filename = 'cap4_model%i_%i.eps' % (self.model, self.plot_id)
        canvas.print_eps(os.path.join(output_dir, filename))


plots = [
    Plot(5, 0.01, 20, n=4),
    Plot(5, 0.01, 20, n=4, simulate=True),
    Plot(5, 0.01, 20, n=4, simulate=True, kp=2.0, ki=0.9, kd=1.4),
]


cwd = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.abspath(os.path.join(cwd, '..', 'imagens'))

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for plot in plots:
    plot.run(dest_dir)
