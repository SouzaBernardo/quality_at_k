
class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []



    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions,and add the position information to the job_listings list.
        :param job_title: The title of the position,str.
        :param company: The company of the position,str.
        :param requirements: The requirements of the position,list.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1','requirement2'])
        >>> jobMarketplace.job_listings
        [{'job_title': 'Software Engineer', 'company': 'ABC Company','requirements': ['requirement1','requirement2']}]
        """

    def remove_job(self, job):
        self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes,and add the resume information to the resumes list.
        :param name: The name of the resume,str.
        :param skills: The skills of the resume,list.
        :param experience: The experience of the resume,str.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.submit_resume("Tom", ['skill1','skill2'], "experience")
        >>> jobMarketplace.resumes
        [{'name': 'Tom','skills': ['skill1','skill2'], 'experience': 'experience'}]
        """

    def withdraw_resume(self, resume):
        self.resumes.remove(resume)

    def search_jobs(self, criteria):
        result = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                result.append(job)
        return result

    def get_job_applicants(job_listings, resumes):
        """
        This function is used to obtain candidate information,and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job_listings: The list of positions,list of dicts.
        :param resumes: The list of candidates' resumes,list of dicts.
        :return: The candidate information that meets the requirements,list.
        >>> job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1','skill2']}]
        >>> resumes = [{"name": "Tom", "skills": ['skill1','skill2'], "experience": "experience"}]
        >>> get_job_applicants(job_listings, resumes)
        [{'name': 'Tom','skills': ['skill1','skill2'], 'experience': 'experience'}]
    
        """
        applicants = []
        for job in job_listings:
            for resume in resumes:
                if matches_requirements(resume, job['requirements']):
                    applicants.append(resume)
        return applicants