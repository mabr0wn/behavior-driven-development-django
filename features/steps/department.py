# file:features/steps/department.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave     import given, when, then
from hamcrest   import assert_that, equal_to
from testutil   import NamedNumber
from company_model import companyModel

@given('a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    if not Model:
        context.model = companyModel()
    for row in context.table:
        context.model.add_user(row["name"], department=row["department"])
