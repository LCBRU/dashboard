
from datetime import date
from dashboard.model.academics import Academic
from lbrc_flask.database import db
from lbrc_flask.security import AuditMixin
from lbrc_flask.model import CommonMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text
from dashboard.model.lookups import Lookup


class ProjectStatus(Lookup, db.Model):
    pass

class Theme(Lookup, db.Model):
    pass

class UkcrcHealthCategory(Lookup, db.Model):
    pass

class NihrPriorityArea(Lookup, db.Model):
    pass

class UkcrcResearchActivityCode(Lookup, db.Model):
    pass

class RacsSubcategory(Lookup, db.Model):
    pass

class ResearchType(Lookup, db.Model):
    pass

class Methodology(Lookup, db.Model):
    pass

class ExpectedImpact(Lookup, db.Model):
    pass

class TrialPhase(Lookup, db.Model):
    pass

class MainFundingSource(Lookup, db.Model):
    pass

class MainFundingCategory(Lookup, db.Model):
    pass

class MainFundingDhscNihrFunding(Lookup, db.Model):
    pass

class MainFundingIndustryCollaborationOrIndustry(Lookup, db.Model):
    pass


projects_nihr_priority_areas = db.Table(
    'projects_nihr_priority_areas',
    db.Column(
        'project_id',
        db.Integer(),
        db.ForeignKey('project.id'),
        primary_key=True,
    ),
    db.Column(
        'nihr_priority_area_id',
        db.Integer(),
        db.ForeignKey('nihr_priority_area.id'),
        primary_key=True,
    ),
)


class Project(AuditMixin, CommonMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(1000))
    local_rec_number: Mapped[str] = mapped_column(String(50), index=True)
    senstive: Mapped[bool] = mapped_column()
    summary: Mapped[str] = mapped_column(String(1000))
    iras_number: Mapped[str] = mapped_column(String(50), index=True)
    crn_rdn_portfolio_study: Mapped[bool] = mapped_column()
    crn_rdn_cpms_identifier: Mapped[int] = mapped_column(index=True, nullable=True)
    academic_id: Mapped[int] = mapped_column(ForeignKey(Academic.id), index=True)
    academic: Mapped[Academic] = relationship(foreign_keys=[academic_id])
    actual_start_date: Mapped[date] = mapped_column(index=True)
    end_date: Mapped[date] = mapped_column(index=True, nullable=True)
    project_status_id: Mapped[int] = mapped_column(ForeignKey(ProjectStatus.id), index=True)
    project_status: Mapped[ProjectStatus] = relationship(foreign_keys=[project_status_id])
    theme_id: Mapped[int] = mapped_column(ForeignKey(Theme.id), index=True)
    theme: Mapped[Theme] = relationship(foreign_keys=[theme_id])
    ukcrc_health_category_id: Mapped[int] = mapped_column(ForeignKey(UkcrcHealthCategory.id), index=True)
    ukcrc_health_category: Mapped[UkcrcHealthCategory] = relationship(foreign_keys=[ukcrc_health_category_id])
    nihr_priority_areas = db.relationship(NihrPriorityArea, secondary='projects_nihr_priority_areas')
    rec_approval_required: Mapped[bool] = mapped_column()
    ukcrc_research_activity_code_id: Mapped[int] = mapped_column(ForeignKey(UkcrcResearchActivityCode.id), index=True)
    ukcrc_research_activity_code: Mapped[UkcrcResearchActivityCode] = relationship(foreign_keys=[ukcrc_research_activity_code_id])
    racs_subcategory_id: Mapped[int] = mapped_column(ForeignKey(RacsSubcategory.id), index=True)
    racs_subcategory: Mapped[RacsSubcategory] = relationship(foreign_keys=[racs_subcategory_id])
    research_type_id: Mapped[int] = mapped_column(ForeignKey(ResearchType.id), index=True)
    research_type: Mapped[ResearchType] = relationship(foreign_keys=[research_type_id])
    methodology_id: Mapped[int] = mapped_column(ForeignKey(Methodology.id), index=True)
    methodology: Mapped[Methodology] = relationship(foreign_keys=[methodology_id])
    expected_impact_id: Mapped[int] = mapped_column(ForeignKey(ExpectedImpact.id), index=True)
    expected_impact: Mapped[ExpectedImpact] = relationship(foreign_keys=[expected_impact_id])
    rendomised_trial: Mapped[bool] = mapped_column()
    trial_phase_id: Mapped[int] = mapped_column(ForeignKey(TrialPhase.id), index=True)
    trial_phase: Mapped[TrialPhase] = relationship(foreign_keys=[trial_phase_id])
    participants_recruited_to_centre_fy: Mapped[int] = mapped_column()
    brc_funding: Mapped[int] = mapped_column()
    main_funding_source_id: Mapped[int] = mapped_column(ForeignKey(MainFundingSource.id), index=True)
    main_funding_source: Mapped[MainFundingSource] = relationship(foreign_keys=[main_funding_source_id])
    main_funding_category_id: Mapped[int] = mapped_column(ForeignKey(MainFundingCategory.id), index=True)
    main_funding_category: Mapped[MainFundingCategory] = relationship(foreign_keys=[main_funding_category_id])
    main_funding_brc_funding: Mapped[int] = mapped_column()
    main_funding_dhsc_nihr_funding_id: Mapped[int] = mapped_column(ForeignKey(MainFundingDhscNihrFunding.id), index=True)
    main_funding_dhsc_nihr_funding: Mapped[MainFundingDhscNihrFunding] = relationship(foreign_keys=[main_funding_dhsc_nihr_funding_id])
    main_funding_industry_collaboration_or_industry_id: Mapped[int] = mapped_column(ForeignKey(MainFundingIndustryCollaborationOrIndustry.id), index=True)
    main_funding_industry_collaboration_or_industry: Mapped[MainFundingIndustryCollaborationOrIndustry] = relationship(foreign_keys=[main_funding_industry_collaboration_or_industry_id])
    total_external_funding_award: Mapped[int] = mapped_column()
    first_in_human_project: Mapped[bool] = mapped_column()
    link_to_nihr_translational_research_collaboration: Mapped[bool] = mapped_column()
    comments: Mapped[str] = mapped_column(Text)
