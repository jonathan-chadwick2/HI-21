from ehrql import create_dataset
from ehrql.codes import codelist_from_csv
from ehrql.tables.core import practice_registrations, clinical_events

dataset = create_dataset()
index_date = "2025-03-31"

autism_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-autism_cod.csv", column="code"
)

has_registration = practice_registrations.for_patient_on(
    index_date
).exists_for_patient()

has_autism = clinical_events.where(
    clinical_events.snomedct_code.is_in(autism_codelist)
).exists_for_patient()

dataset.autism_dat = (
    clinical_events.where(clinical_events.snomedct_code.is_in(autism_codelist))
    .sort_by(clinical_events.date)
    .where(clinical_events.date <= index_date)
    .last_for_patient()
    .date
)

dataset.define_population(has_autism & has_registration)