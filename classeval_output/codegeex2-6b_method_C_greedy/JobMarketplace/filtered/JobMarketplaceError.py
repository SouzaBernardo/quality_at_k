class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []



    def post_job(self, job_title, company, requirements):
        
        self.job_listings.append({'job_title': job_title, 'company': company, 'requirements': requirements})


    def remove_job(self, job):
        
        self.job_listings.remove(job)


    def submit_resume(self, name, skills, experience):
        
        self.resumes.append({'name': name, 'skills': skills, 'experience': experience})


    def withdraw_resume(self, resume):
        
        self.resumes.remove(resume)


    def search_jobs(self, criteria):
        

        return self.job_listings


    def get_job_applicants(self, job):