"""
Admin file for btcat project
"""
from django.contrib import admin

from cmponline.models import (Questions, Tests, QuestionBanks, Exams, CategoryTypes, ConceptVideo, ExpertVideo,
                              MockTestSummary, VideoAuthor, StudentUser, QuestionFiles, FeatureFeedback, ForumQue,
                              ForumAns, ForumQALikes, ForumAnsLikes, SummaryNotes, StudentReferralCode, ReferenceBooks,
                              StudentProfilePic)

from studentstats.models import StudentTests_QueBank, StudentTests_mock
from studentstats.models import StudentTheorySections
from studentstats.models import StudentVideos
from studentstats.models import TestData
from studentstats.models import TestQueBank
from studentstats.models import FreeTest

from payments.models import Transactions, Referrals

from instant_eval.models import Instant_answer

admin.site.register(Questions)
admin.site.register(Tests)
admin.site.register(QuestionBanks)
admin.site.register(Exams)
admin.site.register(ExpertVideo)
admin.site.register(ConceptVideo)
admin.site.register(CategoryTypes)
admin.site.register(MockTestSummary)
admin.site.register(VideoAuthor)
admin.site.register(StudentUser)
admin.site.register(QuestionFiles)
admin.site.register(FeatureFeedback)
admin.site.register(ForumQue)
admin.site.register(ForumAns)
admin.site.register(ForumQALikes)
admin.site.register(ForumAnsLikes)
admin.site.register(SummaryNotes)
#admin.site.register(ForumQuestions)
admin.site.register(StudentReferralCode)

# admin.site.register(StudentTests)
admin.site.register(StudentTests_QueBank)
admin.site.register(StudentTests_mock)
admin.site.register(StudentTheorySections)
admin.site.register(StudentVideos)
admin.site.register(TestData)
admin.site.register(TestQueBank)
admin.site.register(FreeTest)

admin.site.register(Transactions)
admin.site.register(Referrals)

admin.site.register(Instant_answer)

admin.site.register(ReferenceBooks)

admin.site.register(StudentProfilePic)
