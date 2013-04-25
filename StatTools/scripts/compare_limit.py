#! /usr/bin/env python
__doc__ = '''
Simple script that compares multiple limits
'''

import rootpy.io as io
from FinalStateAnalysis.Utilities.struct import struct
from FinalStateAnalysis.Utilities.solarized import colors
import FinalStateAnalysis.Utilities.prettyjson as prettyjson
from rootpy.plotting.graph import Graph
import rootpy.plotting as plotting
import rootpy.plotting.views as views
from optparse import OptionParser
import os
import ROOT
import math

def json2graph(json_dict, load_error=None, **kwargs):
    limit   = json_dict['limits']
    ret     = Graph(npoints = len(limit.keys()), **kwargs)
    for i, x in enumerate(sorted(limit.keys())): #fills it (why it is not available in the default constructor???)
        y = limit[x]['median']
        ret.SetPoint(i, float(x), y)
        if load_error:
            eyh = abs(limit[x]['+'+load_error] - y)
            eyl = abs(limit[x]['-'+load_error] - y)
            ret.SetPointError(i, 0, 0, eyl, eyh)
    return ret

parser = OptionParser(description=__doc__)
parser.add_option('--output', '-o', type=str, default = 'limit_comparison',
                  help='file name to be used',dest='outfile')
parser.add_option('--xtitle', type=str, default = "m_{H} [GeV]",
                  help='x axis title',dest='xtitle')
parser.add_option('--ytitle', type=str, default = "95% CL limit on #sigma/#sigma_{SM}",
                  help='y axis title',dest='ytitle')
parser.add_option('--xrange', type=str, default = "",
                  help='x range',dest='xrange')
parser.add_option('--yrange', type=str, default = "",
                  help='y range',dest='yrange')
parser.add_option('--logy', action='store_true', dest='logy', default = False,
                  help='log scale on y axis')
parser.add_option('--name-by', type=str, default = "channel",
                  help='which information use to name',dest='name_by')
parser.add_option('--ref', type=str, default = "",
                  help='limit to be used as reference',dest='ref')
parser.add_option('--legend-on-the-left', action='store_true', dest='legend_left', default = False,
                  help='puts the legend on the left')

## parser.add_option('--png', action='store_true', dest='png', default = False,
##                   help='prints in png format')
## parser.add_option('--pdf', action='store_true', dest='pdf', default = False,
##                   help='prints in pdf format')
## parser.add_option('--tex', action='store_true', dest='tex', default = False,
##                   help='prints in LaTex format')
## parser.add_option('--txt', action='store_true', dest='txt', default = False,
##                   help='prints in txt format')
## parser.add_option('--root', action='store_true', dest='root', default = False,
##                   help='prints in root format')
## parser.add_option('--cpp', action='store_true', dest='cpp', default = False,
##                   help='prints in .C format')


(options,jsons) = parser.parse_args()
jmaps= [prettyjson.loads( open(json).read() ) for json in jsons]

to_print = []
mycols   = [
    colors['red'],
    colors['blue'],
    colors['green'],
    colors['orange'],
    colors['cyan'],
    ]

canvas   = plotting.Canvas(name='adsf', title='asdf')
one_line = None
first = True
for json, col in zip(jmaps, mycols):
    col = col if (not options.ref) or \
        json[options.name_by] != options.ref \
        else ROOT.kBlack
    to_print.append(
        json2graph(
            json,
            name=json['channel'],
            drawstyle = 'ALP' if first else 'LP SAME',
            legendstyle = 'PL',
            fillcolor = col,
            linecolor = col,
            markercolor = col,
            title = json[options.name_by],
            markerstyle = 20,
            markersize  = 1,
            linewidth = 3,
            linestyle = 1,
            )
        )

    if first:
        mass_points = [i for i in to_print[-1].x()]
        one_line = Graph(
            len(mass_points),
            name='unity',
            drawstyle = 'L SAME',
            inlegend  = False,
            linecolor = ROOT.kBlue,
            linewidth = 3,
            )
        for i, m in enumerate(mass_points):
            one_line.SetPoint(i, m, 1.)
    first=False

to_print[0].GetXaxis().SetTitle(options.xtitle)
to_print[0].GetYaxis().SetTitle(options.ytitle)

if options.xrange:
    r = eval(options.xrange)
    to_print[0].GetXaxis().SetRangeUser(r[0], r[1])
if options.yrange:
    r = eval(options.yrange)
    to_print[0].GetYaxis().SetRangeUser(r[0], r[1])

if options.logy:
    canvas.SetLogy(True)

for graph in to_print:
    graph.Draw()

one_line.Draw()

legend = plotting.Legend(len(to_print), rightmargin=0.07, topmargin=0.05, leftmargin=0.45) \
    if not options.legend_left else \
    plotting.Legend(len(to_print), leftmargin=0.03, topmargin=0.05, rightmargin=0.65)
legend.SetEntrySeparation(0.0)
legend.SetMargin(0.35)

for graph in to_print[::-1]:
    legend.AddEntry(graph)

legend.Draw()
canvas.SaveAs(options.outfile+'.png')
canvas.SaveAs(options.outfile+'.pdf')