from random import choice
from dashboard.model.academics import Academic
from dashboard.model.projects import ExpectedImpact, MainFundingCategory, MainFundingDhscNihrFunding, MainFundingIndustryCollaborationOrIndustry, MainFundingSource, Methodology, NihrPriorityArea, Project, ProjectStatus, RacsSubcategory, ResearchType, Theme, TrialPhase, UkcrcHealthCategory, UkcrcResearchActivityCode
from faker.providers import BaseProvider
from faker import Faker
from lbrc_flask.pytest.faker import LbrcFlaskFakerProvider, FakeCreator


class LookupFakeCreator(FakeCreator):
    def get(self, **kwargs):
        fake = Faker("en_GB")
        result = self.cls(
            name=kwargs.get('name', fake.pystr(min_chars=1, max_chars=100))
        )

        return result


class AcademicFakeCreator(FakeCreator):
    def __init__(self):
        super().__init__(Academic)

    def get(self, **kwargs):
        fake = Faker("en_GB")
        fake.add_provider(LbrcFlaskFakerProvider)
        result = self.cls(
            first_name=kwargs.get('first_name', fake.first_name()),
            surname=kwargs.get('surname', fake.last_name()),
            orcid=kwargs.get('orcid', fake.orcid()),
        )

        return result


class ProjectFakeCreator(FakeCreator):
    def __init__(self):
        super().__init__(Project)

    def get(self, **kwargs):
        fake = Faker("en_GB")
        fake.add_provider(LbrcFlaskFakerProvider)
        fake.add_provider(LookupProvider)
        fake.add_provider(AcademicProvider)
        result = self.cls(
            title=kwargs.get('title', fake.sentence()),
            local_rec_number=kwargs.get('local_rec_number', fake.local_rec_number()),
            senstive=kwargs.get('sensitive', fake.pybool()),
            summary=kwargs.get('summary', fake.sentence()),
            iras_number=kwargs.get('iras_number', fake.pyint()),
            crn_rdn_portfolio_study=kwargs.get('crn_rdn_portfolio_study', fake.pybool()),
            crn_rdn_cpms_identifier=kwargs.get('crn_rdn_cpms_identifier', fake.pyint()),
            academic=kwargs.get('academic', fake.academic().get()),
            actual_start_date=kwargs.get('actual_start_date', fake.date_object()),
            end_date=kwargs.get('end_date', fake.date_object()),
            project_status=kwargs.get('project_status', fake.project_status().choice_from_db()),
            theme=kwargs.get('theme', fake.theme().choice_from_db()),
            ukcrc_health_category=kwargs.get('ukcrc_health_category', fake.ukcrc_health_category().choice_from_db()),
            nihr_priority_areas=kwargs.get('nihr_priority_areas', fake.nihr_priority_area().choices_from_db(choice([1,2]))),
            rec_approval_required=kwargs.get('rec_approval_required', fake.pybool()),
            ukcrc_research_activity_code=kwargs.get('ukcrc_research_activity_code', fake.ukcrc_research_activity_code().choice_from_db()),
            racs_subcategory=kwargs.get('racs_subcategory', fake.racs_subcategory().choice_from_db()),
            research_type=kwargs.get('research_type', fake.research_type().choice_from_db()),
            methodology=kwargs.get('methodology', fake.methodology().choice_from_db()),
            expected_impact=kwargs.get('expected_impact', fake.expected_impact().choice_from_db()),
            rendomised_trial=kwargs.get('rendomised_trial', fake.pybool()),
            trial_phase=kwargs.get('trial_phase', fake.trial_phase().choice_from_db()),
            participants_recruited_to_centre_fy=kwargs.get('participants_recruited_to_centre_fy', fake.pyint()),
            brc_funding=kwargs.get('brc_funding', fake.pyint()),
            main_funding_source=kwargs.get('main_funding_source', fake.main_funding_source().choice_from_db()),
            main_funding_category=kwargs.get('main_funding_category', fake.main_funding_category().choice_from_db()),
            main_funding_brc_funding=kwargs.get('main_funding_brc_funding', fake.pyint()),
            main_funding_dhsc_nihr_funding=kwargs.get('main_funding_dhsc_nihr_funding', fake.main_funding_dhsc_nihr_funding().choice_from_db()),
            main_funding_industry_collaboration_or_industry=kwargs.get('main_funding_industry_collaboration_or_industry', fake.main_funding_industry_collaboration_or_industry().choice_from_db()),
            total_external_funding_award=kwargs.get('total_external_funding_award', fake.pyint()),
            first_in_human_project=kwargs.get('first_in_human_project', fake.pybool()),
            link_to_nihr_translational_research_collaboration=kwargs.get('link_to_nihr_translational_research_collaboration', fake.pybool()),
            comments=kwargs.get('comments', fake.paragraph()),
        )

        return result


class LookupProvider(BaseProvider):
    def create_standard_lookups(self):
        for _ in range(5):
            self.project_status().get_in_db()
            self.theme().get_in_db()
            self.ukcrc_health_category().get_in_db()
            self.nihr_priority_area().get_in_db()
            self.ukcrc_research_activity_code().get_in_db()
            self.racs_subcategory().get_in_db()
            self.research_type().get_in_db()
            self.methodology().get_in_db()
            self.expected_impact().get_in_db()
            self.trial_phase().get_in_db()
            self.main_funding_source().get_in_db()
            self.main_funding_category().get_in_db()
            self.main_funding_dhsc_nihr_funding().get_in_db()
            self.main_funding_industry_collaboration_or_industry().get_in_db()

    def project_status(self):
        return LookupFakeCreator(ProjectStatus)        

    def theme(self):
        return LookupFakeCreator(Theme)        

    def ukcrc_health_category(self):
        return LookupFakeCreator(UkcrcHealthCategory)        

    def nihr_priority_area(self):
        return LookupFakeCreator(NihrPriorityArea)        

    def ukcrc_research_activity_code(self):
        return LookupFakeCreator(UkcrcResearchActivityCode)        

    def racs_subcategory(self):
        return LookupFakeCreator(RacsSubcategory)        

    def research_type(self):
        return LookupFakeCreator(ResearchType)        

    def methodology(self):
        return LookupFakeCreator(Methodology)        

    def expected_impact(self):
        return LookupFakeCreator(ExpectedImpact)        

    def trial_phase(self):
        return LookupFakeCreator(TrialPhase)        

    def main_funding_source(self):
        return LookupFakeCreator(MainFundingSource)        

    def main_funding_category(self):
        return LookupFakeCreator(MainFundingCategory)        

    def main_funding_dhsc_nihr_funding(self):
        return LookupFakeCreator(MainFundingDhscNihrFunding)        

    def main_funding_industry_collaboration_or_industry(self):
        return LookupFakeCreator(MainFundingIndustryCollaborationOrIndustry)        


class AcademicProvider(BaseProvider):
    def academic(self):
        return AcademicFakeCreator()        


class ProjectProvider(BaseProvider):
    def project(self):
        return ProjectFakeCreator()        
