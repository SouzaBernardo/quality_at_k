
class JobMarketplace:  
    """
    This is a class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []
        self.resumes = []






    def remove_job(self, job):
        
        self.job_listings.remove(job)





    def withdraw_resume(self, resume):
        
        self.resumes.remove(resume)


    def search_jobs(self, criteria):
        
        return [job for job in self.job_listings if criteria in job["requirements"]]


    def get_job_applicants(self, job):
        
        return [resume for resume in self.resumes if self.matches_requirements(resume, job)]


    def matches_requirements(self, resume, job):
