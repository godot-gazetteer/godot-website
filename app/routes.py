from flask import render_template, request, jsonify, redirect
from flask_simplelogin import login_required
from app import app
from app.forms import RomanConsularDating, CyrenaicaYears, AttestationUpdate, AttestationDelete, CyrenaicaRomanImperialTitulature, SearchRomanConsulate, EgyptianCalendarLatePeriod, EgyptianCalendarPtolemies, EgyptianCalendarRomanEmperors, RomanImperialDating, EponymOffice, EponymOfficial
from app.convert import Convert_roman_calendar
from app.EgyptianCalendarDate import EgyptianCalendarDate
from app.neo4j_utils import *
from app.cyrenaica import write_cyrenaica_single_year, write_cyrenaica_emperor_titulature_path
import simplejson as json
from app.openrefine_utils import search, get_openrefine_metadata
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/browse', defaults={'yrs': 'All', 'yrs2': 1})
@app.route('/browse/<yrs>', defaults={'yrs2': 1})
@app.route('/browse/<yrs>/<yrs2>')
def browse(yrs, yrs2):
    list_of_yrs = get_list_of_yrs()
    if yrs == "Regnal Years - Roman Emperors":
        if yrs2 == 1:
            # show list of emperors names
            emperors_list = get_all_roman_emperors()
            return render_template('browse_emperors.html', title='Browse Data', browse_data=emperors_list, list_of_yrs=list_of_yrs, yrs=yrs)
        else:
            # show all regnal years of specified emperor
            emperors_list = get_all_roman_emperors()
            regnal_years_list = get_regnal_years_for_emperor(yrs2)
            return render_template('browse_emperors_detail.html', title='Browse Data', browse_data=emperors_list,
                                   list_of_yrs=list_of_yrs, yrs=yrs, yrs2=yrs2, regnal_years_list=regnal_years_list)

    else:
        pass
    browse_data = get_browse_data(yrs, yrs2)

    total_hits = get_browse_data_number_of_results(yrs)
    return render_template('browse.html', title='Browse Data', browse_data=browse_data, list_of_yrs=list_of_yrs,
                           yrs=yrs, page=yrs2, total_hits=total_hits)


@app.route('/contact')
def contact():
    number_of_nodes = get_number_of_nodes()
    number_of_relations = get_number_of_relations()
    number_of_godot_uris = get_number_of_godot_uris()
    return render_template('contact.html', title='Contact', number_of_nodes=number_of_nodes,
                           number_of_relations=number_of_relations, number_of_godot_uris=number_of_godot_uris)


@app.route('/about')
def about():
    return render_template('about.html', title='About GODOT', about_text='About GODOT')


@app.route('/data/edh')
def data_edh():
    return render_template('data_edh.html', title='GODOT Data: Epigraphic Database Heidelberg', data_text='GODOT Data: Epigraphic Database Heidelberg')


@app.route('/data/tm')
def data_tm():
    return render_template('data_tm.html', title='GODOT Data: Trismegistos', data_text='GODOT Data: Trismegistos')


@app.route('/data/ircyr')
def data_ircyr():
    return render_template('data_ircyr.html', title='GODOT Data: IRCyr', data_text='GODOT Data: IRCyr')


@app.route('/data')
def data():
    return render_template('data.html', title='GODOT Data', data_text='GODOT Data')


@app.route('/id/<godot_uri>')
def display_godot_uri(godot_uri):
    # get data/path and attestation links for this GODOT URI as list of dicts
    paths = get_godot_path("https://godot.date/id/" + godot_uri)
    # some info needn't be displayed on detail view page
    date_dict = {}
    path_list = []
    for p_dict in paths:
        if p_dict['label'] == 'GODOT' and p_dict['type'] == 'synchron':
            continue
        else:
            path_list.append(p_dict)
    paths = path_list
    attestations = get_attestations("https://godot.date/id/" + godot_uri)
    if paths:
        return render_template('detail.html', title='Detail view', id=godot_uri, paths=paths, attestations=attestations)
    else:
        return render_template('404.html'), 404


@app.route('/id/<godot_uri>/<node_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_attestation_data(godot_uri, node_id):
    form = AttestationUpdate()
    date_category = form.date_category.data
    date_categories = ['', 'Uncategorised', 'Date of Death', 'Date of Birth', 'Date of Document', 'Date of Recording', 'Date of Action', 'Date of Office', 'Recurring Date of Action', 'Roman Emperor Titulature']
    if form.validate_on_submit():
        attestation_uri = form.attestation_uri.data
        title = form.title.data
        date_string = form.date_string.data
        date_category = form.date_category.data
        if update_attestation(node_id, attestation_uri, title, date_string, date_category):
            return redirect("/id/" + godot_uri)
    paths = get_godot_path("https://godot.date/id/" + godot_uri)
    # some info needn't be displayed on detail view page
    path_list = []
    for p_dict in paths:
        if p_dict['label'] == 'GODOT' and p_dict['type'] == 'synchron':
            continue
        else:
            path_list.append(p_dict)
    paths = path_list
    attestation = get_attestation(node_id)
    if paths:
        return render_template('update_attestation_data.html', title='Edit Attestation Data', id=godot_uri, paths=paths, attestations=attestation, date_categories=date_categories, form=form)
    else:
        return render_template('404.html'), 404


@app.route('/id/<godot_uri>/<node_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_attestation_node(godot_uri, node_id):
    form = AttestationDelete()
    if form.validate_on_submit():
        if delete_attestation(node_id):
            return redirect("/id/" + godot_uri)
    paths = get_godot_path("https://godot.date/id/" + godot_uri)
    # some info needn't be displayed on detail view page
    path_list = []
    for p_dict in paths:
        if p_dict['label'] == 'GODOT' and p_dict['type'] == 'synchron':
            continue
        else:
            path_list.append(p_dict)

    paths = path_list
    attestation = get_attestation(node_id)
    if paths:
        return render_template('delete_attestation_data.html', title='Delete Attestation Data', id=godot_uri, paths=paths, attestations=attestation, form=form)
    else:
        return render_template('404.html'), 404


@app.route('/convert/roman_consuls', methods=['GET', 'POST'])
def roman_consuls():
    form = RomanConsularDating()
    if form.consulship.data is not None:
        # date validation: some date combinations are not valid

        #
        # convert date from roman calendar with consulship
        # get year from form.consulship.data (number at beginning of string until colon)
        year = form.consulship.data.split(':')[0]
        converted_date = Convert_roman_calendar.consulship(
            form.day_number.data, form.day_ref.data, form.months.data, year)
        result_string = converted_date
        consulate = form.consulship.data
        if '|' in form.consulship.data:
            consul_label, godot_uri = form.consulship.data.split('|')
            day_number_label = Convert_roman_calendar.get_day_number_label(form.day_number.data)
            # return conversion result to template
            return render_template('roman_consuls_result.html', title='Roman Consuls', consulship=consul_label,
                                   day_ref=form.day_ref.data, day_number=day_number_label, month=form.months.data,
                                   result=result_string)
    return render_template('roman_consuls.html', title='Roman Consular Dating', form=form)


@app.route('/convert/roman_emperors', methods=['GET', 'POST'])
def roman_emperors():
    form = RomanImperialDating()
    if form.validate_on_submit():
        pass
    return render_template('roman_emperors.html', title='Roman Imperial Dating', form=form)


@app.route('/convert/egyptian/late_period', methods=['GET', 'POST'])
def convert_egyptian_late_period():
    form = EgyptianCalendarLatePeriod()
    if form.validate_on_submit():
        reign = form.late_period_pharaos.data
        year = form.year.data
        month = form.egyptian_calendar_months.data
        day = form.day.data
        lp_date = EgyptianCalendarDate('latePeriod', reign, year, month, day)
        converted_date_json = lp_date.convert_to_julian()
        return render_template('convert_egyptian_late_period_result.html',
            reign=reign, year=year, month=month, day=day, response=converted_date_json)
    return render_template('convert_egyptian_late_period.html', form=form)


@app.route('/convert/egyptian/ptolemies', methods=['GET', 'POST'])
def convert_egyptian_ptolemies():
    form = EgyptianCalendarPtolemies()
    if form.validate_on_submit():
        reign = form.ptolemaic_pharaos.data
        year = form.year.data
        month = form.egyptian_calendar_months.data
        day = form.day.data
        ptolemaic_date = EgyptianCalendarDate('ptolemies', reign, year, month, day)
        converted_date_json = ptolemaic_date.convert_to_julian()
        return render_template('convert_egyptian_ptolemies_result.html',
            reign=reign, year=year, month=month, day=day, response=converted_date_json)
    return render_template('convert_egyptian_ptolemies.html', form=form)


@app.route('/convert/egyptian/roman_emperors', methods=['GET', 'POST'])
def convert_egyptian_roman_emperors():
    form = EgyptianCalendarRomanEmperors()
    if form.validate_on_submit():
        reign = form.roman_emperors.data
        year = form.year.data
        month = form.egyptian_calendar_months.data
        day = form.day.data
        roman_emperor_date = EgyptianCalendarDate('romanEmperors', reign, year, month, day)
        converted_date_json = roman_emperor_date.convert_to_julian()
        return render_template('convert_egyptian_roman_emperors_result.html',
            reign=reign, year=year, month=month, day=day, response=converted_date_json)
    return render_template('convert_egyptian_roman_emperors.html', form=form)


@app.route('/cyrenaica/roman_imperial_titulature', methods=['GET', 'POST'])
@login_required
def cyrenaica_roman_emperor_titulature():
    form = CyrenaicaRomanImperialTitulature()
    if form.validate_on_submit():
        roman_emperor = form.roman_emperors.data
        consul_number = form.consul_number.data
        consul_designatus = form.consul_designatus.data
        trib_pot_number = form.trib_pot_number.data
        imperator_number = form.imperator_number.data
        victory_titles = form.victory_titles.data
        date_category = form.date_category.data
        attestation_uri = form.attestation_uri.data
        date_string = form.date_string.data
        date_title = form.title.data
        godot_uri = write_cyrenaica_emperor_titulature_path(roman_emperor, consul_number, consul_designatus, trib_pot_number, imperator_number, victory_titles, attestation_uri,
                                         date_string, date_title, date_category)
        return render_template('cyrenaica_emperors_result.html',
                               title='Cyrenaica Roman Imperial Titulature',
                               attestation_uri=attestation_uri,
                               date_string=date_string,
                               date_title=date_title,
                               roman_emperor=roman_emperor,
                               consul_number=consul_number,
                               consul_designatus=consul_designatus,
                               trib_pot_number=trib_pot_number,
                               imperator_number=imperator_number,
                               victory_titles=victory_titles,
                               godot_uri=godot_uri.split("/")[-1],
                               date_category=date_category,
                               form=form)
    return render_template('cyrenaica_emperors.html', title='Cyrenaica Roman Imperial Titulature', form=form)


@app.route('/cyrenaica/single_year', methods=['GET', 'POST'])
@login_required
def cyrenaica_years():
    form = CyrenaicaYears()
    if form.validate_on_submit():
        yrs = form.year_reference_system.data
        apollo_priest = form.apollo_priests_cyrenaica.data
        roman_emperor = form.roman_emperors.data
        year = form.year.data
        month = form.egyptian_calendar_months.data
        day = form.day.data
        date_category = form.date_category.data
        attestation_uri = form.attestation_uri.data
        date_string = form.date_string.data
        date_title = form.title.data
        godot_uri = write_cyrenaica_single_year(yrs, apollo_priest, roman_emperor, year, month, day, attestation_uri,
                                                date_string, date_title, date_category)
        if yrs == "Eponymous Officials: Apollo Priest (Cyrenaica)":
            roman_emperor = ""
        elif yrs == "Regnal: Roman Emperors":
            apollo_priest = ""
        else:
            apollo_priest = ""
            roman_emperor = ""
        if godot_uri:
            return render_template('cyrenaica_years_result.html', title='Cyrenaica Year Dating', yrs=yrs,
                               apollo_priest=apollo_priest, roman_emperor=roman_emperor, year=year, month=month,
                               day=day, attestation_uri=attestation_uri, date_string=date_string, date_category=date_category, date_title=date_title, godot_uri=godot_uri.split("/")[-1])
    return render_template('cyrenaica_years.html', title='Cyrenaica Year Dating', form=form)


@app.route('/tools/openrefine')
def tools_openrefine():
    return render_template('tools_openrefine.html', title="Tools: OpenRefine")


@app.route('/tools/api')
def tools_api():
    return render_template('tools_api.html', title="Tools: API")


@app.route('/tools/search/consulate', methods=['GET', 'POST'])
def tools_search_consulate():
    form = SearchRomanConsulate()
    if form.validate_on_submit():
        if "|" in form.consulship.data:
            godot_uri = form.consulship.data.split('|')[1].strip()
            consulate = form.consulship.data.split('|')[0].strip()
            attestations = get_attestations(godot_uri)
            property_dict = get_godot_node_properties(godot_uri)
            return render_template('search_consulate_result.html', attestations=attestations, consulate=consulate, godot_uri=godot_uri, property_dict=property_dict, form=form)
    return render_template('search_consulate.html', title="Tools: Search Roman Consulate", form=form)


def _jsonpify(obj):
    try:
        callback = request.args['callback']
        response = app.make_response("%s(%s)" % (callback, json.dumps(obj)))
        response.mimetype = "text/javascript"
        return response
    except KeyError:
        return jsonify(obj)


@app.route("/api/openrefine/reconcile", methods=['POST', 'GET'])
def reconcile():
    query = request.args.get('query')
    queries = request.form.get('queries')
    if query:
        if query.startswith("{"):
            query = json.loads(query)['query']
        results = search(query)
        return _jsonpify({"result": results})
    if queries:
        queries = json.loads(queries)
        results = {}
        for (key, query) in queries.items():
            results[key] = {"result": app.search(query['query'])}
        return _jsonpify(results)
    return _jsonpify(get_openrefine_metadata())


@app.route('/eponymous_office/add', methods=['GET', 'POST'])
def eponymous_office_add():
    form = EponymOffice()
    if form.validate_on_submit():
        description = form.description.data
        wikidata_uri = form.wikidata_uri.data
        pleiades_uri = form.pleiades_uri.data
        place_label = form.place_label.data
        type = form.type.data
        godot_uri = get_godot_uri_for_eponymous_office(type, place_label, pleiades_uri, wikidata_uri, description)
        return render_template('eponymous_office_add_result.html', title="Add Eponymous Office Result",
                               data_text="Add Eponymous Office Result", description=description, wikidata_uri=wikidata_uri, pleiades_uri=pleiades_uri, place_label=place_label, type=type, godot_uri=str(godot_uri.split("/")[-1]))
    return render_template('eponymous_office_add.html', title="Add Eponymous Office", data_text="Add Eponymous Office", form=form)


@app.route('/eponymous_office/<godot_id>/edit', methods=['GET', 'POST'])
@login_required
def eponyms_detailview_edit(godot_id):
    form = EponymOffice()
    eponym_data = get_eponym_data(godot_id)
    if form.validate_on_submit():
        description = form.description.data
        wikidata_uri = form.wikidata_uri.data
        pleiades_uri = form.pleiades_uri.data
        godot_uri = form.godot_uri.data
        place_label = form.place_label.data
        type = form.type.data
        godot_uri = update_godot_uri_for_eponymous_office(type, place_label, pleiades_uri, wikidata_uri, description)
        return render_template('eponymous_office_add_result.html', title="Edit Eponymous Office Result",
                               data_text="Edit Eponymous Office Result", description=description,
                               wikidata_uri=wikidata_uri, pleiades_uri=pleiades_uri, place_label=place_label, type=type,
                               godot_uri=str(godot_uri.split("/")[-1]))
    else:
        return render_template('detail_eponym_edit.html', title="Edit Eponymous Office",
                           data_text="Edit Eponymous Office", eponym_data=eponym_data, godot_id=godot_id, form=form)


@app.route('/eponymous_office/<godot_id>')
def eponyms_detailview(godot_id):
    # show all information for this eponym
    eponym_data = get_eponym_data(godot_id)
    individuals_list = get_individuals_for_eponym(godot_id)
    pleiades_info = _get_pleiades_info(eponym_data['pleiades_uri'])
    return render_template('detail_eponym.html', title="Eponymous Office Detail View", data_text="Eponymous Office Detail View", eponym_data=eponym_data, individuals_list=individuals_list, pleiades_info=pleiades_info, godot_id=godot_id)


@app.route('/eponymous_office')
def eponyms_list():
    # get all eponymous offices node information
    eponyms_list = get_eponyms()
    return render_template('eponyms_list.html', title="Eponyms", data_text="Eponyms", eponyms_list=eponyms_list)


@app.route('/eponymous_office/<godot_id>/add', methods=['GET', 'POST'])
def eponymous_official_add(godot_id):
    form = EponymOfficial()
    office_data = get_eponym_data(godot_id)
    if form.validate_on_submit():
        name = form.name.data
        office_godot_uri = "https://godot.date/id/"+godot_id
        wikidata_uri = form.wikidata_uri.data
        snap_uri = form.snap_uri.data
        not_before = form.not_before.data
        not_after = form.not_after.data
        official_godot_uri = get_godot_uri_for_eponymous_official(office_godot_uri, name, wikidata_uri, snap_uri, not_before, not_after)
        return render_template('eponymous_official_add_result.html', title="Add Eponymous Official Result",
                               data_text="Add Eponymous Office Result", name=name, wikidata_uri=wikidata_uri, snap_uri=snap_uri, not_before=not_before, not_after=not_after, official_godot_uri=str(official_godot_uri.split("/")[-1]), office_godot_uri=str(office_godot_uri.split("/")[-1]), office_data=office_data)
    return render_template('eponymous_official_add.html', title="Add Eponymous Official", data_text="Add Eponymous Official", form=form, godot_uri='https://godot.date/id/'+godot_id, office_data=office_data)


@app.route('/eponymous_office/<office_godot_id>/<official_godot_id>/edit', methods=['GET', 'POST'])
def eponymous_official_edit(office_godot_id, official_godot_id):
    form = EponymOfficial()
    official_data_dict = get_official_data(official_godot_id)
    office_data = get_office_data_by_official_id(official_godot_id)
    if form.validate_on_submit():
        name = form.name.data
        office_godot_uri = "https://godot.date/id/"+office_godot_id
        wikidata_uri = form.wikidata_uri.data
        snap_uri = form.snap_uri.data
        not_before = form.not_before.data
        not_after = form.not_after.data
        official_data = update_eponymous_official_data(official_godot_id, name, wikidata_uri, snap_uri, not_before, not_after)
        return render_template('eponymous_official_add_result.html', title="Edit Eponymous Official Result",
                               data_text="Edit Eponymous Office Result", name=official_data['value'], wikidata_uri=official_data['wikidata_uri'], snap_uri=official_data['snap_uri'], not_before=official_data['not_before'], not_after=official_data['not_after'], official_godot_uri=official_godot_id, office_godot_uri=office_godot_id)
    return render_template('eponymous_official_edit.html', title="Edit Eponymous Official", data_text="Edit Eponymous Official", form=form, official_godot_uri='https://godot.date/id/'+official_godot_id, official_data=official_data_dict, office_data=office_data)


@app.route('/eponymous_office/<office_godot_id>/<official_godot_id>')
def eponymous_official(office_godot_id, official_godot_id):
    form = EponymOfficial()
    official_data_dict = get_official_data(official_godot_id)
    office_data = get_office_data_by_official_id(official_godot_id)
    return render_template('eponymous_official_add_result.html', title="Eponymous Official Detail View",
                           data_text="Eponymous Official Detail View", name=official_data_dict['value'],
                           wikidata_uri=official_data_dict['wikidata_uri'], snap_uri=official_data_dict['snap_uri'],
                           not_before=official_data_dict['not_before'], not_after=official_data_dict['not_after'],
                           official_godot_uri=official_godot_id, office_godot_uri=office_godot_id, office_data=office_data)

@app.route('/workshop')
def workshop():
    return render_template('workshop.html', title="Workshop")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def _get_pleiades_info(pleiades_uri):
    """
    queries pleiades json for names & coordinates of place
    :param pleiades_uri:
    :return: dictionary
    """
    place_information_dict = {}
    print("huhu")
    try:
        r = requests.get(pleiades_uri+'/json', timeout=4)
        names = r.json()['names']
        names_list = []
        for name in names:
            if name['attested']:
                names_list.append(name['attested'])
            else:
                names_list.append(name['romanized'])
        # reverse order lat/lng vs. lng/lat
        coordinates = r.json()['reprPoint'][::-1]
        place_information_dict['names'] = names_list
        place_information_dict['coordinates'] = coordinates
        return place_information_dict
    except:
        return {'error':'Service not available'}
