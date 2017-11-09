# file:features/steps/company_model.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
class Department(object):
    def __init__(self, name, members=None):
        if not members:
            members = []
        self.name = name
        self.members = members
        
    def add_member(self, name):
        assert name not in self.members
        self.memebers.append(name)
        
    """
    will turn this into a read-only attribute,
    show the length of members """
    @property
    def count(self):
        return len(self.members)
      
    ''' return the lenth of count in members '''
    def __len__(self):
        return self.count
      
class CompanyModel(object):
    def __init__(self):
        self.users = [] # List
        self.departments = {} # dictionary
        
    def add_user(self, name, department):
        assert name not in self.users
        if department not in self.departments:
            self.departments[department] = Department(department)
        self.departments[department].add_member(name)
        
    def count_persons_per_department(self):
        pass
      
    def get_headcount_for(self, department):
        return self.departments[deparment].count
