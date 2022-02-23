from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from datetime import datetime, timedelta
from datetime import *
import pytz
import copy
from dateutil import tz, parser
import json

from requests.api import delete
from scheduleSynchronizer.debug import *
from scheduleSynchronizer.consistency import *

from scheduleSynchronizer.auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from scheduleSynchronizer.graph_helper import *
from scheduleSynchronizer.web_scraper1111.search import look, Session

teams = {}


def home(request):
    context = initialize_context(request)
    print(context)

    return render(request, 'scheduleSynchronizer/home.html', context)

def guide(request):
    context = initialize_context(request)
    print(context)

    return render(request, 'scheduleSynchronizer/guide.html', context)

def initialize_context(request):
    context = {}

    # Check for any errors in the session
    error = request.session.pop('flash_error', None)

    if error != None:
        context['errors'] = []
        context['errors'].append(error)

    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context


def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])


def callback(request):
    # Make the token request
    result = get_token_from_code(request)

    # Get the user's profile
    user = get_user(result['access_token'])

    # Store user
    store_user(request, user)
    return HttpResponseRedirect(reverse('home'))


def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)

    return HttpResponseRedirect(reverse('home'))


# def dateFormat(dateTime):
#     date_split = dateTime.split("/")
#     date_month = ""
#     if date_split[1] == "Jan":
#         date_month = "01"
#     elif date_split[1] == "Feb":
#         date_month = "02"
#     elif date_split[1] == "Mar":
#         date_month = "03"
#     elif date_split[1] == "Apr":
#         date_month = "04"
#     elif date_split[1] == "May":
#         date_month = "05"
#     elif date_split[1] == "Jun":
#         date_month = "06"
#     elif date_split[1] == "Jul":
#         date_month = "07"
#     elif date_split[1] == "Aug":
#         date_month = "08"
#     elif date_split[1] == "Sep":
#         date_month = "09"
#     elif date_split[1] == "Oct":
#         date_month = "10"
#     elif date_split[1] == "Nov":
#         date_month = "11"
#     else:
#         date_month = "12"

#     date_time = date_split[2][:4] + "-" + date_month + "-" + date_split[0]
#     return date_time


def search_function(request):
    course_name = request.GET.get('courseName')
    course_name_tmp = course_name.split(" ")
    course_name_abb = ""
    for y in course_name_tmp:
        if (y[:1].isupper() and y[:1] != "&" and y[:1] != "("):
            course_name_abb = course_name_abb + y[:1]
    semester = request.GET.get('semester')
    sestype = request.GET.get('sestype')
    session_name = ""
    if sestype == "Lecture":
        session_name = "LE"
    elif sestype == "Workshop":
        session_name = "WR"
    elif sestype == "Seminar":
        session_name = "SE"
    else:
        session_name = "TU"
    
    # print(course_name)
    # print(semester)
    # print(sestype)

    result_list = look(course_name, semester, sestype)
    course_list = []
    for x in result_list:
        # print((datetime.strptime(dateFormat(x.sdate), "%Y-%m-%d") - datetime.today()).days,'--------',(x.startDateTime - datetime.today()).days)
        #   print(dateFormat(x.sdate) + " " + datetime.today().strftime("%Y-%m-%d") + "   " + str((datetime.strptime(dateFormat(x.sdate), "%Y-%m-%d") - datetime.today()).days))
        # if (datetime.strptime(dateFormat(x.sdate), "%Y-%m-%d") - datetime.today()).days >= -1:
        if (x.startDateTime - datetime.today()).days >= -1:
            course_list.append(x)
    for m in course_list:
        m.isMatched = -1

    context = initialize_context(request)

    # global teams
    # if there are teams in user's account
    # if 'value' in teams:
    if teams['value']:
        context['teams'] = teams['value']
        for team in teams['value']:
            for b in team['shifts']:
                b['Shift']['selectedOne'] = 0
                # print(b['Shift']['groupName'])
                # print(b['Shift']['displayName'][:2])
                if (b['Shift']['groupName'] == course_name or b['Shift']['groupName'] == course_name_abb) and b['Shift']['displayName'][:2] == session_name:
                    b['Shift']['selectedOne'] = 0
                    for z in course_list:
                        if z.sdate == b['Shift']['startDateTime'] and z.edate == b['Shift']['endDateTime'] and z.location == b['Shift']['notes'] and z.section == b['Shift']['displayName']:
                            # b['Shift']['isMatched'] = 0
                            z.isMatched = 0
                        else:
                            if z.isMatched == 0:
                                z.isMatched = 0
                            else:
                                z.isMatched = 1
                            # if b['Shift']['isMatched'] == 0:
                            #     b['Shift']['isMatched'] = 0
                            # else:
                            #     b['Shift']['isMatched'] = 1
                            #     if z.section != b['Shift']['displayName']:
                            #         b['Shift']['isDisplayName'] = 1
                            #     if z.sdate != b['Shift']['startDateTime']:
                            #         b['Shift']['isStartTime'] = 1
                            #     if z.edate != b['Shift']['endDateTime']:
                            #         b['Shift']['isEndTime'] = 1
                            #     if z.location != b['Shift']['notes']:
                            #         b['Shift']['isLocation'] = 1
                else:
                    b['Shift']['selectedOne'] = 1
    else:
        if 'error' in teams:
            print_json(teams)
            context = teams
    course_list = [course_list]
    context['result_list'] = course_list

    return render(request, 'scheduleSynchronizer/shift.html', context)
    # return HttpResponseRedirect(reverse('home'))


def delete_by_id(request):

    context = initialize_context(request)

    shift_id = request.POST.get('shift_id')
    teamID = request.POST.get('team_id')
    token = get_token(request)

    r = requests.delete('https://graph.microsoft.com/v1.0/teams/{0}/schedule/shifts/'.format(teamID)+shift_id,
                        headers={'Authorization': 'Bearer {0}'.format(token)})

    for team in teams['value']:
        if team['id'] == teamID:
            for shift in team['shifts']:
                if shift['id'] == id:
                    del shift
                    break
                break

    context['teams'] = teams

    return HttpResponseRedirect(reverse('shift'))


def delete_incorrect_shifts(request):
    context = initialize_context(request)
    user = context['user']

    time_zone = get_iana_from_windows(user['timeZone'])
    tz_info = tz.gettz(time_zone)
    # timeZone = pytz.timezone(time_zone)

    # Get midnight today in user's time zone
    # date_now = datetime.now(timeZone)
    today = datetime.now(tz_info).replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0)


    token = get_token(request)

    number_teams = 0
    global teams
    # if there are teams in user's account
    if teams['value']:
        # print_json(teams)
        context = teams
        for team in teams['value']:
            team_name = team['displayName']
            team_ID = team['id']

            # print("-------------------------printing team-------------------------")
            # print(team)
            shifts = teams['value']

            # if there are shifts in the team
            if shifts:
                shifts = shifts[0]
                for shift in shifts['shifts'][::-1]:
                    if shift['Shift']['isMatched'] != 0:
                        delete(shift, team_ID, token)
                number_teams += 1
            else:
                print(
                    '-------------------------no shift was found-------------------------')
                print_json(shifts)
                team['shifts'] = shifts['value']
    else:
        print('-------------------------no team was found-------------------------')
        context['teams'] = teams['value']
    # print_json(teams)
    # print(time_zone)
    # print("testing view.delete_incorrect_shifts")
    return HttpResponseRedirect(reverse('shift'))


def shift(request):
    context = initialize_context(request)
    user = context['user']

    # Load the user's time zone
    # Microsoft Graph can return the user's time zone as either
    # a Windows time zone name or an IANA time zone identifier
    # Python datetime requires IANA, so convert Windows to IANA
    time_zone = get_iana_from_windows(user['timeZone'])
    tz_info = tz.gettz(time_zone)
    timeZone = pytz.timezone(time_zone)

    # Get midnight today in user's time zone
    # date_now = datetime.now(timeZone)
    # today = datetime.now(tz_info).replace(
    #     hour=0,
    #     minute=0,
    #     second=0,
    #     microsecond=0)

    # Based on today, get the start of the week (Sunday)
    # if (today.weekday() != 6):
    #   start = today - timedelta(days=today.isoweekday())
    # else:
    start = datetime.now(timezone.utc)

    # end = start + timedelta(days=7)
    # start = start - timedelta(days=1)

    token = get_token(request)
    global teams
    teams = get_teams(token)

    number_teams = 0

    # if there are teams in user's account
    # if 'value' in teams:
    if teams['value']:
        # print_json(teams)
        context['teams'] = teams['value']
        for team in teams['value']:
            team_name = team['displayName']
            team_ID = team['id']

            # print("-------------------------printing team-------------------------")
            # print(team)
            members = get_members(token,team_ID)
            team['members'] = members
            # print_json(team)
            shifts = get_shift(
                token,
                start.isoformat(timespec='seconds'),
                # end.isoformat(timespec='seconds'),
                user['timeZone'],
                team_ID
            )

            # if there are shifts in the team
            # if 'value' in shifts:
            if shifts['value']:
                # print_json(shifts)
                # Convert the ISO 8601 date times to a datetime object
                # This allows the Django template to format the value nicely
                # print ("-------------------------printing shifts-------------------------")
                # print_json(shifts)
                for shift in shifts['value']:
                    shift['Shift'] = copy.deepcopy(shift['draftShift'])
                    shift['Shift']['startDateTime'] = parser.parse(
                        shift['draftShift']['startDateTime'])
                    shift['Shift']['endDateTime'] = parser.parse(
                        shift['draftShift']['endDateTime'])
                    # assign timezone
                    shift['Shift']['startDateTime'] = shift['Shift']['startDateTime'].astimezone(
                        timeZone)
                    shift['Shift']['endDateTime'] = shift['Shift']['endDateTime'].astimezone(
                        timeZone)
                    # change date type to string
                    shift['Shift']['startDateTime'] = shift['Shift']['startDateTime'].strftime(
                        '%d/%b/%Y, %H:%M')
                    shift['Shift']['endDateTime'] = shift['Shift']['endDateTime'].strftime(
                        '%d/%b/%Y, %H:%M')
                    # get the group name(course name) of the shift
                    shift['Shift']['groupName'] = get_group_name(
                        token, team_ID, shift['schedulingGroupId'])
                    # get user name by ID
                    shift['Shift']['userName'] = get_user_name(team,shift['userId'])
                    # try to match this shift to the course planner
                    # shift['Shift']['isMatched'] = 3
                    shift['Shift']['isMatched'] = match(shift['Shift'])
                team['shifts'] = shifts['value']
                number_teams += 1
            else:
                print(
                    '-------------------------no shift was found-------------------------')
                print_json(shifts)
                team['shifts'] = shifts['value']

                if 'error' in shifts.keys():
                    print('error:')
                    print_json(shifts)
                    team['error'] = shifts['error']
                    print_json(context)
            # else:
            # 	if 'error' in shifts.keys():
            # 		print('error:')
            # 		print_json(shifts)
            # 		team['error'] = shifts['error']
            # 		print_json(context)
    else:
        print('-------------------------no team was found-------------------------')
        print_json(teams)
        context['teams'] = teams['value']
    # else:
    #     if 'error' in teams.keys():
    #         print_json(teams)
    #         context = teams
    course_list = get_courses_cache().values
    context['result_list'] = course_list

    return render(request, 'scheduleSynchronizer/shift.html', context)


def calendar(request):
    context = initialize_context(request)
    user = context['user']

    # Load the user's time zone
    # Microsoft Graph can return the user's time zone as either
    # a Windows time zone name or an IANA time zone identifier
    # Python datetime requires IANA, so convert Windows to IANA
    time_zone = get_iana_from_windows(user['timeZone'])
    tz_info = tz.gettz(time_zone)

    # Get midnight today in user's time zone
    today = datetime.now(tz_info).replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0)

    # Based on today, get the start of the week (Sunday)
    if (today.weekday() != 6):
        start = today - timedelta(days=today.isoweekday())
    else:
        start = today

    end = start + timedelta(days=7)

    token = get_token(request)

    events = get_calendar_events(
        token,
        start.isoformat(timespec='seconds'),
        end.isoformat(timespec='seconds'),
        user['timeZone'])

    if events:
        # Convert the ISO 8601 date times to a datetime object
        # This allows the Django template to format the value nicely
        for event in events['value']:
            event['start']['dateTime'] = parser.parse(
                event['start']['dateTime'])
            event['end']['dateTime'] = parser.parse(event['end']['dateTime'])

        context['events'] = events['value']

    return render(request, 'scheduleSynchronizer/calendar.html', context)


def newevent(request):
    context = initialize_context(request)
    print(context)
    user = context['user']

    if request.method == 'POST':
        # Validate the form values
        # Required values
        if (not request.POST['ev-subject']) or \
           (not request.POST['ev-start']) or \
           (not request.POST['ev-end']):
            context['errors'] = [
                {'message': 'Invalid values',
                 'debug': 'The subject, start, and end fields are required.'}
            ]
            return render(request, 'scheduleSynchronizer/newevent.html', context)

        attendees = None
        if request.POST['ev-attendees']:
            attendees = request.POST['ev-attendees'].split(';')
        body = request.POST['ev-body']

        # Create the event
        token = get_token(request)

        create_event(
            token,
            request.POST['ev-subject'],
            request.POST['ev-start'],
            request.POST['ev-end'],
            attendees,
            request.POST['ev-body'],
            user['timeZone'])

        # Redirect back to calendar view
        return HttpResponseRedirect(reverse('calendar'))
    else:
        # Render the form
        return render(request, 'scheduleSynchronizer/newevent.html', context)
    print('hello')