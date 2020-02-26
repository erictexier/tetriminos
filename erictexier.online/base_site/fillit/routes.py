from flask import Blueprint
from flask import render_template, jsonify, flash, request, redirect, url_for

from base_site.fillit import do_tetrino
from base_site.fillit.fillit_form import FillitForm


fillit = Blueprint('fillit', __name__)


def render_tetrino(form, nb):
    if nb < 1:
        nb = 1
    t = do_tetrino.Tetrino()
    t.build_random(nb)
    t.do_play()
    perf = "perf for {} tetriminos: {:.3f}sec (grid {} x {} - coverage {:.2f}%)".format(nb, 
                                                                        t.delta,
                                                                        t.sqa,t.sqa,t.stat)
    flash(perf, 'success')
    nb_col = max(int(nb / 2), 10)
    return render_template('fillit/fillit.html',
                            title='New Grid',
                            result = t.result,
                            data = t.show_in_line(nb_col),
                            label = "", blank = False,
                            form=form)

@fillit.route("/fillit", methods=['GET','POST'])
def fillit_route():
    form = FillitForm()
    if form.validate_on_submit():
        nb = int(form.nb_element.data)
        return render_tetrino(form, nb)
    if request.method == 'GET':
        form.nb_element.data = 4
        form.doletter.data = False
        return render_template('fillit/fillit.html',
                                title='New Grid',
                                result = None,
                                data = None,
                                label = "", blank = True,
                                form=form)
    return redirect(url_for('fillit.fillit_route'))


@fillit.route('/fillit_ajax', methods=['POST','GET'])
def fillit_ajax():
    form = FillitForm()
    if not form.validate_on_submit():
        return jsonify({"success": False})
    nb = int(form.nb_element.data)
    if nb < 1:
        nb = 1
    t = do_tetrino.Tetrino()
    t.build_random(nb)
    t.do_play()
    perf = "perf for {} tetriminos: {:.3f}sec (grid {} x {} - coverage {:.2f}%)".format(nb, 
                                                                    t.delta,
                                                                    t.sqa,t.sqa,t.stat)
    label = "Inputs:"
    nb_col = max(int(nb/4), 4)

    if form.doletter.data in ["Do Anim" ,"Do 3D"]:
        do_3d = form.doletter.data == "Do 3D"
        xspace = 30
        yspace = 30
        rmargin = 20
        tmargin = 20
        spacing = 200
        scalegame = 0.15
        if do_3d:
            xspace = 21
            yspace = 21
            scalegame = 0.10

        sizex = ((nb_col + 1) * 5 * xspace) + (2 * rmargin)
        sizey = (tmargin * 2) + len(t.result) + len(t.data) + (spacing * 2) + tmargin
        htmlobjlist = ['<canvas id="myCanvas" width="%d" height="%d"></canvas>' % (sizex, sizey)]
        htmlobjlist.append('<button class="btn btn-outline-info" id="refresh">Replay Anim</button>')
        return jsonify({'success' : True,
                        'data': t.get_segment_anim(nb_col,
                                            xspace = xspace,
                                            yspace = yspace,
                                            rmargin = rmargin,
                                            tmargin = tmargin,
                                            spacing = spacing,
                                            scalegame = scalegame,
                                            for3d = do_3d),
                        'html' : "".join(htmlobjlist),
                        'sizex' : sizex,
                        'sizey' : sizey,
                        'canvas': True,
                        'for3d': do_3d})

    dotext = form.doletter.data == "Do Text"
    if dotext:
        inpt = t.show_in_line(nb_col, False)
        res = t.result
    else:
        inpt = t.show_in_line(nb_col, True)
        res = do_tetrino.Tetrino.wrap_box_result(t.result)
    html = render_template('fillit/fillit_ajax.html',
                            result = res,
                            data = inpt,
                            message = perf,
                            label = label,
                            dotext = dotext)
    return jsonify({'html': html, 'success' : True, 'canvas': False})
