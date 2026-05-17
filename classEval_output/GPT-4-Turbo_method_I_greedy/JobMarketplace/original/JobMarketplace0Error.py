
class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []


    def post_job(self, job_title, company, requirements):
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)
    def remove_job(self, job):
        if job in self.job_listings:
            self.job_listings.remove(job)
    def submit_resume(self, name, skills, experience):
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)
    def withdraw_resume(self, resume):
        if resume in self.resumes:
            self.resumes.remove(resume)
    def search_jobs(self, criteria):
        matching_jobs = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                matching_jobs.append(job)
        return matching_jobs
    
    def get_job_applicants(self, job):
        matching_resumes = []
        for resume in self.resumes:
            if self.matches_requirements(job, resume):
                matching_resumes.append(resume)
        return matching_resumes
    
