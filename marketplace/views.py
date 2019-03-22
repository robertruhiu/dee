from collections import Counter

import requests
from decouple import config
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from classroom.models import Student, TakenQuiz
from frontend.form import Portfolio_form, Experience_Form, Github_form
from frontend.models import Github, Experience, Portfolio
from marketplace.filters import UserFilter
from .models import Job, JobApplication
from .forms import JobForm


def job_list(request):
    jobs = Job.objects.all()
    applied_jobs = ()
    if request.user.is_authenticated:
        developer = request.user
        applied_jobs = JobApplication.objects.filter(candidate=developer)
    return render(request, 'frontend/jobs.html', {'jobs': jobs, 'applied_jobs': applied_jobs})


def job_details(request, id):
    if request.user.profile.user_type == 'recruiter':
        job = Job.objects.get(id=id)

        selected_candidates = []
        applicants = []
        selected_devs = JobApplication.objects.filter(selected=True).all()
        for selectdev in selected_devs:
            selected_candidates.append(selectdev.candidate)
        all_devs = JobApplication.objects.filter(selected=False).all()
        for alldev in all_devs:
            applicants.append(alldev.candidate)

        recommended = [dev for dev in get_recommended_developers(job) if dev not in selected_candidates]

        return render(request, 'marketplace/recruiter/jobs/detail.html',
                      {'job': job, 'applicants': applicants, 'recommended': recommended,
                       'selected_candidates': selected_candidates})
    elif request.user.profile.user_type == 'developer':
        status = JobApplication.objects.filter(job_id=id).filter(candidate=request.user).all()
        job = Job.objects.get(id=id)
        return render(request, 'marketplace/developer/jobs/detail.html',
                      {'job': job, 'status': status})


@login_required
def post_job(request):
    recruiter = request.user

    if request.method == 'POST':
        job_form = JobForm(data=request.POST)
        if job_form.is_valid():
            new_job = job_form.save(commit=False)
            new_job.posted_by = recruiter
            new_job.save()
            return HttpResponseRedirect(reverse('marketplace:manage_posted_jobs'))
    else:
        job_form = JobForm()
        return render(request, 'marketplace/recruiter/jobs/create.html', {'job_form': job_form})


@login_required
def apply_for_job(request, job_id):
    if request.method == 'POST':
        subject = 'Job Application received'
        html_message = render_to_string('invitations/email/jobapplications.html',
                                        {'dev': request.user})
        plain_message = strip_tags(html_message)
        from_email = 'codeln@codeln.com'
        to = request.user.email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        job = Job.objects.get(id=job_id)
        newapply = JobApplication(candidate=request.user, job=job)
        newapply.save()
        return redirect(reverse('marketplace:job_list'))
    else:
        return redirect(reverse('marketplace:job_list'))


def manage_posted_jobs(request):
    jobs = Job.objects.filter(posted_by=request.user)
    job_details = []
    for job in jobs:
        applied = JobApplication.objects.filter(job_id=job.id).all()
        app = applied.count()
        selected = JobApplication.objects.filter(job_id=job.id).filter(selected=True).all()
        sele = selected.count()
        job_details.append((job, app, sele))

    return render(request, 'marketplace/recruiter/jobs/list.html', {'job_details': job_details})


def pick_candidate(request, job_id, dev_id):
    job = Job.objects.get(id=job_id)
    dev = User.objects.get(id=dev_id)
    newpick = JobApplication(job=job, candidate=dev, selected=True)
    newpick.save()

    return HttpResponseRedirect(reverse('marketplace:recruiter_job_detail', args=(job_id,)))


def select_candidate(request, job_id, dev_id):
    candidate = User.objects.get(id=dev_id)
    job = JobApplication.objects.filter(job_id=job_id).filter(candidate=candidate).get()
    job.selected = True
    job.save()
    return HttpResponseRedirect(reverse('marketplace:recruiter_job_detail', args=(job_id,)))


def get_recommended_developers(job):
    job_tags = [job.engagement_type, job.job_role, job.location.name, job.dev_experience, job.tech_stack]

    developers = User.objects.filter(profile__user_type='developer').filter(
        profile__tags__name__in=job_tags)

    return developers


def dev_pool(request):
    developers = User.objects.filter(profile__user_type='developer')

    if request.method == 'POST':
        search_field = request.POST['search_field']

        developers_filter = UserFilter(request.POST, queryset=developers)

        filtered_devs = developers_filter.qs

        developers = filtered_devs.filter(
            Q
            (username__icontains=search_field)
            | Q(first_name__icontains=search_field)
            | Q(last_name__icontains=search_field)
            | Q(profile__gender__icontains=search_field)
            | Q(profile__framework__icontains=search_field)
            | Q(profile__language__icontains=search_field)
        )

        developers = [dev for dev in developers]

        return render(request, 'marketplace/recruiter/dev_pool.html',
                      {'developers': developers, 'search_form': developers_filter.form})
    else:
        developers_filter = UserFilter(request.GET, queryset=developers)
        developers = [dev for dev in developers_filter.qs]

        return render(request, 'marketplace/recruiter/dev_pool.html',
                      {'developers': developers, 'search_form': developers_filter.form})


def dev_details(request, dev_id):
    requested_dev = User.objects.get(id=dev_id)
    try:
        candidate = Github.objects.get(candidate=requested_dev)
        user = candidate.github_username
        username = config('GITHUB_USERNAME', default='GITHUB_USERNAME')
        token = config('ACCESS_TOKEN', default='ACCESS_TOKEN')
        json_data = requests.get('https://api.github.com/users/' + user, auth=(username, token)).json()

        form = Portfolio_form()
        experience_form = Experience_Form()
        repo = 'https://api.github.com/users/' + user + '/repos'
        repos = requests.get(repo, auth=(username, token)).json()
        paginator = Paginator(repos, 8)

        page = request.GET.get('page')
        repoz = paginator.get_page(page)
        languages = []

        for i in repos:
            for x in i:
                languages.append(i['language'])

        counter = Counter(languages)
        labels = []
        c = {}
        items = []
        for z in counter:
            c[z] = counter[z]
            labels.append(z)
            items.append(counter[z])
        data = {
            "labels": labels,
            "data": items,
        }
        student = Student.objects.get(user_id=dev_id)
        verified_skills = TakenQuiz.objects.filter(student=student).filter(score__gte=50).all()
        skill = []
        for verified_skill in verified_skills:
            skill.append(verified_skill.quiz.subject.name)
        skillset = set(skill)
        skills = list(skillset)

        experiences = Experience.objects.filter(candidate=requested_dev).all()
        verified_projects = Portfolio.objects.filter(candidate=requested_dev).all()
        return render(request, 'marketplace/recruiter/dev_portfolio.html',
                      {'json': json_data, 'repos': repoz, 'data': data, 'c': c, 'form': form,
                       'verified_projects': verified_projects, 'experience_form': experience_form,
                       'experiences': experiences, 'skills': skills, 'developer': requested_dev})
    except Github.DoesNotExist:
        form = Github_form()

        return render(request, 'frontend/developer/github.html', {'form': form})
