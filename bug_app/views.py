from django.shortcuts import render, HttpResponseRedirect, reverse

from bug_tracker.settings import AUTH_USER_MODEL
from bug_app.models import MyUser, Ticket
from bug_app.forms import AddTicketForm, LoginForm, AssignTicketForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index_view(request):
    user = MyUser.objects.filter(username=request.user)
    tickets = Ticket.objects.filter(
        filed=request.user).order_by('-post_date')
    newTicket = tickets.filter(status="NEW")
    inprogress = tickets.filter(status="IN_PROGRESS")
    inValid = tickets.filter(status="INVALID")
    done = tickets.filter(status="DONE")

    return render(request, "index.html", {"users": user, "newTickets": newTicket,
                                          "progressTickets": inprogress, "doneTickets": done, "invalidTickets": inValid})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm
    return render(request, "generic_form.html", {"form": form})


def addTicket_view(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                filed=request.user,
                assigned=None,
                completed=None
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddTicketForm()
    return render(request, "generic_form.html", {"form": form})


def edit_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.description = data["description"]
            ticket.title = data["title"]
            ticket.save()
        return HttpResponseRedirect(reverse("homepage"))

    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    form = AddTicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})


def ticketDetail_view(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    # current_user = MyUser.objects.filter(username=request.user).first()
    return render(request, "ticketdetail.html", {"ticket": ticket})


def userdetail_view(request, user_id):
    current_user = MyUser.objects.filter(id=user_id).first()
    tickets = Ticket.objects.filter(filed=current_user)
    progress = tickets.filter(status="IN_PROGRESS")
    done = tickets.filter(status="DONE")
    return render(request, "userdetail.html", {"user": current_user, "tickets": tickets, "completed_tickets": done, "progress": progress})


def assignticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = AssignTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.status = data["status"]
            ticket.assigned = data["assigned"]
            ticket.save()

    data = {
        "status": "IN_PROGRESS",
        "assigned": ticket.assigned
    }
    form = AssignTicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


# if request.method == "POST":
    #     form = TicketDetailForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         ticket.ticket_actions = data["ticket_actions"]
    #         ticket.save()
    #     return HttpResponseRedirect(reverse("ticketDetail"))

    # data = {
    #     "ticket_actions": ticket.ticket_actions,

    # }
    # form = TicketDetailForm(initial=data)
