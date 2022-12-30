# Generated by Django 1.9.9 on 2016-11-30 08:30
import cmsplugin_survey.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=150, verbose_name="question")),
                (
                    "limit",
                    models.CharField(
                        choices=[("S", "1 vote per session"), ("U", "1 vote per user")],
                        default="S",
                        max_length=1,
                        verbose_name="limit",
                    ),
                ),
                (
                    "users_voted",
                    models.ManyToManyField(
                        editable=False,
                        related_name="cmsplugin_survey_votes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="users voted",
                    ),
                ),
                (
                    "closed",
                    models.BooleanField(default=False, verbose_name="voting closed"),
                ),
            ],
            options={
                "ordering": ("-id",),
                "verbose_name": "question",
                "verbose_name_plural": "questions",
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="cmsplugin_survey.Question",
                        verbose_name="question",
                    ),
                ),
                ("answer", models.CharField(max_length=150, verbose_name="answer")),
                (
                    "color",
                    cmsplugin_survey.fields.ColorField(
                        max_length=10, verbose_name="color"
                    ),
                ),
                (
                    "order",
                    models.IntegerField(blank=True, default=0, verbose_name="order"),
                ),
            ],
            options={
                "ordering": ("order",),
                "verbose_name": "answer",
                "verbose_name_plural": "answers",
            },
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="cmsplugin_survey.Answer",
                        verbose_name="answer",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="time"),
                ),
            ],
            options={
                "ordering": ("created",),
                "verbose_name": "vote",
                "verbose_name_plural": "votes",
            },
        ),
        migrations.CreateModel(
            name="QuestionPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="cmsplugin_survey_questionplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "template",
                    models.CharField(
                        choices=settings.CMSPLUGIN_SURVEY_TEMPLATES,
                        default=settings.CMSPLUGIN_SURVEY_TEMPLATES[0][0],
                        help_text="The template used to render plugin.",
                        max_length=100,
                        verbose_name="template",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cmsplugin_survey.Question",
                        verbose_name="question",
                    ),
                ),
            ],
            bases=("cms.cmsplugin",),
        ),
    ]
